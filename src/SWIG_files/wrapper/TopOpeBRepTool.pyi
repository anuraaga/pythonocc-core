from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.BRepClass3d import *
from OCC.Core.TopTools import *
from OCC.Core.TopoDS import *
from OCC.Core.TopAbs import *
from OCC.Core.Bnd import *
from OCC.Core.TColStd import *
from OCC.Core.Geom2d import *
from OCC.Core.GeomAdaptor import *
from OCC.Core.Geom import *
from OCC.Core.TColgp import *
from OCC.Core.gp import *
from OCC.Core.TopExp import *
from OCC.Core.BRepAdaptor import *
from OCC.Core.TCollection import *
from OCC.Core.GeomAbs import *
from OCC.Core.Extrema import *

#the following typedef cannot be wrapped as is
TopOpeBRepTool_IndexedDataMapOfShapeBox = NewType('TopOpeBRepTool_IndexedDataMapOfShapeBox', Any)
#the following typedef cannot be wrapped as is
TopOpeBRepTool_IndexedDataMapOfShapeBox2d = NewType('TopOpeBRepTool_IndexedDataMapOfShapeBox2d', Any)
#the following typedef cannot be wrapped as is
TopOpeBRepTool_IndexedDataMapOfShapeconnexity = NewType('TopOpeBRepTool_IndexedDataMapOfShapeconnexity', Any)
TopOpeBRepTool_PShapeClassifier = NewType('TopOpeBRepTool_PShapeClassifier', TopOpeBRepTool_ShapeClassifier)
TopOpeBRepTool_PSoClassif = NewType('TopOpeBRepTool_PSoClassif', BRepClass3d_SolidClassifier)
TopOpeBRepTool_Plos = NewType('TopOpeBRepTool_Plos', TopTools_ListOfShape)

class TopOpeBRepTool_ListOfC2DF:
    def __init__(self) -> None: ...
    def __len__(self) -> int: ...
    def Size(self) -> int: ...
    def Clear(self) -> None: ...
    def First(self) -> TopOpeBRepTool_C2DF: ...
    def Last(self) -> TopOpeBRepTool_C2DF: ...
    def Append(self, theItem: TopOpeBRepTool_C2DF) -> TopOpeBRepTool_C2DF: ...
    def Prepend(self, theItem: TopOpeBRepTool_C2DF) -> TopOpeBRepTool_C2DF: ...
    def RemoveFirst(self) -> None: ...
    def Reverse(self) -> None: ...

class TopOpeBRepTool_OutCurveType(IntEnum):
	TopOpeBRepTool_BSPLINE1: int = ...
	TopOpeBRepTool_APPROX: int = ...
	TopOpeBRepTool_INTERPOL: int = ...
TopOpeBRepTool_BSPLINE1 = TopOpeBRepTool_OutCurveType.TopOpeBRepTool_BSPLINE1
TopOpeBRepTool_APPROX = TopOpeBRepTool_OutCurveType.TopOpeBRepTool_APPROX
TopOpeBRepTool_INTERPOL = TopOpeBRepTool_OutCurveType.TopOpeBRepTool_INTERPOL

class topopebreptool:
	@staticmethod
	def CorrectONUVISO(F: TopoDS_Face, Fsp: TopoDS_Face) -> bool: ...
	@staticmethod
	def MakeFaces(F: TopoDS_Face, LOF: TopTools_ListOfShape, MshNOK: TopTools_IndexedMapOfOrientedShape, LOFF: TopTools_ListOfShape) -> bool: ...
	@overload
	@staticmethod
	def PurgeClosingEdges(F: TopoDS_Face, FF: TopoDS_Face, MWisOld: TopTools_DataMapOfShapeInteger, MshNOK: TopTools_IndexedMapOfOrientedShape) -> bool: ...
	@overload
	@staticmethod
	def PurgeClosingEdges(F: TopoDS_Face, LOF: TopTools_ListOfShape, MWisOld: TopTools_DataMapOfShapeInteger, MshNOK: TopTools_IndexedMapOfOrientedShape) -> bool: ...
	@staticmethod
	def Regularize(aFace: TopoDS_Face, aListOfFaces: TopTools_ListOfShape, ESplits: TopTools_DataMapOfShapeListOfShape) -> bool: ...
	@staticmethod
	def RegularizeFace(aFace: TopoDS_Face, OldWiresnewWires: TopTools_DataMapOfShapeListOfShape, aListOfFaces: TopTools_ListOfShape) -> bool: ...
	@staticmethod
	def RegularizeShells(aSolid: TopoDS_Solid, OldSheNewShe: TopTools_DataMapOfShapeListOfShape, FSplits: TopTools_DataMapOfShapeListOfShape) -> bool: ...
	@staticmethod
	def RegularizeWires(aFace: TopoDS_Face, OldWiresNewWires: TopTools_DataMapOfShapeListOfShape, ESplits: TopTools_DataMapOfShapeListOfShape) -> bool: ...

class TopOpeBRepTool_AncestorsTool:
	@staticmethod
	def MakeAncestors(S: TopoDS_Shape, TS: TopAbs_ShapeEnum, TA: TopAbs_ShapeEnum, M: TopTools_IndexedDataMapOfShapeListOfShape) -> None: ...

class TopOpeBRepTool_BoxSort:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, T: TopOpeBRepTool_HBoxTool) -> None: ...
	def AddBoxes(self, S: TopoDS_Shape, TS: TopAbs_ShapeEnum, TA: Optional[TopAbs_ShapeEnum] = TopAbs_SHAPE) -> None: ...
	def AddBoxesMakeCOB(self, S: TopoDS_Shape, TS: TopAbs_ShapeEnum, TA: Optional[TopAbs_ShapeEnum] = TopAbs_SHAPE) -> None: ...
	def Box(self, S: TopoDS_Shape) -> Bnd_Box: ...
	def Clear(self) -> None: ...
	def Compare(self, S: TopoDS_Shape) -> TColStd_ListIteratorOfListOfInteger: ...
	def HAB(self) -> Bnd_HArray1OfBox: ...
	def HABShape(self, I: int) -> TopoDS_Shape: ...
	def HBoxTool(self) -> TopOpeBRepTool_HBoxTool: ...
	def MakeCOB(self, S: TopoDS_Shape, TS: TopAbs_ShapeEnum, TA: Optional[TopAbs_ShapeEnum] = TopAbs_SHAPE) -> None: ...
	def MakeHAB(self, S: TopoDS_Shape, TS: TopAbs_ShapeEnum, TA: Optional[TopAbs_ShapeEnum] = TopAbs_SHAPE) -> None: ...
	@staticmethod
	def MakeHABCOB(HAB: Bnd_HArray1OfBox, COB: Bnd_Box) -> None: ...
	def SetHBoxTool(self, T: TopOpeBRepTool_HBoxTool) -> None: ...
	def TouchedShape(self, I: TColStd_ListIteratorOfListOfInteger) -> TopoDS_Shape: ...

class TopOpeBRepTool_C2DF:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, PC: Geom2d_Curve, f2d: float, l2d: float, tol: float, F: TopoDS_Face) -> None: ...
	def Face(self) -> TopoDS_Face: ...
	def IsFace(self, F: TopoDS_Face) -> bool: ...
	def IsPC(self, PC: Geom2d_Curve) -> bool: ...
	def PC(self) -> Tuple[Geom2d_Curve, float, float, float]: ...
	def SetFace(self, F: TopoDS_Face) -> None: ...
	def SetPC(self, PC: Geom2d_Curve, f2d: float, l2d: float, tol: float) -> None: ...

class TopOpeBRepTool_CLASSI:
	def __init__(self) -> None: ...
	def Add2d(self, S: TopoDS_Shape) -> bool: ...
	def ClassiBnd2d(self, S1: TopoDS_Shape, S2: TopoDS_Shape, tol: float, checklarge: bool) -> int: ...
	def Classilist(self, lS: TopTools_ListOfShape, mapgreasma: TopTools_DataMapOfShapeListOfShape) -> bool: ...
	def Classip2d(self, S1: TopoDS_Shape, S2: TopoDS_Shape, stabnd2d12: int) -> int: ...
	def GetBox2d(self, S: TopoDS_Shape, Box2d: Bnd_Box2d) -> bool: ...
	def Getface(self, S: TopoDS_Shape, fa: TopOpeBRepTool_face) -> bool: ...
	def HasInit2d(self) -> bool: ...
	def Init2d(self, Fref: TopoDS_Face) -> None: ...

class TopOpeBRepTool_CORRISO:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, FRef: TopoDS_Face) -> None: ...
	def AddNewConnexity(self, V: TopoDS_Vertex, E: TopoDS_Edge) -> bool: ...
	def Connexity(self, V: TopoDS_Vertex, Eds: TopTools_ListOfShape) -> bool: ...
	def EdgeOUTofBoundsUV(self, E: TopoDS_Edge, onU: bool, tolx: float) -> Tuple[int, float]: ...
	@overload
	def EdgeWithFaultyUV(self, E: TopoDS_Edge) -> Tuple[bool, int]: ...
	@overload
	def EdgeWithFaultyUV(self, EdsToCheck: TopTools_ListOfShape, nfybounds: int, fyE: TopoDS_Shape) -> Tuple[bool, int]: ...
	def EdgesOUTofBoundsUV(self, EdsToCheck: TopTools_ListOfShape, onU: bool, tolx: float, FyEds: TopTools_DataMapOfOrientedShapeInteger) -> bool: ...
	def EdgesWithFaultyUV(self, EdsToCheck: TopTools_ListOfShape, nfybounds: int, FyEds: TopTools_DataMapOfOrientedShapeInteger, stopatfirst: Optional[bool] = False) -> bool: ...
	def Eds(self) -> TopTools_ListOfShape: ...
	def Fref(self) -> TopoDS_Face: ...
	def GASref(self) -> GeomAdaptor_Surface: ...
	def GetnewS(self, newS: TopoDS_Face) -> bool: ...
	def Init(self, S: TopoDS_Shape) -> bool: ...
	def PurgeFyClosingE(self, ClEds: TopTools_ListOfShape, fyClEds: TopTools_ListOfShape) -> bool: ...
	def Refclosed(self, x: int) -> Tuple[bool, float]: ...
	def RemoveOldConnexity(self, V: TopoDS_Vertex, E: TopoDS_Edge) -> bool: ...
	def S(self) -> TopoDS_Shape: ...
	def SetConnexity(self, V: TopoDS_Vertex, Eds: TopTools_ListOfShape) -> bool: ...
	def SetUVRep(self, E: TopoDS_Edge, C2DF: TopOpeBRepTool_C2DF) -> bool: ...
	def Tol(self, I: int, tol3d: float) -> float: ...
	def TrslUV(self, onU: bool, FyEds: TopTools_DataMapOfOrientedShapeInteger) -> bool: ...
	def UVClosed(self) -> bool: ...
	def UVRep(self, E: TopoDS_Edge, C2DF: TopOpeBRepTool_C2DF) -> bool: ...

class TopOpeBRepTool_CurveTool:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, OCT: TopOpeBRepTool_OutCurveType) -> None: ...
	@overload
	def __init__(self, GT: TopOpeBRepTool_GeomTool) -> None: ...
	def ChangeGeomTool(self) -> TopOpeBRepTool_GeomTool: ...
	def GetGeomTool(self) -> TopOpeBRepTool_GeomTool: ...
	@staticmethod
	def IsProjectable(S: TopoDS_Shape, C: Geom_Curve) -> bool: ...
	@staticmethod
	def MakeBSpline1fromPnt(P: TColgp_Array1OfPnt) -> Geom_Curve: ...
	@staticmethod
	def MakeBSpline1fromPnt2d(P: TColgp_Array1OfPnt2d) -> Geom2d_Curve: ...
	def MakeCurves(self, min: float, max: float, C3D: Geom_Curve, PC1: Geom2d_Curve, PC2: Geom2d_Curve, S1: TopoDS_Shape, S2: TopoDS_Shape, C3DN: Geom_Curve, PC1N: Geom2d_Curve, PC2N: Geom2d_Curve) -> Tuple[bool, float, float]: ...
	@staticmethod
	def MakePCurveOnFace(S: TopoDS_Shape, C: Geom_Curve, first: Optional[float] = 0.0, last: Optional[float] = 0.0) -> Tuple[Geom2d_Curve, float]: ...
	def SetGeomTool(self, GT: TopOpeBRepTool_GeomTool) -> None: ...

class TopOpeBRepTool_FuseEdges:
	def __init__(self, theShape: TopoDS_Shape, PerformNow: Optional[bool] = False) -> None: ...
	def AvoidEdges(self, theMapEdg: TopTools_IndexedMapOfShape) -> None: ...
	def Edges(self, theMapLstEdg: TopTools_DataMapOfIntegerListOfShape) -> None: ...
	def Faces(self, theMapFac: TopTools_DataMapOfShapeShape) -> None: ...
	def NbVertices(self) -> int: ...
	def Perform(self) -> None: ...
	def ResultEdges(self, theMapEdg: TopTools_DataMapOfIntegerShape) -> None: ...
	def Shape(self) -> TopoDS_Shape: ...

class TopOpeBRepTool_GeomTool:
	def __init__(self, TypeC3D: Optional[TopOpeBRepTool_OutCurveType] = TopOpeBRepTool_BSPLINE1, CompC3D: Optional[bool] = True, CompPC1: Optional[bool] = True, CompPC2: Optional[bool] = True) -> None: ...
	def CompC3D(self) -> bool: ...
	def CompPC1(self) -> bool: ...
	def CompPC2(self) -> bool: ...
	@overload
	def Define(self, TypeC3D: TopOpeBRepTool_OutCurveType, CompC3D: bool, CompPC1: bool, CompPC2: bool) -> None: ...
	@overload
	def Define(self, TypeC3D: TopOpeBRepTool_OutCurveType) -> None: ...
	@overload
	def Define(self, GT: TopOpeBRepTool_GeomTool) -> None: ...
	def DefineCurves(self, CompC3D: bool) -> None: ...
	def DefinePCurves1(self, CompPC1: bool) -> None: ...
	def DefinePCurves2(self, CompPC2: bool) -> None: ...
	def GetTolerances(self) -> Tuple[float, float]: ...
	def NbPntMax(self) -> int: ...
	def SetNbPntMax(self, NbPntMax: int) -> None: ...
	def SetTolerances(self, tol3d: float, tol2d: float) -> None: ...
	def TypeC3D(self) -> TopOpeBRepTool_OutCurveType: ...

class TopOpeBRepTool_HBoxTool(Standard_Transient):
	def __init__(self) -> None: ...
	def AddBox(self, S: TopoDS_Shape) -> None: ...
	def AddBoxes(self, S: TopoDS_Shape, TS: TopAbs_ShapeEnum, TA: Optional[TopAbs_ShapeEnum] = TopAbs_SHAPE) -> None: ...
	@overload
	def Box(self, S: TopoDS_Shape) -> Bnd_Box: ...
	@overload
	def Box(self, I: int) -> Bnd_Box: ...
	def ChangeIMS(self) -> TopOpeBRepTool_IndexedDataMapOfShapeBox: ...
	def Clear(self) -> None: ...
	@staticmethod
	def ComputeBox(S: TopoDS_Shape, B: Bnd_Box) -> None: ...
	@staticmethod
	def ComputeBoxOnVertices(S: TopoDS_Shape, B: Bnd_Box) -> None: ...
	@staticmethod
	def DumpB(B: Bnd_Box) -> None: ...
	def Extent(self) -> int: ...
	def HasBox(self, S: TopoDS_Shape) -> bool: ...
	def IMS(self) -> TopOpeBRepTool_IndexedDataMapOfShapeBox: ...
	def Index(self, S: TopoDS_Shape) -> int: ...
	def Shape(self, I: int) -> TopoDS_Shape: ...

class TopOpeBRepTool_PurgeInternalEdges:
	def __init__(self, theShape: TopoDS_Shape, PerformNow: Optional[bool] = True) -> None: ...
	def Faces(self, theMapFacLstEdg: TopTools_DataMapOfShapeListOfShape) -> None: ...
	def IsDone(self) -> bool: ...
	def NbEdges(self) -> int: ...
	def Perform(self) -> None: ...
	def Shape(self) -> TopoDS_Shape: ...

class TopOpeBRepTool_REGUS:
	def __init__(self) -> None: ...
	def GetFsplits(self, Fsplits: TopTools_DataMapOfShapeListOfShape) -> None: ...
	def GetOshNsh(self, OshNsh: TopTools_DataMapOfShapeListOfShape) -> None: ...
	def Init(self, S: TopoDS_Shape) -> None: ...
	def InitBlock(self) -> bool: ...
	def MapS(self) -> bool: ...
	def NearestF(self, e: TopoDS_Edge, lof: TopTools_ListOfShape, ffound: TopoDS_Face) -> bool: ...
	def NextinBlock(self) -> bool: ...
	def REGU(self) -> bool: ...
	def S(self) -> TopoDS_Shape: ...
	def SetFsplits(self, Fsplits: TopTools_DataMapOfShapeListOfShape) -> None: ...
	def SetOshNsh(self, OshNsh: TopTools_DataMapOfShapeListOfShape) -> None: ...
	@staticmethod
	def SplitF(Fanc: TopoDS_Face, FSplits: TopTools_ListOfShape) -> bool: ...
	def SplitFaces(self) -> bool: ...
	@staticmethod
	def WireToFace(Fanc: TopoDS_Face, nWs: TopTools_ListOfShape, nFs: TopTools_ListOfShape) -> bool: ...

class TopOpeBRepTool_REGUW:
	def __init__(self, FRef: TopoDS_Face) -> None: ...
	def AddNewConnexity(self, v: TopoDS_Vertex, OriKey: int, e: TopoDS_Edge) -> bool: ...
	def Connexity(self, v: TopoDS_Vertex, co: TopOpeBRepTool_connexity) -> bool: ...
	def Fref(self) -> TopoDS_Face: ...
	def GetEsplits(self, Esplits: TopTools_DataMapOfShapeListOfShape) -> None: ...
	def GetOwNw(self, OwNw: TopTools_DataMapOfShapeListOfShape) -> None: ...
	def GetSplits(self, Splits: TopTools_ListOfShape) -> bool: ...
	def HasInit(self) -> bool: ...
	def Init(self, S: TopoDS_Shape) -> None: ...
	def InitBlock(self) -> bool: ...
	def MapS(self) -> bool: ...
	def NearestE(self, loe: TopTools_ListOfShape, efound: TopoDS_Edge) -> bool: ...
	def NextinBlock(self) -> bool: ...
	@overload
	def REGU(self, istep: int, Scur: TopoDS_Shape, Splits: TopTools_ListOfShape) -> bool: ...
	@overload
	def REGU(self) -> bool: ...
	def RemoveOldConnexity(self, v: TopoDS_Vertex, OriKey: int, e: TopoDS_Edge) -> bool: ...
	def S(self) -> TopoDS_Shape: ...
	def SetEsplits(self, Esplits: TopTools_DataMapOfShapeListOfShape) -> None: ...
	def SetOwNw(self, OwNw: TopTools_DataMapOfShapeListOfShape) -> None: ...
	def SplitEds(self) -> bool: ...
	def UpdateMultiple(self, v: TopoDS_Vertex) -> bool: ...

class TopOpeBRepTool_ShapeClassifier:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, SRef: TopoDS_Shape) -> None: ...
	def ChangeSolidClassifier(self) -> TopOpeBRepTool_SolidClassifier: ...
	def ClearAll(self) -> None: ...
	def ClearCurrent(self) -> None: ...
	def P2D(self) -> gp_Pnt2d: ...
	def P3D(self) -> gp_Pnt: ...
	@overload
	def SameDomain(self) -> int: ...
	@overload
	def SameDomain(self, samedomain: int) -> None: ...
	def SetReference(self, SRef: TopoDS_Shape) -> None: ...
	def State(self) -> TopAbs_State: ...
	def StateP2DReference(self, P2D: gp_Pnt2d) -> None: ...
	def StateP3DReference(self, P3D: gp_Pnt) -> None: ...
	@overload
	def StateShapeReference(self, S: TopoDS_Shape, AvoidS: TopoDS_Shape) -> TopAbs_State: ...
	@overload
	def StateShapeReference(self, S: TopoDS_Shape, LAvoidS: TopTools_ListOfShape) -> TopAbs_State: ...
	@overload
	def StateShapeShape(self, S: TopoDS_Shape, SRef: TopoDS_Shape, samedomain: Optional[int] = 0) -> TopAbs_State: ...
	@overload
	def StateShapeShape(self, S: TopoDS_Shape, AvoidS: TopoDS_Shape, SRef: TopoDS_Shape) -> TopAbs_State: ...
	@overload
	def StateShapeShape(self, S: TopoDS_Shape, LAvoidS: TopTools_ListOfShape, SRef: TopoDS_Shape) -> TopAbs_State: ...

class TopOpeBRepTool_ShapeExplorer(TopExp_Explorer):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, S: TopoDS_Shape, ToFind: TopAbs_ShapeEnum, ToAvoid: Optional[TopAbs_ShapeEnum] = TopAbs_SHAPE) -> None: ...
	def Index(self) -> int: ...
	def Init(self, S: TopoDS_Shape, ToFind: TopAbs_ShapeEnum, ToAvoid: Optional[TopAbs_ShapeEnum] = TopAbs_SHAPE) -> None: ...
	def Next(self) -> None: ...

class TopOpeBRepTool_ShapeTool:
	@staticmethod
	def AdjustOnPeriodic(S: TopoDS_Shape) -> Tuple[float, float]: ...
	@overload
	@staticmethod
	def BASISCURVE(C: Geom_Curve) -> Geom_Curve: ...
	@overload
	@staticmethod
	def BASISCURVE(E: TopoDS_Edge) -> Geom_Curve: ...
	@overload
	@staticmethod
	def BASISSURFACE(S: Geom_Surface) -> Geom_Surface: ...
	@overload
	@staticmethod
	def BASISSURFACE(F: TopoDS_Face) -> Geom_Surface: ...
	@staticmethod
	def Closed(S1: TopoDS_Shape, S2: TopoDS_Shape) -> bool: ...
	@staticmethod
	def CurvesSameOriented(C1: BRepAdaptor_Curve, C2: BRepAdaptor_Curve) -> bool: ...
	@overload
	@staticmethod
	def EdgeData(BRAC: BRepAdaptor_Curve, P: float, T: gp_Dir, N: gp_Dir) -> Tuple[float, float]: ...
	@overload
	@staticmethod
	def EdgeData(E: TopoDS_Shape, P: float, T: gp_Dir, N: gp_Dir) -> Tuple[float, float]: ...
	@staticmethod
	def EdgesSameOriented(E1: TopoDS_Shape, E2: TopoDS_Shape) -> bool: ...
	@staticmethod
	def FacesSameOriented(F1: TopoDS_Shape, F2: TopoDS_Shape) -> bool: ...
	@staticmethod
	def PeriodizeParameter(par: float, EE: TopoDS_Shape, FF: TopoDS_Shape) -> float: ...
	@staticmethod
	def Pnt(S: TopoDS_Shape) -> gp_Pnt: ...
	@overload
	@staticmethod
	def Resolution3d(SU: Geom_Surface, Tol2d: float) -> float: ...
	@overload
	@staticmethod
	def Resolution3d(F: TopoDS_Face, Tol2d: float) -> float: ...
	@staticmethod
	def Resolution3dU(SU: Geom_Surface, Tol2d: float) -> float: ...
	@staticmethod
	def Resolution3dV(SU: Geom_Surface, Tol2d: float) -> float: ...
	@staticmethod
	def ShapesSameOriented(S1: TopoDS_Shape, S2: TopoDS_Shape) -> bool: ...
	@staticmethod
	def SurfacesSameOriented(S1: BRepAdaptor_Surface, S2: BRepAdaptor_Surface) -> bool: ...
	@staticmethod
	def Tolerance(S: TopoDS_Shape) -> float: ...
	@overload
	@staticmethod
	def UVBOUNDS(S: Geom_Surface) -> Tuple[bool, bool, float, float, float, float]: ...
	@overload
	@staticmethod
	def UVBOUNDS(F: TopoDS_Face) -> Tuple[bool, bool, float, float, float, float]: ...

class TopOpeBRepTool_SolidClassifier:
	def __init__(self) -> None: ...
	@overload
	def Classify(self, S: TopoDS_Solid, P: gp_Pnt, Tol: float) -> TopAbs_State: ...
	@overload
	def Classify(self, S: TopoDS_Shell, P: gp_Pnt, Tol: float) -> TopAbs_State: ...
	def Clear(self) -> None: ...
	def LoadShell(self, S: TopoDS_Shell) -> None: ...
	def LoadSolid(self, S: TopoDS_Solid) -> None: ...
	def State(self) -> TopAbs_State: ...

class TopOpeBRepTool_TOOL:
	@staticmethod
	def ClosedE(E: TopoDS_Edge, vclo: TopoDS_Vertex) -> bool: ...
	@staticmethod
	def ClosedS(F: TopoDS_Face) -> bool: ...
	@staticmethod
	def CurvE(E: TopoDS_Edge, par: float, tg0: gp_Dir) -> Tuple[bool, float]: ...
	@staticmethod
	def CurvF(F: TopoDS_Face, uv: gp_Pnt2d, tg0: gp_Dir) -> Tuple[bool, float, bool]: ...
	@staticmethod
	def EdgeONFace(par: float, ed: TopoDS_Edge, uv: gp_Pnt2d, fa: TopoDS_Face) -> Tuple[bool, bool]: ...
	@staticmethod
	def Getduv(f: TopoDS_Face, uv: gp_Pnt2d, dir: gp_Vec, factor: float, duv: gp_Dir2d) -> bool: ...
	@staticmethod
	def Getstp3dF(p: gp_Pnt, f: TopoDS_Face, uv: gp_Pnt2d, st: TopAbs_State) -> bool: ...
	@overload
	@staticmethod
	def IsClosingE(E: TopoDS_Edge, F: TopoDS_Face) -> bool: ...
	@overload
	@staticmethod
	def IsClosingE(E: TopoDS_Edge, W: TopoDS_Shape, F: TopoDS_Face) -> bool: ...
	@overload
	@staticmethod
	def IsQuad(E: TopoDS_Edge) -> bool: ...
	@overload
	@staticmethod
	def IsQuad(F: TopoDS_Face) -> bool: ...
	@overload
	@staticmethod
	def IsonCLO(PC: Geom2d_Curve, onU: bool, xfirst: float, xperiod: float, xtol: float) -> bool: ...
	@overload
	@staticmethod
	def IsonCLO(C2DF: TopOpeBRepTool_C2DF, onU: bool, xfirst: float, xperiod: float, xtol: float) -> bool: ...
	@overload
	@staticmethod
	def Matter(d1: gp_Vec, d2: gp_Vec, ref: gp_Vec) -> float: ...
	@overload
	@staticmethod
	def Matter(d1: gp_Vec2d, d2: gp_Vec2d) -> float: ...
	@overload
	@staticmethod
	def Matter(xx1: gp_Dir, nt1: gp_Dir, xx2: gp_Dir, nt2: gp_Dir, tola: float) -> Tuple[bool, float]: ...
	@overload
	@staticmethod
	def Matter(f1: TopoDS_Face, f2: TopoDS_Face, e: TopoDS_Edge, pare: float, tola: float) -> Tuple[bool, float]: ...
	@staticmethod
	def MatterKPtg(f1: TopoDS_Face, f2: TopoDS_Face, e: TopoDS_Edge) -> Tuple[bool, float]: ...
	@staticmethod
	def MkShell(lF: TopTools_ListOfShape, She: TopoDS_Shape) -> None: ...
	@staticmethod
	def NgApp(par: float, E: TopoDS_Edge, F: TopoDS_Face, tola: float, ngApp: gp_Dir) -> bool: ...
	@staticmethod
	def NggeomF(uv: gp_Pnt2d, F: TopoDS_Face, ng: gp_Vec) -> bool: ...
	@staticmethod
	def Nt(uv: gp_Pnt2d, f: TopoDS_Face, normt: gp_Dir) -> bool: ...
	@staticmethod
	def OnBoundary(par: float, E: TopoDS_Edge) -> int: ...
	@staticmethod
	def OriinSor(sub: TopoDS_Shape, S: TopoDS_Shape, checkclo: Optional[bool] = False) -> int: ...
	@staticmethod
	def OriinSorclosed(sub: TopoDS_Shape, S: TopoDS_Shape) -> int: ...
	@staticmethod
	def ParE(Iv: int, E: TopoDS_Edge) -> float: ...
	@staticmethod
	def ParE2d(p2d: gp_Pnt2d, e: TopoDS_Edge, f: TopoDS_Face) -> Tuple[bool, float, float]: ...
	@staticmethod
	def ParISO(p2d: gp_Pnt2d, e: TopoDS_Edge, f: TopoDS_Face) -> Tuple[bool, float]: ...
	@staticmethod
	def Remove(loS: TopTools_ListOfShape, toremove: TopoDS_Shape) -> bool: ...
	@staticmethod
	def SplitE(Eanc: TopoDS_Edge, Splits: TopTools_ListOfShape) -> bool: ...
	@staticmethod
	def Tg2d(iv: int, E: TopoDS_Edge, C2DF: TopOpeBRepTool_C2DF) -> gp_Vec2d: ...
	@staticmethod
	def Tg2dApp(iv: int, E: TopoDS_Edge, C2DF: TopOpeBRepTool_C2DF, factor: float) -> gp_Vec2d: ...
	@staticmethod
	def TgINSIDE(v: TopoDS_Vertex, E: TopoDS_Edge, Tg: gp_Vec) -> Tuple[bool, int]: ...
	@overload
	@staticmethod
	def TggeomE(par: float, BC: BRepAdaptor_Curve, Tg: gp_Vec) -> bool: ...
	@overload
	@staticmethod
	def TggeomE(par: float, E: TopoDS_Edge, Tg: gp_Vec) -> bool: ...
	@staticmethod
	def TolP(E: TopoDS_Edge, F: TopoDS_Face) -> float: ...
	@staticmethod
	def TolUV(F: TopoDS_Face, tol3d: float) -> float: ...
	@staticmethod
	def TrslUV(t2d: gp_Vec2d, C2DF: TopOpeBRepTool_C2DF) -> None: ...
	@staticmethod
	def TrslUVModifE(t2d: gp_Vec2d, F: TopoDS_Face, E: TopoDS_Edge) -> bool: ...
	@staticmethod
	def UVF(par: float, C2DF: TopOpeBRepTool_C2DF) -> gp_Pnt2d: ...
	@overload
	@staticmethod
	def UVISO(PC: Geom2d_Curve, d2d: gp_Dir2d, o2d: gp_Pnt2d) -> Tuple[bool, bool, bool]: ...
	@overload
	@staticmethod
	def UVISO(C2DF: TopOpeBRepTool_C2DF, d2d: gp_Dir2d, o2d: gp_Pnt2d) -> Tuple[bool, bool, bool]: ...
	@overload
	@staticmethod
	def UVISO(E: TopoDS_Edge, F: TopoDS_Face, d2d: gp_Dir2d, o2d: gp_Pnt2d) -> Tuple[bool, bool, bool]: ...
	@staticmethod
	def Vertex(Iv: int, E: TopoDS_Edge) -> TopoDS_Vertex: ...
	@staticmethod
	def Vertices(E: TopoDS_Edge, Vces: TopTools_Array1OfShape) -> None: ...
	@staticmethod
	def WireToFace(Fref: TopoDS_Face, mapWlow: TopTools_DataMapOfShapeListOfShape, lFs: TopTools_ListOfShape) -> bool: ...
	@staticmethod
	def XX(uv: gp_Pnt2d, f: TopoDS_Face, par: float, e: TopoDS_Edge, xx: gp_Dir) -> bool: ...
	@staticmethod
	def minDUV(F: TopoDS_Face) -> float: ...
	@staticmethod
	def outUVbounds(uv: gp_Pnt2d, F: TopoDS_Face) -> bool: ...
	@staticmethod
	def stuvF(uv: gp_Pnt2d, F: TopoDS_Face) -> Tuple[int, int]: ...
	@staticmethod
	def tryNgApp(par: float, E: TopoDS_Edge, F: TopoDS_Face, tola: float, ng: gp_Dir) -> bool: ...
	@staticmethod
	def tryOriEinF(par: float, E: TopoDS_Edge, F: TopoDS_Face) -> int: ...
	@staticmethod
	def tryTg2dApp(iv: int, E: TopoDS_Edge, C2DF: TopOpeBRepTool_C2DF, factor: float) -> gp_Vec2d: ...
	@staticmethod
	def uvApp(f: TopoDS_Face, e: TopoDS_Edge, par: float, eps: float, uvapp: gp_Pnt2d) -> bool: ...

class TopOpeBRepTool_connexity:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, Key: TopoDS_Shape) -> None: ...
	@overload
	def AddItem(self, OriKey: int, Item: TopTools_ListOfShape) -> None: ...
	@overload
	def AddItem(self, OriKey: int, Item: TopoDS_Shape) -> None: ...
	def AllItems(self, Item: TopTools_ListOfShape) -> int: ...
	def ChangeItem(self, OriKey: int) -> TopTools_ListOfShape: ...
	def IsFaulty(self) -> bool: ...
	def IsInternal(self, Item: TopTools_ListOfShape) -> int: ...
	def IsMultiple(self) -> bool: ...
	def Item(self, OriKey: int, Item: TopTools_ListOfShape) -> int: ...
	def Key(self) -> TopoDS_Shape: ...
	@overload
	def RemoveItem(self, OriKey: int, Item: TopoDS_Shape) -> bool: ...
	@overload
	def RemoveItem(self, Item: TopoDS_Shape) -> bool: ...
	def SetKey(self, Key: TopoDS_Shape) -> None: ...

class TopOpeBRepTool_face:
	def __init__(self) -> None: ...
	def Ffinite(self) -> TopoDS_Face: ...
	def Finite(self) -> bool: ...
	def Init(self, W: TopoDS_Wire, Fref: TopoDS_Face) -> bool: ...
	def IsDone(self) -> bool: ...
	def RealF(self) -> TopoDS_Face: ...
	def W(self) -> TopoDS_Wire: ...

class TopOpeBRepTool_makeTransition:
	def __init__(self) -> None: ...
	def Getfactor(self) -> float: ...
	def HasRest(self) -> bool: ...
	def Initialize(self, E: TopoDS_Edge, pbef: float, paft: float, parE: float, FS: TopoDS_Face, uv: gp_Pnt2d, factor: float) -> bool: ...
	def IsT2d(self) -> bool: ...
	def MkT2donE(self, stb: TopAbs_State, sta: TopAbs_State) -> bool: ...
	def MkT3dproj(self, stb: TopAbs_State, sta: TopAbs_State) -> bool: ...
	def MkT3onE(self, stb: TopAbs_State, sta: TopAbs_State) -> bool: ...
	def MkTonE(self, stb: TopAbs_State, sta: TopAbs_State) -> bool: ...
	def SetRest(self, ES: TopoDS_Edge, parES: float) -> bool: ...
	def Setfactor(self, factor: float) -> None: ...

#classnotwrapped
class TopOpeBRepTool_STATE: ...

#classnotwrapped
class TopOpeBRepTool_mkTondgE: ...

# harray1 classes
# harray2 classes
# hsequence classes

topopebreptool_CorrectONUVISO = topopebreptool.CorrectONUVISO
topopebreptool_MakeFaces = topopebreptool.MakeFaces
topopebreptool_Print = topopebreptool.Print
topopebreptool_PurgeClosingEdges = topopebreptool.PurgeClosingEdges
topopebreptool_PurgeClosingEdges = topopebreptool.PurgeClosingEdges
topopebreptool_Regularize = topopebreptool.Regularize
topopebreptool_RegularizeFace = topopebreptool.RegularizeFace
topopebreptool_RegularizeShells = topopebreptool.RegularizeShells
topopebreptool_RegularizeWires = topopebreptool.RegularizeWires
TopOpeBRepTool_AncestorsTool_MakeAncestors = TopOpeBRepTool_AncestorsTool.MakeAncestors
TopOpeBRepTool_BoxSort_MakeHABCOB = TopOpeBRepTool_BoxSort.MakeHABCOB
TopOpeBRepTool_CurveTool_IsProjectable = TopOpeBRepTool_CurveTool.IsProjectable
TopOpeBRepTool_CurveTool_MakeBSpline1fromPnt = TopOpeBRepTool_CurveTool.MakeBSpline1fromPnt
TopOpeBRepTool_CurveTool_MakeBSpline1fromPnt2d = TopOpeBRepTool_CurveTool.MakeBSpline1fromPnt2d
TopOpeBRepTool_CurveTool_MakePCurveOnFace = TopOpeBRepTool_CurveTool.MakePCurveOnFace
TopOpeBRepTool_HBoxTool_ComputeBox = TopOpeBRepTool_HBoxTool.ComputeBox
TopOpeBRepTool_HBoxTool_ComputeBoxOnVertices = TopOpeBRepTool_HBoxTool.ComputeBoxOnVertices
TopOpeBRepTool_HBoxTool_DumpB = TopOpeBRepTool_HBoxTool.DumpB
TopOpeBRepTool_REGUS_SplitF = TopOpeBRepTool_REGUS.SplitF
TopOpeBRepTool_REGUS_WireToFace = TopOpeBRepTool_REGUS.WireToFace
TopOpeBRepTool_ShapeTool_AdjustOnPeriodic = TopOpeBRepTool_ShapeTool.AdjustOnPeriodic
TopOpeBRepTool_ShapeTool_BASISCURVE = TopOpeBRepTool_ShapeTool.BASISCURVE
TopOpeBRepTool_ShapeTool_BASISCURVE = TopOpeBRepTool_ShapeTool.BASISCURVE
TopOpeBRepTool_ShapeTool_BASISSURFACE = TopOpeBRepTool_ShapeTool.BASISSURFACE
TopOpeBRepTool_ShapeTool_BASISSURFACE = TopOpeBRepTool_ShapeTool.BASISSURFACE
TopOpeBRepTool_ShapeTool_Closed = TopOpeBRepTool_ShapeTool.Closed
TopOpeBRepTool_ShapeTool_CurvesSameOriented = TopOpeBRepTool_ShapeTool.CurvesSameOriented
TopOpeBRepTool_ShapeTool_EdgeData = TopOpeBRepTool_ShapeTool.EdgeData
TopOpeBRepTool_ShapeTool_EdgeData = TopOpeBRepTool_ShapeTool.EdgeData
TopOpeBRepTool_ShapeTool_EdgesSameOriented = TopOpeBRepTool_ShapeTool.EdgesSameOriented
TopOpeBRepTool_ShapeTool_FacesSameOriented = TopOpeBRepTool_ShapeTool.FacesSameOriented
TopOpeBRepTool_ShapeTool_PeriodizeParameter = TopOpeBRepTool_ShapeTool.PeriodizeParameter
TopOpeBRepTool_ShapeTool_Pnt = TopOpeBRepTool_ShapeTool.Pnt
TopOpeBRepTool_ShapeTool_Resolution3d = TopOpeBRepTool_ShapeTool.Resolution3d
TopOpeBRepTool_ShapeTool_Resolution3d = TopOpeBRepTool_ShapeTool.Resolution3d
TopOpeBRepTool_ShapeTool_Resolution3dU = TopOpeBRepTool_ShapeTool.Resolution3dU
TopOpeBRepTool_ShapeTool_Resolution3dV = TopOpeBRepTool_ShapeTool.Resolution3dV
TopOpeBRepTool_ShapeTool_ShapesSameOriented = TopOpeBRepTool_ShapeTool.ShapesSameOriented
TopOpeBRepTool_ShapeTool_SurfacesSameOriented = TopOpeBRepTool_ShapeTool.SurfacesSameOriented
TopOpeBRepTool_ShapeTool_Tolerance = TopOpeBRepTool_ShapeTool.Tolerance
TopOpeBRepTool_ShapeTool_UVBOUNDS = TopOpeBRepTool_ShapeTool.UVBOUNDS
TopOpeBRepTool_ShapeTool_UVBOUNDS = TopOpeBRepTool_ShapeTool.UVBOUNDS
TopOpeBRepTool_TOOL_ClosedE = TopOpeBRepTool_TOOL.ClosedE
TopOpeBRepTool_TOOL_ClosedS = TopOpeBRepTool_TOOL.ClosedS
TopOpeBRepTool_TOOL_CurvE = TopOpeBRepTool_TOOL.CurvE
TopOpeBRepTool_TOOL_CurvF = TopOpeBRepTool_TOOL.CurvF
TopOpeBRepTool_TOOL_EdgeONFace = TopOpeBRepTool_TOOL.EdgeONFace
TopOpeBRepTool_TOOL_Getduv = TopOpeBRepTool_TOOL.Getduv
TopOpeBRepTool_TOOL_Getstp3dF = TopOpeBRepTool_TOOL.Getstp3dF
TopOpeBRepTool_TOOL_IsClosingE = TopOpeBRepTool_TOOL.IsClosingE
TopOpeBRepTool_TOOL_IsClosingE = TopOpeBRepTool_TOOL.IsClosingE
TopOpeBRepTool_TOOL_IsQuad = TopOpeBRepTool_TOOL.IsQuad
TopOpeBRepTool_TOOL_IsQuad = TopOpeBRepTool_TOOL.IsQuad
TopOpeBRepTool_TOOL_IsonCLO = TopOpeBRepTool_TOOL.IsonCLO
TopOpeBRepTool_TOOL_IsonCLO = TopOpeBRepTool_TOOL.IsonCLO
TopOpeBRepTool_TOOL_Matter = TopOpeBRepTool_TOOL.Matter
TopOpeBRepTool_TOOL_Matter = TopOpeBRepTool_TOOL.Matter
TopOpeBRepTool_TOOL_Matter = TopOpeBRepTool_TOOL.Matter
TopOpeBRepTool_TOOL_Matter = TopOpeBRepTool_TOOL.Matter
TopOpeBRepTool_TOOL_MatterKPtg = TopOpeBRepTool_TOOL.MatterKPtg
TopOpeBRepTool_TOOL_MkShell = TopOpeBRepTool_TOOL.MkShell
TopOpeBRepTool_TOOL_NgApp = TopOpeBRepTool_TOOL.NgApp
TopOpeBRepTool_TOOL_NggeomF = TopOpeBRepTool_TOOL.NggeomF
TopOpeBRepTool_TOOL_Nt = TopOpeBRepTool_TOOL.Nt
TopOpeBRepTool_TOOL_OnBoundary = TopOpeBRepTool_TOOL.OnBoundary
TopOpeBRepTool_TOOL_OriinSor = TopOpeBRepTool_TOOL.OriinSor
TopOpeBRepTool_TOOL_OriinSorclosed = TopOpeBRepTool_TOOL.OriinSorclosed
TopOpeBRepTool_TOOL_ParE = TopOpeBRepTool_TOOL.ParE
TopOpeBRepTool_TOOL_ParE2d = TopOpeBRepTool_TOOL.ParE2d
TopOpeBRepTool_TOOL_ParISO = TopOpeBRepTool_TOOL.ParISO
TopOpeBRepTool_TOOL_Remove = TopOpeBRepTool_TOOL.Remove
TopOpeBRepTool_TOOL_SplitE = TopOpeBRepTool_TOOL.SplitE
TopOpeBRepTool_TOOL_Tg2d = TopOpeBRepTool_TOOL.Tg2d
TopOpeBRepTool_TOOL_Tg2dApp = TopOpeBRepTool_TOOL.Tg2dApp
TopOpeBRepTool_TOOL_TgINSIDE = TopOpeBRepTool_TOOL.TgINSIDE
TopOpeBRepTool_TOOL_TggeomE = TopOpeBRepTool_TOOL.TggeomE
TopOpeBRepTool_TOOL_TggeomE = TopOpeBRepTool_TOOL.TggeomE
TopOpeBRepTool_TOOL_TolP = TopOpeBRepTool_TOOL.TolP
TopOpeBRepTool_TOOL_TolUV = TopOpeBRepTool_TOOL.TolUV
TopOpeBRepTool_TOOL_TrslUV = TopOpeBRepTool_TOOL.TrslUV
TopOpeBRepTool_TOOL_TrslUVModifE = TopOpeBRepTool_TOOL.TrslUVModifE
TopOpeBRepTool_TOOL_UVF = TopOpeBRepTool_TOOL.UVF
TopOpeBRepTool_TOOL_UVISO = TopOpeBRepTool_TOOL.UVISO
TopOpeBRepTool_TOOL_UVISO = TopOpeBRepTool_TOOL.UVISO
TopOpeBRepTool_TOOL_UVISO = TopOpeBRepTool_TOOL.UVISO
TopOpeBRepTool_TOOL_Vertex = TopOpeBRepTool_TOOL.Vertex
TopOpeBRepTool_TOOL_Vertices = TopOpeBRepTool_TOOL.Vertices
TopOpeBRepTool_TOOL_WireToFace = TopOpeBRepTool_TOOL.WireToFace
TopOpeBRepTool_TOOL_XX = TopOpeBRepTool_TOOL.XX
TopOpeBRepTool_TOOL_minDUV = TopOpeBRepTool_TOOL.minDUV
TopOpeBRepTool_TOOL_outUVbounds = TopOpeBRepTool_TOOL.outUVbounds
TopOpeBRepTool_TOOL_stuvF = TopOpeBRepTool_TOOL.stuvF
TopOpeBRepTool_TOOL_tryNgApp = TopOpeBRepTool_TOOL.tryNgApp
TopOpeBRepTool_TOOL_tryOriEinF = TopOpeBRepTool_TOOL.tryOriEinF
TopOpeBRepTool_TOOL_tryTg2dApp = TopOpeBRepTool_TOOL.tryTg2dApp
TopOpeBRepTool_TOOL_uvApp = TopOpeBRepTool_TOOL.uvApp
