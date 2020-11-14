##Copyright Thomas Paviot (tpaviot@gmail.com) and Andreas Plesch (@andreasplesch)
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

__doc__ = "BRep/STEP to X3D exporter """

import os
import uuid
import xml.etree.ElementTree as ET

# core OCC packages
from OCC.Core.gp import gp_XYZ
from OCC.Core.TopAbs import TopAbs_ShapeEnum

# OCC extensions
from OCC.Extend.TopologyUtils import is_edge, is_wire
from OCC.Extend.DataExchange.XDE import SceneGraphFromDoc, DocFromSTEP
from OCC.Extend.Tesselator import ShapeTesselator, EdgeDiscretizer, WireDiscretizer

# official x3d package
import OCC.Extend.DataExchange.x3d_standard.x3d as XX3D


_X3DOM_HEADER = '''<script type='text/javascript' src='https://www.x3dom.org/download/dev/x3dom-full.debug.js'> </script>
<link rel='stylesheet' type='text/css' href='https://www.x3dom.org/download/dev/x3dom.css'></link>
'''
def _flatten(lst):
    """ take nested lists and return flattened values
    """
    return [item for sublist in lst for item in sublist]

def _sanitize_DEF(name):
        # IdFirstChar ::=
        # Any ISO-10646 character encoded using UTF-8 except: 0x30-0x3a, 0x0-0x20, 0x22,
        # 0x23, 0x27, 0x2b, 0x2c, 0x2d, 0x2e, 0x5b, 0x5c, 0x5d, 0x7b, 0x7d, 0x7f ;
        # first no [0-9],space,",#,',+,comma,-,.,[,\,],{,}
        # IdRestChars ::=
        # Any number of ISO-10646 characters except: 0x0-0x20, 0x22, 0x23, 0x27, 0x2c, 0x2e,
        # 0x3a, 0x5b, 0x5c, 0x5d, 0x7b, 0x7d, 0x7f ;
        # rest no space,",#,',comma,.,:,[,\,],{,}
        replace_dict = {" ": "_", '"': '^', '#': 'N', "'": "^", ",": ";",
                        ".": ";", ":": "-", "[": "(", "]": ")", "{": "(",
                        "}": ")", "\\": "/"}
        for k, v in replace_dict.items():
            name = name.replace(k, v)
        return 'L-' + name

class X3DCurveExporter:
    """ A class for exporting 1d topology such as TopoDS_Wire or TopoDS_Edge
    This class takes either a TopoDS_Edge, a TopoDS_Wire or a list of TopoDS_Edge
    or a list of TopoDS_Wire.
    In any case, all that is passd to this exporter is exported to a single
    LineSet instance."""
    def __init__(self, shape):
        self._shape = shape
        self._cd = None

        self._geo = None
        self._edges = None

        self.compute()


    def get_geo(self):
        return self._geo


    def get_edges(self):
        return self._edges


    def compute(self):
        shape_type = self._shape.ShapeType()
        if shape_type == TopAbs_ShapeEnum.TopAbs_EDGE:
            self._cd = EdgeDiscretizer(self._shape)
        elif shape_type == TopAbs_ShapeEnum.TopAbs_WIRE:
            self._cd = WireDiscretizer(self._shape)
        else:
            raise AssertionError('you must provide an edge or a wire to the X3DCurveExporter')

        coord = XX3D.Coordinate(point=self._cd.get_points())
        coord.DEF = "COORD" + uuid.uuid4().hex
        self._geo = XX3D.LineSet(coord=coord)


class X3DLODShapeExporter:
    """ A class that generates several level of detail, with mesh decimation
    """
    def __init__(self, shape, compute_normals=False, compute_edges=True, uid=None,
                 lod_levels=None):
        # LOD levels is a dict with keys: distance from point of view, and
        # the value is the decimation ratio
        # disance is from near to far
        lod_Node = XX3D.LOD()
        lod_Node.range = list(lod_levels.keys())
        # first level
        shp_exporter = X3DShapeExporter(shape, compute_normals, compute_edges, uid)
        shp_exporter.compute()

        # the material for the shape and the edge
        mesh_material = XX3D.Material(DEF='popo',
                                     diffuseColor=(0.4,.4,0.4),
                                     specularColor=(0.9, 0.9, 0.9),
                                     shininess=1, ambientIntensity=0.1)
        edge_material = XX3D.Material(DEF='popo2',
                                     diffuseColor=(0.1,.1,0.1),
                                     specularColor=(0.9, 0.9, 0.9),
                                     shininess=1, ambientIntensity=0.1)

        for lod_level in lod_levels:
            decimation_ratio = lod_levels[lod_level]
            shp_exporter.set_decimation_ratio(decimation_ratio)
            shp_exporter.to_x3d_graph()

            group = XX3D.Group()
           
            # the transform to be used by any of the shapes
            transform_node = XX3D.Transform()
            transform_node.rotation = tuple(shp_exporter._rotation_vector + [shp_exporter._rotation_angle])
            transform_node.translation = tuple(shp_exporter._translation)
            sf = shp_exporter._scale_factor
            transform_node.scale = (sf, sf, sf)

            mesh_shp = shp_exporter.get_X3DShape_mesh()
            
            mesh_shp.appearance = XX3D.Appearance(material=mesh_material)

            # if the decimation ratio is high, no need to export
            # edges as well, only mesh triangles is enough
            if decimation_ratio < 0.8:
                edge_shp = shp_exporter.get_X3DShape_edges()
                edge_shp.appearance = XX3D.Appearance(material=edge_material)
                transform_node.children = [mesh_shp, edge_shp]
            else:
                transform_node.children = [mesh_shp]

            group.children.append(transform_node)

            lod_Node.children.append(group)
        # add the end, add an empty group, as suggested at
        # https://doc.x3dom.org/author/Navigation/LOD.html
        # Camera-to-object distance transitions for each child level,
        # where range values go from near to far. For n range values,
        # you must have n+1 child levels! Hint: can add an empty Group
        # node as nonrendering final child.
        lod_Node.children.append(XX3D.Group())

        self._lod_Node = lod_Node


class X3DShapeExporter:
    """ A class for exporting a single TopoDS_Shape to x3d
    """
    def __init__(self, shape, compute_normals=False, compute_edges=True, uid=None,
                 decimation_ratio=0., mesh_quality=1.0):
        self._compute_normals = compute_normals
        self._compute_edges = compute_edges
        self._mesh_quality = mesh_quality

        # the shape tesselator
        self._shape_tesselator = None

        if uid is None:
            self._uid = uuid.uuid4().hex
        else:
            self._uid = uid

        self._shape = shape
        self._decimation_ratio = decimation_ratio

        self._geo = None
        self._edges = None

        self._bb_center = None
        self._bb_size = None

        self._rotation_vector = None
        self._rotation_angle = None
        self._translation = None
        self._scale_factor = None

        # X3D outputs
        self._x3d_2d_mesh_geometry = None
        self._x3d_edges_geometry = None
        self._x3d_Shape_2d_mesh = None
        self._x3d_Shape_edges = None
        self._x3d_Transform = None

        self.compute()


    def set_decimation_ratio(self, decimation_ratio_value):
        """ method that modifies the decimation ratio, useful if we want another
        decimation ratio level
        """
        self._decimation_ratio = decimation_ratio_value


    def get_X3DTransform(self):
        return self._x3d_Transform


    def get_X3DShape_mesh(self):
        return self._x3d_Shape_2d_mesh


    def get_X3DShape_edges(self):
        return self._x3d_Shape_edges

    
    def get_geo(self):
        return self._x3d_2d_mesh_geometry


    def get_edges(self):
        return self._x3d_edges_geometry


    def compute(self):
        """ compute meshes, return True if successful
        """
        shape_tesselator = ShapeTesselator(self._shape,
                                           compute_normals=self._compute_normals,
                                           compute_edges=self._compute_edges,
                                           mesh_quality=self._mesh_quality)
        # store shape information
        self._bb_center = shape_tesselator.get_bb_center()
        self._bb_size = shape_tesselator.get_bb_size()

        self._rotation_vector, self._rotation_angle = shape_tesselator.get_rotation()
        self._translation = shape_tesselator.get_translation()
        self._scale_factor = shape_tesselator.get_scale_factor()

        # store the shape tesselator
        self._shape_tesselator = shape_tesselator

        self.to_x3d_graph()

    def to_x3d_graph(self, export_bb=False):
        """" taks the tesselator and build an related x3d nodes
        """
        if self._decimation_ratio > 0.:
            self._shape_tesselator.decimate(self._decimation_ratio)

        idx = self._shape_tesselator.get_flattened_vertex_indices()
        coord = XX3D.Coordinate(point=self._shape_tesselator.get_vertex_coords())
        coord.DEF = "ITS-COORD-" + self._uid
        if self._compute_normals:
            # convert list of list to list of tuples since
            # Normal expects a list of tuples as the vector
            normals_as_tuples = list(map(tuple, self._shape_tesselator.get_normal_coords()))
            normal = XX3D.Normal(vector=normals_as_tuples)
        else:
            normal = None
        if coord:
            # if there's a mesh decimation, we don't calculate normal per vertex
            if self._decimation_ratio > 0.:
                normal_per_pertex = False
            else:
                normal_per_pertex = True
            self._x3d_2d_mesh_geometry = XX3D.IndexedTriangleSet(coord=coord,
                                                                 index=idx,
                                                                 normal=normal,
                                                                 normalPerVertex=normal_per_pertex,
                                                                 solid=False)
        # TODO : issue with x3d standard creaseAngle is not a property of this node
        # we need here a creaseAngle of creaseAngle=0.2)

        if self._compute_edges:
            # flatten edges indices
            tmp1 = [[a for a in l] + [-1] for l in self._shape_tesselator._edges_indices]
            edge_idx = [item for sublist in tmp1 for item in sublist]
            if edge_idx:
                if self._decimation_ratio == 0.:  # no decimation, use the vertex coord
                    edge_coord = XX3D.Coordinate(USE=coord.DEF)
                else:  # we can't use the same coordinates that the faces
                    # we use the LOD 0 vertex coordinates, more precise
                    # and decimation algorithm may alter sharp edges
                    default_vert_coord, _, _ = self._shape_tesselator.get_lod()[0.]
                    edge_coord = XX3D.Coordinate(point=default_vert_coord)
                self._x3d_edges_geometry = XX3D.IndexedLineSet(coord=edge_coord, coordIndex=edge_idx)

        # finally create the X3D Shape for this shape
        self._x3d_Shape_2d_mesh = XX3D.Shape()
        self._x3d_Shape_2d_mesh.geometry = self._x3d_2d_mesh_geometry
        if export_bb:
            self._x3d_Shape_2d_mesh.bboxCenter = tuple(self._bb_center)
            self._x3d_Shape_2d_mesh.bboxSize = tuple(self._bb_size)
        child_nodes = [self._x3d_Shape_2d_mesh]

        # another shape for the edges
        if self._compute_edges:
            self._x3d_Shape_edges = XX3D.Shape()
            self._x3d_Shape_edges.geometry = self._x3d_edges_geometry
            child_nodes.append(self._x3d_Shape_edges)

        # transform node
        transform_node = XX3D.Transform(children=child_nodes)
        transform_node.rotation = tuple(self._rotation_vector + [self._rotation_angle])
        transform_node.translation = tuple(self._translation)
        sf = self._scale_factor
        transform_node.scale = (sf, sf, sf)
        self._x3d_Transform = transform_node


class X3DSceneExporter:
    """ creates an x3d scene
    """
    def __init__(self):
        self._x3dscene = XX3D.Scene(children=[])
        self._x3ddoc = XX3D.X3D(Scene=self._x3dscene)

        # keep references for DEFs
        # use a set to prevent duplicates
        self._app_def_set = set()


    def get_scene(self):
        return self._x3dscene


    def get_doc(self):
        return self._x3ddoc


    def add_group(self, group_def_name, DEF=None, USE=None):
        group = XX3D.Group()
        if DEF:
            group.DEF = DEF
        elif USE:
            group.USE = USE
        self._x3dscene.children()


    def add_shape(self, shape, shape_DEF_name=None, shape_color=(0.4, 0.4, 0.4),
                  color_DEF_name=None, emissive=True, edge_color=(0, 0, 0),
                  decimation_ratio = 0., export_edges=True, to_existing_node=None,
                  mesh_quality=1.):
        if decimation_ratio < 0. or decimation_ratio > 1.:
            raise ValueError("decimation ration must be > 0. and < 1.")

        # create the material
        if emissive:
            x3d_material = XX3D.Material(emissiveColor=shape_color)
        else:
            x3d_material = XX3D.Material(diffuseColor=shape_color,
                                         specularColor=(0.9, 0.9, 0.9),
                                         shininess=1, ambientIntensity=0.1)
        if color_DEF_name is not None:
            if color_DEF_name in self._app_def_set:
                shape_appearance = XX3D.Appearance(USE=color_DEF_name)
            else:
                self._app_def_set.add(color_DEF_name)
                shape_appearance = XX3D.Appearance(DEF=color_DEF_name, material=x3d_material)
        else:
            shape_appearance = XX3D.Appearance(material=x3d_material)

        # then process NEW shape node that is added to the Scene node
        if is_edge(shape) or is_wire(shape):
            x3dcurve_geometry = XX3D.Shape()
            x3d_exporter = X3DCurveExporter(shape)
            x3dcurve_geometry.geometry = x3d_exporter.get_geo()
            x3dcurve_geometry.appearance = shape_appearance

            self._x3dscene.children.extend([x3dcurve_geometry])
        else:
            x3d_exporter = X3DShapeExporter(shape,
                                            compute_normals=False,
                                            compute_edges=export_edges,
                                            decimation_ratio= decimation_ratio,
                                            mesh_quality=mesh_quality)

            x3dshape_geometry = x3d_exporter.get_X3DShape_mesh()
            x3dshape_geometry.appearance = shape_appearance

            if export_edges:
                x3dvisible_edge_geometry = x3d_exporter.get_X3DShape_edges()

                edge_material = XX3D.Material(emissiveColor=edge_color)
                edge_appearance = XX3D.Appearance(DEF="edge_material", material=edge_material)
                x3dvisible_edge_geometry.appearance = edge_appearance

            if to_existing_node is None:  # append this shape to the current scene
                self._x3dscene.children.append(x3d_exporter.get_X3DTransform())
            else: # add geometries to the specified node
                index0 = to_existing_node.children[0].geometry.index
                coord0 = to_existing_node.children[0].geometry.coord.point
                index_to_add = x3dshape_geometry.geometry.index
                coord_to_add = x3dshape_geometry.geometry.coord.point
                # we extend the original coord array
                to_existing_node.children[0].geometry.coord.point = coord0 + coord_to_add
                # we translate the index and add it
                decl = len(coord0)
                to_existing_node.children[0].geometry.index = index0 + [l + decl for l in index_to_add]
                return to_existing_node
        return x3d_exporter.get_X3DTransform()
        


    def to_xml(self):
        return self._x3ddoc.XML()


    def to_x3dom_html(self):
        """ x3d adaptation to x3dom library
        """
        xml_content = self.to_xml()
        # root node
        x3d_element = list(ET.XML(xml_content).iter('X3D'))[0]

        # remove gama correction
        next(x3d_element.iter('Scene')).append(ET.XML('<Environment gammaCorrectionDefault="none"/>'))

        # add crease angle to IndexedTriangleSet instances, supported by x3dom
        # but not part of the X3D standard
        for idx_ts in x3d_element.iter('IndexedTriangleSet'):
            idx_ts.set('creaseAngle', '0.2')
        
        x3dHTML = ET.tostring(x3d_element, encoding="unicode", short_empty_elements=False)
        x3dHTML = x3dHTML.replace("visible=", 'render=')
        return _X3DOM_HEADER + x3dHTML


    def write_to_file(self, filename):
        with open(filename, "w") as f:
            f.write(self.to_x3dom_html())


class X3DFromSceneGraph:
    def __init__(self, scene=None, faces_in_solids=None, show_edges=True,
                 edge_color=(0, 0, 0), log=True):
        self._app_def_set = set()

        if faces_in_solids is None:
            self._faces_in_solids = set()
        else:
            self._faces_in_solids = faces_in_solids

        self._scene = scene
        self._show_edges = show_edges
        self._edge_color = edge_color
        self._log = log

        self._x3d_scene = None
        self._x3d_doc = None

        self.build_x3d_scene()


    def to_xml(self):
        return self._x3ddoc.XML()


    def to_x3dom_html(self):
        x3dele = list(ET.XML(self.to_xml()).iter('X3D'))[0]
        next(x3dele.iter('Scene')).append(ET.XML('<Environment gammaCorrectionDefault="none"/>'))
        x3d_html = ET.tostring(x3dele, encoding="unicode", short_empty_elements=False)
        x3d_html = x3d_html.replace("visible=", 'render=')
        return _X3DOM_HEADER + x3d_html


    def build_x3d_scene(self):
        self._x3dscene = XX3D.Scene(children=[])
        self._x3ddoc = XX3D.X3D(Scene=self._x3dscene)

        for node in self._scene:
            success, x3dnodelist = self.get_x3d_node(node)
            if success:
                self._x3dscene.children.extend(x3dnodelist)
            else:
                self.print_log('no x3d for root node, skipped')


    def print_log(self, message):
        if self._log:
            print(message)


    def x3d_apply_location(self, x3dtransformnode, location):
        # get translation and rotation from location
        transformation = location.Transformation()
        rot_axis = gp_XYZ()

        success, rot_angle = transformation.GetRotation(rot_axis)
        translation = transformation.TranslationPart()
        scale_factor = transformation.ScaleFactor()
        x3dtransformnode.rotation = (rot_axis.X(), rot_axis.Y(), rot_axis.Z(), rot_angle)
        x3dtransformnode.translation = (translation.X(), translation.Y(), translation.Z())
        x3dtransformnode.scale = (scale_factor, scale_factor, scale_factor)


    def x3d_geometry_from_TShape(self, shape):
        if is_edge(shape) or is_wire(shape):
            x3d_exporter = X3DCurveExporter(shape)
        else:
            x3d_exporter = X3DShapeExporter(shape, compute_normals=False, compute_edges=True)

        return {'x3dgeo': x3d_exporter.get_geo(), 'x3dedges': x3d_exporter.get_edges()}


    def x3d_appearance_from_color(self, color, DEFname, emissive):
        if emissive:
            DEFname = DEFname + "-emissive"
        if DEFname in self._app_def_set:
            return XX3D.Appearance(USE=DEFname)
        else:
            self._app_def_set.add(DEFname)
            if emissive:
                x3dmat = XX3D.Material(emissiveColor=color)
            else:
                x3dmat = XX3D.Material(diffuseColor=color, specularColor=(0.9, 0.9, 0.9),
                                       shininess=1, ambientIntensity=0.1)
            return XX3D.Appearance(DEF=DEFname, material=x3dmat)


    def apply_DEF_or_USE(self, node, x3dnode):
        if 'USE' in node:
            x3dnode.USE = _sanitize_DEF(node['USE'])
        if 'DEF' in node:
            x3dnode.DEF = _sanitize_DEF(node['DEF'])


    def set_children(self, node, x3dnode):
        if 'children' in node:
            for n in node['children']:
                success, childlist = self.get_x3d_node(n)
                if success:
                    x3dnode.children.extend(childlist)


    def get_x3d_node(self, node):
        if not 'node' in node:
            self.print_log('no node type, skipping')
            return False, None

        if 'DEF' in node:
            if node['DEF'] in self._faces_in_solids:
                return False, None

        if 'is_assembly' in node:
            node_is_assembly = node['is_assembly']
        else:
            node_is_assembly = False

        ntype = node['node']

        edge_node = None

        node_metadata = XX3D.MetadataString(name="type", value=["%s" % node['name']])

        if ntype == 'Group':
            x3dnode = XX3D.CADAssembly()
            x3dnode.metadata = node_metadata
            self.apply_DEF_or_USE(node, x3dnode)
            self.set_children(node, x3dnode)

        elif ntype == 'Transform':
            x3dnode = XX3D.Transform()
            x3dnode.metadata = node_metadata
            if 'transform' in node:
                self.x3d_apply_location(x3dnode, node['transform'])
            self.apply_DEF_or_USE(node, x3dnode)
            self.set_children(node, x3dnode)

        elif ntype in ['Shape', 'SubShape']:
            x3dnode = XX3D.Shape()
            x3dnode.metadata = node_metadata
            self.apply_DEF_or_USE(node, x3dnode)
            if 'shape' in node:
                shape = node['shape']
                geometry_dict = self.x3d_geometry_from_TShape(shape)
                x3dnode.geometry = geometry_dict['x3dgeo']
                is_edge_or_wire = is_edge(shape) or is_wire(shape)
                if 'color' in node:
                    color_def = _sanitize_DEF(node['color_uid'])
                    x3dnode.appearance = self.x3d_appearance_from_color(tuple(node['color']), color_def, is_edge_or_wire)
                if not is_edge_or_wire:
                    node_metadata.value = [node['name'] + '-edge']
                    edge_node = XX3D.Shape(visible=self._show_edges)
                    edge_node.geometry = geometry_dict['x3dedges']
                    edge_node.appearance = self.x3d_appearance_from_color(self._edge_color, 'app-faceedge', True)
                    edge_node.metadata = node_metadata
        else:
            self.print_log('unknown node: --' + ntype + "--")

        x3dnodelist = [x3dnode]
        if edge_node is not None:
            x3dnodelist.append(edge_node)

        return True, x3dnodelist


if __name__ == "__main__":
    # test with the as1_pe.stp file
    from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox, BRepPrimAPI_MakeTorus
    

    #scene_exp = X3DSceneExporter()
    #scene_exp.add_shape(shp, shape_color=(0.5, 0.6, 0.7), emissive=False)

    #scene_exp.write_to_file('ess.x3d')
    step_file = os.path.join('..', '..', '..', 'test', 'test_io', 'as1_pe_203.stp')
    doc_exp = DocFromSTEP(step_file)
    document = doc_exp.get_doc()
    scenegraph = SceneGraphFromDoc(document)
    x3dXML = X3DFromSceneGraph(scene=scenegraph.get_scene(),
                               faces_in_solids=scenegraph.get_internal_face_entries(),
                               log=True)
    with open('out.x3d', 'w') as f:
        f.write(x3dXML.to_xml())
    x3dXML.to_x3dom_html()

    print("LOD test")
    box_shp = BRepPrimAPI_MakeTorus(40, 10).Shape()
    rff = X3DLODShapeExporter(box_shp, lod_levels={200:0.4, 500:0.9, 1000:0.99})
    x3dscene = XX3D.Scene(children=[])
    x3ddoc = XX3D.X3D(Scene=x3dscene)
    x3dscene.children.append(rff._lod_Node)
    with open('out_LOD.x3d', 'w') as f:
        f.write(x3ddoc.XML())