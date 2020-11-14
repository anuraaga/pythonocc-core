##Copyright 2020 Thomas Paviot (tpaviot@gmail.com)
##
##This file is part of pythonOCC.
##
##pythonOCC is free software: you can redistribute it and/or modify
##it under the terms of the GNU Lesser General Public License as published by
##the Free Software Foundation, either version 3 of the License, or
##(at your option) any later version.
##
##pythonOCC is distributed in the hope that it will be useful,
##but WITHOUT ANY WARRANTY; without even the implied warranty of
##MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##GNU Lesser General Public License for more details.
##
##You should have received a copy of the GNU Lesser General Public License
##along with pythonOCC.  If not, see <http://www.gnu.org/licenses/>.

from math import pi
import time

from OCC.Core.TopExp import (TopExp_Explorer, topexp_MapShapes, topexp_MapShapesAndAncestors)
from OCC.Core.BRepTools import breptools_Clean
from OCC.Core.BRepMesh import BRepMesh_DiscretFactory_Get
from OCC.Core.BRep import BRep_Tool_Triangulation, BRep_Tool_Polygon3D, BRep_Tool_PolygonOnTriangulation
from OCC.Core.TopLoc import TopLoc_Location
from OCC.Core.Bnd import Bnd_Box
from OCC.Core.BndLib import BndLib_Add3dCurve_Add
from OCC.Core.BRepBndLib import brepbndlib_Add
from OCC.Core.TopAbs import TopAbs_Orientation, TopAbs_ShapeEnum
from OCC.Core.BRepGProp import BRepGProp_Face
from OCC.Core.TopoDS import topods_Edge, topods_Face
from OCC.Core.gp import gp_Pnt, gp_Vec, gp_Trsf, gp_XYZ
from OCC.Core.TopTools import TopTools_IndexedDataMapOfShapeListOfShape, TopTools_IndexedMapOfShape
from OCC.Core.BRepAdaptor import BRepAdaptor_Curve
from OCC.Core.GeomAbs import GeomAbs_C1, GeomAbs_Line
from OCC.Core.TColStd import TColStd_Array1OfReal
from OCC.Core.GCPnts import GCPnts_TangentialDeflection
from OCC.Core.Precision import precision_Confusion

from OCC.Extend.TopologyUtils import TopologyExplorer, WireExplorer, check_shape

try:
    import vtk
    HAVE_VTK = True
except:
    HAVE_VTK = False


def _flatten(lst):
    """ take nested lists and return flattened values
    """
    return [item for sublist in lst for item in sublist]


def _test_flatten():
    assert _flatten([[1, 2, 3], [4, 5, 6]]) == [1, 2, 3, 4, 5, 6]


class WireDiscretizer:
    def __init__(self, a_wire):
        curve_type = a_wire.ShapeType()
        if curve_type != TopAbs_ShapeEnum.TopAbs_WIRE:
            raise AssertionError('you must pass a wire to this class')
        self._wire = a_wire
        self._pnts = []

        self.discretize()

    def get_points(self):
        return self._pnts

    def discretize(self):
        """ splitthe wire into edges, discretize each edge and
        merge points lists
        """
        wire_explorer = WireExplorer(self._wire)
        wire_pnts = []
        for edg in wire_explorer.ordered_edges():
            edg_dscrtzr = EdgeDiscretizer(edg)
            wire_pnts += edg_dscrtzr.get_points()
        self._pnts = wire_pnts


class EdgeDiscretizer:
    def __init__(self, a_curve):
        curve_type = a_curve.ShapeType()
        if curve_type != TopAbs_ShapeEnum.TopAbs_EDGE:
            raise AssertionError("You must provide a wire or a curve to the CurveDiscretizer class.")

        # the pnts
        self._pnts = []

        # curve properties
        self._curve = a_curve
        self._curve_adaptator = BRepAdaptor_Curve(self._curve)
        self._U1 = self._curve_adaptator.FirstParameter()
        self._U2 = self._curve_adaptator.LastParameter()

        self._deviation = 0.3
        self._angular_deflection = 5. * pi / 180.0

        # bbsize and center, as lists
        # None by default, lists if computation successfull
        self._bb = None
        self._bb_size = None
        self._bb_center = None
        self.compute_bounding_box()

        self.discretize()


    def get_points(self):
        return self._pnts


    def compute_bounding_box(self):
        """ computes and stores the curve bounding box
        """
        curve_bounding_box = Bnd_Box()
        BndLib_Add3dCurve_Add(self._curve_adaptator, self._U1, self._U2, 0., curve_bounding_box)

        x_min, y_min, z_min, x_max, y_max, z_max = curve_bounding_box.Get()

        dx, dy, dz = x_max - x_min, y_max - y_min, z_max - z_min
        px, py, pz = x_max + dx / 2., y_max + dy / 2., z_min + dz / 2.

        self._bb = curve_bounding_box
        self._bb_size = [dx, dy, dz]
        self._bb_center = [px, py, pz]


    def compute_deviation(self):
        dx, dy, dz = self._bb_size
        max_param_value = 500000.
        default_deviation = 0.3
        if not (self._bb.IsOpenXmin() or self._bb.IsOpenXmax()):
            m = abs(dx)
        if not (self._bb.IsOpenYmin() or self._bb.IsOpenYmax()):
            m = max(m, abs(dy))
        if not (self._bb.IsOpenZmin() or self._bb.IsOpenZmax()):
            m = max(m, abs(dz))

        m = min(m, max_param_value)
        m = max(m, precision_Confusion())

        self._deviation = m * default_deviation


    def discretize(self):
        """ build the point sets as a list of 3d coordinates
        """
        # cas of a line
        # first compute the deviation
        self.compute_deviation()

        if self._curve_adaptator.GetType() == GeomAbs_Line:
            p1 = self._curve_adaptator.Value(self._U1)
            p2 = self._curve_adaptator.Value(self._U2)
            pnts = [[p1.X(), p1.Y(), p1.Z()], [p2.X(), p2.Y(), p2.Z()]]
        # other cases
        else:
            nb_inter = self._curve_adaptator.NbIntervals(GeomAbs_C1)
            #print("Intervals:", nb_inter)
            T = TColStd_Array1OfReal(1, nb_inter+1)
            self._curve_adaptator.Intervals(T, GeomAbs_C1)

            pnts = []

            for j in range(1, nb_inter + 1):
                current_u1 = T.Value(j)
                current_u2 = T.Value(j+1)
                if current_u1 < self._U2 and current_u2 > self._U1:
                    current_u1 = max(current_u1, self._U1)
                    current_u2 = max(current_u2, self._U2)
                    algo = GCPnts_TangentialDeflection(self._curve_adaptator,
                                                       self._U1,
                                                       self._U2,
                                                       self._angular_deflection,
                                                       self._deviation)

                    for i in range(1, algo.NbPoints() + 1):
                        p = self._curve_adaptator.Value(algo.Parameter(i))
                        pnts.append([p.X(), p.Y(), p.Z()])
        self._pnts = pnts


class Tesselator:
    def __init__(self, a_topods_shape, compute_normals=False,
                 compute_edges=False, mesh_quality=1., global_coordinates=False,
                 check_shape_before=True):
        if check_shape_before:  # first check that shape
            is_valid, fixed_shape_if_not_valid = check_shape(a_topods_shape, fix=True)
            if not is_valid:  # take the fixed shape
                self._shape = fixed_shape_if_not_valid
            else: # take the original shape
                self._shape = a_topods_shape
        else:
            self._shape = a_topods_shape

        # options
        self._compute_normals = compute_normals
        self._compute_edges = compute_edges
        self._mesh_quality = mesh_quality
        self._global_coordinates = global_coordinates

        # the indexed geometry representation
        self._vertex_coords = []
        self._vertex_indices = []
        self._normal_coords = []


        # the vtk version of the original mesh
        # the decimated mesh must not be stored here
        self._vtkpolydata = None

        # the transformation (translation, rotation) related to the geometry
        default_location = TopLoc_Location()
        default_location.Identity()
        self._transformation = default_location.Transformation()

        # bbsize and center, as lists
        # None by default, lists if computation successfull
        self._bb_size = None
        self._bb_center = None

        # bounding sphere, computed from the bounding box
        # bounding sphere is used by threejs
        self._bs_radius = None
        self._bs_center = None

        self.tesselate() # this method has to be implemented for each child class

        self.compute_bounding_box()


    def get_lod(self):
        """ returns the lod dictionnary
        """
        return self._lod


    def set_default_lod_level(self):
        self.set_lod_level(0.)


    def set_current_lod_level(self, ratio):
        """ sets the current lod level for the mesh information
        """
        if not ratio in self._lod:
            raise KeyError("No such LOD level")
        else:
            self._vertex_coords, self._vertex_indices, self._normal_coords = self._lod[ratio]


    def compute_bounding_box(self):
        """ compute the bounding box and sphere
        """
        shp_bounding_box = Bnd_Box()
        brepbndlib_Add(self._shape, shp_bounding_box, False)
        if shp_bounding_box.IsVoid():
            return False
        elif shp_bounding_box.IsOpen():
            if not shp_bounding_box.HasFinitePart():
                return False
            else:
                print("Shape bounding box is open, using finite part.")
                shp_bounding_box = shp_bounding_box.FinitePart()
        x_min, y_min, z_min, x_max, y_max, z_max = shp_bounding_box.Get()

        dx, dy, dz = x_max - x_min, y_max - y_min, z_max - z_min
        px, py, pz = x_max + dx / 2., y_max + dy / 2., z_min + dz / 2.

        self._bb_size = [dx, dy, dz]
        self._bb_center = [px, py, pz]

        # the bounding sphere is computed from the bounding box
        # same center, radius is half the max of dx, d, dz
        self._bs_radius = max(self._bb_size) / 2.
        self._bs_center = self._bb_center

        return True


    def get_mesh_density(self):
        """ returns the number of points per volume unit and
        triangles per volume unit
        """
        n_points = len(self._vertex_coords)
        n_tri = len(self._vertex_indices)
        vol = self.get_bb_volume()

        return n_points / vol, n_tri / vol


    def get_bb_volume(self):
        sx, sy, sz = self._bb_size
        return sx * sy * sz


    def get_bb_size(self):
        return self._bb_size


    def get_bb_center(self):
        return self._bb_center


    def get_bs_size(self):
        return self._bs_size


    def get_bs_center(self):
        return self._bs_center


    def get_vertex_coords(self):
        return self._vertex_coords


    def get_normal_coords(self):
        return self._normal_coords


    def get_vertex_indices(self):
        return self._vertex_indices


    def get_flattened_vertex_coords(self):
        return _flatten(self._vertex_coords)


    def get_flattened_normal_coords(self):
        return _flatten(self._normal_coords)


    def get_flattened_vertex_indices(self):
        return _flatten(self._vertex_indices)


    def tesselate(self):
        raise NotImplementedError("this method has to be implemented in each class")


    def get_transformation(self):
        return self._transformation


    def get_scale_factor(self):
        """ returns a float
        """
        return self._transformation.ScaleFactor()


    def get_translation(self):
        """ returns a triple [x, y, z] related to the translational part
        of the transformation """
        tr = self._transformation.TranslationPart()
        return [tr.X(), tr.Y(), tr.Z()]


    def get_rotation(self):
        """ from the transformation, return a vector and an angle
        """
        ax = gp_XYZ()
        _, angle = self._transformation.GetRotation(ax)
        return [ax.X(), ax.Y(), ax.Z()], angle


    def to_vtk(self):
        """ returns a vtkpolydata representation of the mesh
        """
        if not HAVE_VTK:
            print("vtk not installed, method unavailable.")
            return False

        vertex_coords = self.get_vertex_coords()
        vertex_indices = self.get_vertex_indices()

        points = vtk.vtkPoints()
        triangles = vtk.vtkCellArray()

        for face in vertex_indices:
            point_id_1 = points.InsertNextPoint(vertex_coords[face[0]])
            point_id_2 = points.InsertNextPoint(vertex_coords[face[1]])
            point_id_3 = points.InsertNextPoint(vertex_coords[face[2]])
            triangles.InsertNextCell(3, (point_id_1, point_id_2, point_id_3))

        # create the mesh polydata from points and triangles arrays
        polydata = vtk.vtkPolyData()
        polydata.SetPoints(points)
        polydata.SetPolys(triangles)

        # clean_mesh:
        cleaner1 = vtk.vtkCleanPolyData()
        cleaner1.SetInputData(polydata)
        cleaner1.Update()
        cleaned_polydata = cleaner1.GetOutput()

        self._vtkpolydata = cleaned_polydata

        return cleaned_polydata


    def vtkpolydata_to_mesh(self, polydata_input):
        """ takes a computed tesselator instance, returns an indexed set of
        vertex indices, coords and normals
        """
        if not HAVE_VTK:
            print("vtk not installed, method unavailable.")
            return False

        points = polydata_input.GetPoints()
        dataArray = points.GetData()
        numberOfFaces = polydata_input.GetNumberOfCells()
        size = dataArray.GetSize()
        # coords
        coords = []
        number_of_coords = dataArray.GetSize()
        for i in range(0, number_of_coords, 3):
            coords.append([dataArray.GetValue(i),
                           dataArray.GetValue(i + 1),
                           dataArray.GetValue(i + 2)])

        # faces indices
        face_index = vtk.vtkIdList()
        indices = []
        for i in range(numberOfFaces):
            polydata_input.GetCellPoints(i, face_index)
            nb_of_ids = face_index.GetNumberOfIds()
            if nb_of_ids != 3: # degenerated edge
                print("WARNING: detected degenerated edge")
                continue
            face_indices = [face_index.GetId(0),
                            face_index.GetId(1),
                            face_index.GetId(2)]
            indices.append(face_indices)

        return coords, indices


    def decimate(self, decimation_ratio):
        """" decimation ratio, a float between 0 and 1.
        0 : no decimation
        0.5 : 50% decimation (i.e. 50% less triangles)
        1 : 100% decimation (all points/triangles removed)
        """
        if not HAVE_VTK:
            print("vtk not installed, method unavailable.")
            return False

        # first create a vtk polydata from vertex coords and indices
        if self._vtkpolydata is None:
            self.to_vtk()

        print("Before decimation\n"
            "-----------------\n"
            "There are " + str(self._vtkpolydata.GetNumberOfPoints()) + "points.\n"
            "There are " + str(self._vtkpolydata.GetNumberOfPolys()) + "polygons.\n")

        # perform the vtk decimation
        init_time = time.perf_counter()
        decimate = vtk.vtkQuadricDecimation()
        decimate.SetInputData(self._vtkpolydata)
        decimate.SetTargetReduction(decimation_ratio)
        decimate.SetVolumePreservation(True)
        decimate.AttributeErrorMetricOn()
        decimate.Update()
        
        # fix normals orientation
        normals = vtk.vtkPolyDataNormals()
        normals.SetInputData(decimate.GetOutput())
        normals.SetFeatureAngle(20.0)
        normals.ComputePointNormalsOn()
        normals.ComputeCellNormalsOn()
        normals.SplittingOn()
        normals.AutoOrientNormalsOn()  # important, reorder vertices
        normals.Update()
        
        # the result of the vtkPolyDataNormals filter is
        # a non indexed triangle set. Thus the number of triangles is much
        # lower, but the number of points drastically increases. The vtkCleanPolyData
        # filter is useful to merge points but it does not save the normals orientation

        cleaner1 = vtk.vtkCleanPolyData()
        cleaner1.SetInputData(normals.GetOutput())
        cleaner1.Update()

        decimatedPoly = cleaner1.GetOutput()

        final_time = time.perf_counter()
        print("Time for decimation ", str(final_time - init_time), "s")
          
        print("After decimation \n"
              "-----------------\n"
              "There are " + str(decimatedPoly.GetNumberOfPoints()) + "points.\n"
              "There are " + str(decimatedPoly.GetNumberOfPolys()) + "polygons.\n")
        # convert back the vtkpolydata to an indexed triangle set
        coords, indices = self.vtkpolydata_to_mesh(decimatedPoly)


        self._lod[decimation_ratio] = (coords, indices, [])

        self.set_current_lod_level(decimation_ratio)

        # return True if ok
        return decimatedPoly

    
class FaceTesselator(Tesselator):
    """ Face tesselator. Compute the face triangulation and returns an indexed geometry:
    * the vertex coordinates, in absolute or relative mode
    * the vertex indices
    * the transformation as a gp_Trsf
    """
    def __init__(self, *kargs):
        super(FaceTesselator, self).__init__(*kargs)


    def tesselate(self):
        aLocation = TopLoc_Location()
        myT = BRep_Tool_Triangulation(self._shape, aLocation)

        # store the transformation
        self._transformation = aLocation.Transformation()

        if myT is None:
            return False

        vertex_coords = []
        # write vertex buffer
        nodes = myT.Nodes()
        for i in range(nodes.Lower(), nodes.Upper() + 1):
            if self._global_coordinates:
                p = nodes(i).Transformed(aLocation.Transformation())
            else:
                p = nodes(i)
            vertex_coords.append([p.X(), p.Y(), p.Z()])

        # write triangle buffer
        tri_indexes = []
        orient = self._shape.Orientation()
        triangles = myT.Triangles()

        for nt in range(myT.NbTriangles()):
            n0, n1, n2 = triangles(nt + 1).Get()
            if orient not in [TopAbs_Orientation.TopAbs_REVERSED, TopAbs_Orientation.TopAbs_INTERNAL]:
                tri_indexes.append([n0, n1, n2])
            else:
                tri_indexes.append([n0, n2, n1])

        # compute normals, if required
        normal_coords = []
        if self._compute_normals and myT.HasUVNodes():
            prop = BRepGProp_Face(self._shape)
            uvnodes = myT.UVNodes()
            ilower = uvnodes.Lower()
            iBufferSize = uvnodes.Upper() - uvnodes.Lower() + 1

            for i in range(uvnodes.Lower(), uvnodes.Upper() + 1):
                uv_pnt = uvnodes(i)
                p = gp_Pnt()
                n = gp_Vec()
                prop.Normal(uv_pnt.X(), uv_pnt.Y(), p, n)
                if n.SquareMagnitude() > 0.:
                    n.Normalize()
                if self._shape.Orientation() == TopAbs_Orientation.TopAbs_INTERNAL:
                    n.Reverse()
                normal_coords.append([n.X(), n.Y(), n.Z()])

        # store arrays
        self._vertex_coords = vertex_coords
        self._vertex_indices = tri_indexes
        self._normal_coords = normal_coords

        return True


class ShapeTesselator(Tesselator):
    def __init__(self, a_topods_shape,
                 compute_normals=False,
                 compute_edges=False,
                 mesh_quality=1.,
                 global_coordinates=True):
        self._edges_indices = []

        # level of detail
        # a level of detail is a list of tuples (coords, indices, normal)
        self._lod = {}

        # parameters for initial triangulation
        self._deviation = 0.3
        self._angular_deflection = 20.0 * pi / 180.0

        super().__init__(a_topods_shape, compute_normals, compute_edges, mesh_quality,
                         global_coordinates)


    def compute_edges(self):
        M = TopTools_IndexedMapOfShape()
        topexp_MapShapes(self._shape, TopAbs_ShapeEnum.TopAbs_EDGE, M)

        # explore all boundary edges
        edgeMap = TopTools_IndexedDataMapOfShapeListOfShape()
        topexp_MapShapesAndAncestors(self._shape, TopAbs_ShapeEnum.TopAbs_EDGE, TopAbs_ShapeEnum.TopAbs_FACE, edgeMap)

        for iEdge in range(edgeMap.Size()):
            faceList = edgeMap.FindFromIndex(iEdge + 1)

            if faceList.Size() == 0:
                continue

            aFace = topods_Face(faceList.First())
            anEdge = topods_Edge(M(iEdge + 1))
            myTransf = gp_Trsf()
            aLoc = TopLoc_Location()
            aPoly = BRep_Tool_Polygon3D(anEdge, aLoc)

            if aPoly is not None:
                print("The poly is not null.")
            else:
                aFace = topods_Face(edgeMap.FindFromIndex(iEdge + 1).First())
                # take the face's triangulation instead
                aPolyTria = BRep_Tool_Triangulation(aFace, aLoc)
                if not aLoc.IsIdentity():
                    myTransf = aLoc.Transformation()
                if aPolyTria is None:
                    break
                # this holds the indices of the edge's triangulation
                # to the actual points
                aPoly = BRep_Tool_PolygonOnTriangulation(anEdge, aPolyTria, aLoc)
                if aPoly is None:
                    continue

                indices = aPoly.Nodes()
                Nodes = aPolyTria.Nodes()

                edge_indices = []
                # go through the index array
                for i in range(indices.Lower(), indices.Upper() + 1):
                    # node index in face triangulation
                    V = Nodes(indices.Value(i))
                    if self._global_coordinates:
                        V.Transform(myTransf)
                    vertex_coord = [V.X(), V.Y(), V.Z()]
                    if vertex_coord in self._vertex_coords:
                        idx_found = self._vertex_coords.index(vertex_coord)
                        edge_indices.append(idx_found)
                    else:  # it should not !!
                        print("edge not in list :", vertex_coord)
                self._edges_indices.append(edge_indices)


    def compute_deviation(self):
        """ compute the deviation for the mesh
        """
        default_deviation = 0.3
        if self._bb_size is None:
            self._deviation = default_deviation
        else:
            max_comp_diag = max(self._bb_size)
            deviation_coefficient = 0.001
            self._deviation = max_comp_diag * 4 * deviation_coefficient


    def tesselate(self):
        """ tesselate the shape
        """
        #print("Tesselate shape ... ", end="")
        self.compute_deviation()
        # clean shape to remove any previous tringulation
        breptools_Clean(self._shape)
        # Triangulate
        msh_algo = BRepMesh_DiscretFactory_Get().Discret(self._shape,
                                                         self._deviation * self._mesh_quality,
                                                         self._angular_deflection * self._mesh_quality)
        msh_algo.Perform()
        all_vertex_coords = []
        all_vertex_indices = []
        all_normal_coords = []

        # face explorer
        face_explorer = TopExp_Explorer(self._shape, TopAbs_ShapeEnum.TopAbs_FACE)

        advance = 0

        while face_explorer.More():
            face = topods_Face(face_explorer.Current())

            ft = FaceTesselator(face, self._compute_normals,
                                self._compute_edges, self._mesh_quality, self._global_coordinates)

            face_vertex_coords = ft.get_vertex_coords()
            face_vertex_indices = ft.get_vertex_indices()
            face_normal_coords = ft.get_normal_coords()

            all_vertex_coords += face_vertex_coords
            all_normal_coords += face_normal_coords

            # transform the face_vertex_indices
            indices_translated = [[a - 1 + advance for a in l] for l in face_vertex_indices]
            all_vertex_indices += indices_translated

            face_explorer.Next()
            advance += len(face_vertex_coords)

        # store information
        self._vertex_coords = all_vertex_coords
        self._vertex_indices = all_vertex_indices
        self._normal_coords = all_normal_coords

        # the first level of detail (_lod[0])
        self._lod[0.] = (all_vertex_coords, all_vertex_indices, all_normal_coords)

        # we store the shape transformation
        self._transformation = self._shape.Location().Transformation()

        # compute edges, if need
        if self._compute_edges:
            self.compute_edges()
        #print("done.")


if __name__ == "__main__":
    _test_flatten()
    from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox, BRepPrimAPI_MakeTorus
    from OCC.Extend.ShapeFactory import translate_shp
    from OCC.Core.gp import gp_Vec

    box = BRepPrimAPI_MakeBox(10, 20, 30).Shape()
    box = BRepPrimAPI_MakeTorus(30, 10).Shape()
    bo_t = translate_shp(box, gp_Vec(0, 0, 10), copy=False)
    #t = BRepPrimAPI_MakeBox(100, 20, 30).Shape()
    import time
    init_time = time.perf_counter()
    tess = ShapeTesselator(bo_t, compute_normals=True, compute_edges=True, mesh_quality=0.1)
    #print(tess.get_vertex_indices())
    #print(tess.get_vertex_coords())
    #print(tess.get_normal_coords())
    nb_i = len(tess.get_vertex_indices())
    nb_v = len(tess.get_vertex_coords())
    nb_n = len(tess.get_normal_coords())
    final_time = time.perf_counter()
    print('Nb indices :', nb_i)
    print('Nb vertices:', nb_v)
    print('Nb normals:', nb_n)
    print('Triangles, points density:', tess.get_mesh_density())
    #print('Edges:', tess._edges_indices)
    print('Translation', tess.get_translation())
    print('Rotation', tess.get_rotation())
    print(final_time - init_time)
    # # compare with the c++ tesselator
    # from OCC.Core.Tesselator import ShapeTesselator
    # init_time = time.perf_counter()
    # tess = ShapeTesselator(bo_t)
    # tess.Compute(compute_normals=True)
    # print(tess.GetVertexIndices())
    # print(tess.GetVertexCoords())
    # final_time = time.perf_counter()
    # nb_i = len(tess.GetVertexIndices())
    # nb_v = len(tess.GetVertexCoords())

    # print('Nb indices :', nb_i)
    # print('Nb vertices:', nb_v)

    # print(final_time - init_time)
    # build and descretize and helix

    from OCC.Core.gp import gp_Pnt2d, gp_XOY, gp_Lin2d, gp_Ax3, gp_Dir2d
    from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
    from OCC.Core.Geom import Geom_CylindricalSurface
    from OCC.Core.GCE2d import GCE2d_MakeSegment
    # First buil an helix
    aCylinder = Geom_CylindricalSurface(gp_Ax3(gp_XOY()), 6.0)
    aLine2d = gp_Lin2d(gp_Pnt2d(0.0, 0.0), gp_Dir2d(1.0, 1.0))
    aSegment = GCE2d_MakeSegment(aLine2d, 0.0, pi * 2.0)

    helix_edge = BRepBuilderAPI_MakeEdge(aSegment.Value(), aCylinder, 0.0, 6.0 * pi).Edge()
    print("helix curve build ok")
    a_curve_discretizer = EdgeDiscretizer(helix_edge)

    from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeSphere, BRepPrimAPI_MakeTorus, BRepPrimAPI_MakeBox
    torus = BRepPrimAPI_MakeTorus(30., 10).Shape()
    box = BRepPrimAPI_MakeBox(10, 20, 30).Shape()
    import sys
    # loads brep shape
    # create a rendering window and renderer
    ren = vtk.vtkRenderer()
    renWin = vtk.vtkRenderWindow()
    renWin.AddRenderer(ren)
    a_tess = ShapeTesselator(torus)
    print(a_tess.get_mesh_density())
    #a_polydata = a_tess.to_vtk()
    decimated_pd = a_tess.decimate(0.75)
    print(a_tess.get_mesh_density())
    # mapper
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputData(decimated_pd)
    # actor
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    ren.AddActor(actor)
    iren = vtk.vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)
    iren.Initialize()
    renWin.Render()
    iren.Start()