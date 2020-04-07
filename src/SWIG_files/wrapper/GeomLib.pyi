from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.Geom import *
from OCC.Core.gp import *
from OCC.Core.TColgp import *
from OCC.Core.Adaptor3d import *
from OCC.Core.GeomAbs import *
from OCC.Core.TColStd import *
from OCC.Core.Geom2d import *
from OCC.Core.math import *
from OCC.Core.AdvApprox import *

GeomLib_DenominatorMultiplierPtr = NewType('GeomLib_DenominatorMultiplierPtr', GeomLib_DenominatorMultiplier)

class GeomLib_Array1OfMat:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, theLower: int, theUpper: int) -> None: ...
    def __getitem__(self, index: int) -> gp_Mat: ...
    def __setitem__(self, index: int, value: gp_Mat) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[gp_Mat]: ...
    def next(self) -> gp_Mat: ...
    __next__ = next
    def Init(self, theValue: gp_Mat) -> None: ...
    def Size(self) -> int: ...
    def Length(self) -> int: ...
    def IsEmpty(self) -> bool: ...
    def Lower(self) -> int: ...
    def Upper(self) -> int: ...
    def IsDetectable(self) -> bool: ...
    def IsAllocated(self) -> bool: ...
    def First(self) -> gp_Mat: ...
    def Last(self) -> gp_Mat: ...
    def Value(self, theIndex: int) -> gp_Mat: ...
    def SetValue(self, theIndex: int, theValue: gp_Mat) -> None: ...

class GeomLib_InterpolationErrors(IntEnum):
	GeomLib_NoError: int = ...
	GeomLib_NotEnoughtPoints: int = ...
	GeomLib_DegreeSmallerThan3: int = ...
	GeomLib_InversionProblem: int = ...
GeomLib_NoError = GeomLib_InterpolationErrors.GeomLib_NoError
GeomLib_NotEnoughtPoints = GeomLib_InterpolationErrors.GeomLib_NotEnoughtPoints
GeomLib_DegreeSmallerThan3 = GeomLib_InterpolationErrors.GeomLib_DegreeSmallerThan3
GeomLib_InversionProblem = GeomLib_InterpolationErrors.GeomLib_InversionProblem

class geomlib:
	@staticmethod
	def AdjustExtremity(Curve: Geom_BoundedCurve, P1: gp_Pnt, P2: gp_Pnt, T1: gp_Vec, T2: gp_Vec) -> None: ...
	@staticmethod
	def AxeOfInertia(Points: TColgp_Array1OfPnt, Axe: gp_Ax2, Tol: Optional[float] = 1.0e-7) -> bool: ...
	@staticmethod
	def BuildCurve3d(Tolerance: float, CurvePtr: Adaptor3d_CurveOnSurface, FirstParameter: float, LastParameter: float, NewCurvePtr: Geom_Curve, Continuity: Optional[GeomAbs_Shape] = GeomAbs_C1, MaxDegree: Optional[int] = 14, MaxSegment: Optional[int] = 30) -> Tuple[float, float]: ...
	@staticmethod
	def CancelDenominatorDerivative(BSurf: Geom_BSplineSurface, UDirection: bool, VDirection: bool) -> None: ...
	@staticmethod
	def DensifyArray1OfReal(MinNumPoints: int, InParameters: TColStd_Array1OfReal, OutParameters: TColStd_HArray1OfReal) -> None: ...
	@staticmethod
	def EvalMaxDistanceAlongParameter(Curve: Adaptor3d_Curve, AReferenceCurve: Adaptor3d_Curve, Tolerance: float, Parameters: TColStd_Array1OfReal) -> float: ...
	@staticmethod
	def EvalMaxParametricDistance(Curve: Adaptor3d_Curve, AReferenceCurve: Adaptor3d_Curve, Tolerance: float, Parameters: TColStd_Array1OfReal) -> float: ...
	@staticmethod
	def ExtendCurveToPoint(Curve: Geom_BoundedCurve, Point: gp_Pnt, Cont: int, After: bool) -> None: ...
	@staticmethod
	def ExtendSurfByLength(Surf: Geom_BoundedSurface, Length: float, Cont: int, InU: bool, After: bool) -> None: ...
	@staticmethod
	def FuseIntervals(Interval1: TColStd_Array1OfReal, Interval2: TColStd_Array1OfReal, Fusion: TColStd_SequenceOfReal, Confusion: Optional[float] = 1.0e-9) -> None: ...
	@staticmethod
	def GTransform(Curve: Geom2d_Curve, GTrsf: gp_GTrsf2d) -> Geom2d_Curve: ...
	@staticmethod
	def Inertia(Points: TColgp_Array1OfPnt, Bary: gp_Pnt, XDir: gp_Dir, YDir: gp_Dir) -> Tuple[float, float, float]: ...
	@staticmethod
	def IsBSplUClosed(S: Geom_BSplineSurface, U1: float, U2: float, Tol: float) -> bool: ...
	@staticmethod
	def IsBSplVClosed(S: Geom_BSplineSurface, V1: float, V2: float, Tol: float) -> bool: ...
	@staticmethod
	def IsBzUClosed(S: Geom_BezierSurface, U1: float, U2: float, Tol: float) -> bool: ...
	@staticmethod
	def IsBzVClosed(S: Geom_BezierSurface, V1: float, V2: float, Tol: float) -> bool: ...
	@staticmethod
	def IsClosed(S: Geom_Surface, Tol: float) -> Tuple[bool, bool]: ...
	@staticmethod
	def NormEstim(S: Geom_Surface, UV: gp_Pnt2d, Tol: float, N: gp_Dir) -> int: ...
	@staticmethod
	def RemovePointsFromArray(NumPoints: int, InParameters: TColStd_Array1OfReal, OutParameters: TColStd_HArray1OfReal) -> None: ...
	@staticmethod
	def SameRange(Tolerance: float, Curve2dPtr: Geom2d_Curve, First: float, Last: float, RequestedFirst: float, RequestedLast: float, NewCurve2dPtr: Geom2d_Curve) -> None: ...
	@staticmethod
	def To3d(Position: gp_Ax2, Curve2d: Geom2d_Curve) -> Geom_Curve: ...

class GeomLib_Check2dBSplineCurve:
	def __init__(self, Curve: Geom2d_BSplineCurve, Tolerance: float, AngularTolerance: float) -> None: ...
	def FixTangent(self, FirstFlag: bool, LastFlag: bool) -> None: ...
	def FixedTangent(self, FirstFlag: bool, LastFlag: bool) -> Geom2d_BSplineCurve: ...
	def IsDone(self) -> bool: ...
	def NeedTangentFix(self) -> Tuple[bool, bool]: ...

class GeomLib_CheckBSplineCurve:
	def __init__(self, Curve: Geom_BSplineCurve, Tolerance: float, AngularTolerance: float) -> None: ...
	def FixTangent(self, FirstFlag: bool, LastFlag: bool) -> None: ...
	def FixedTangent(self, FirstFlag: bool, LastFlag: bool) -> Geom_BSplineCurve: ...
	def IsDone(self) -> bool: ...
	def NeedTangentFix(self) -> Tuple[bool, bool]: ...

class GeomLib_CheckCurveOnSurface:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theCurve: Geom_Curve, theSurface: Geom_Surface, theFirst: float, theLast: float, theTolRange: Optional[float] = precision_PConfusion()) -> None: ...
	def Curve(self) -> Geom_Curve: ...
	def ErrorStatus(self) -> int: ...
	@overload
	def Init(self, theCurve: Geom_Curve, theSurface: Geom_Surface, theFirst: float, theLast: float, theTolRange: Optional[float] = precision_PConfusion()) -> None: ...
	@overload
	def Init(self) -> None: ...
	def IsDone(self) -> bool: ...
	def MaxDistance(self) -> float: ...
	def MaxParameter(self) -> float: ...
	def Perform(self, thePCurve: Geom2d_Curve, isTheMultyTheradDisabled: Optional[bool] = False) -> None: ...
	def Range(self) -> Tuple[float, float]: ...
	def Surface(self) -> Geom_Surface: ...

class GeomLib_DenominatorMultiplier:
	def __init__(self, Surface: Geom_BSplineSurface, KnotVector: TColStd_Array1OfReal) -> None: ...
	def Value(self, UParameter: float, VParameter: float) -> float: ...

class GeomLib_Interpolate:
	def __init__(self, Degree: int, NumPoints: int, Points: TColgp_Array1OfPnt, Parameters: TColStd_Array1OfReal) -> None: ...
	def Curve(self) -> Geom_BSplineCurve: ...
	def Error(self) -> GeomLib_InterpolationErrors: ...
	def IsDone(self) -> bool: ...

class GeomLib_IsPlanarSurface:
	def __init__(self, S: Geom_Surface, Tol: Optional[float] = 1.0e-7) -> None: ...
	def IsPlanar(self) -> bool: ...
	def Plan(self) -> gp_Pln: ...

class GeomLib_LogSample(math_FunctionSample):
	def __init__(self, A: float, B: float, N: int) -> None: ...
	def GetParameter(self, Index: int) -> float: ...

class GeomLib_MakeCurvefromApprox:
	def __init__(self, Approx: AdvApprox_ApproxAFunction) -> None: ...
	@overload
	def Curve(self, Index3d: int) -> Geom_BSplineCurve: ...
	@overload
	def Curve(self, Index1D: int, Index3D: int) -> Geom_BSplineCurve: ...
	@overload
	def Curve2d(self, Index2d: int) -> Geom2d_BSplineCurve: ...
	@overload
	def Curve2d(self, Index1d: int, Index2d: int) -> Geom2d_BSplineCurve: ...
	def Curve2dFromTwo1d(self, Index1d: int, Index2d: int) -> Geom2d_BSplineCurve: ...
	def IsDone(self) -> bool: ...
	def Nb1DSpaces(self) -> int: ...
	def Nb2DSpaces(self) -> int: ...
	def Nb3DSpaces(self) -> int: ...

class GeomLib_PolyFunc(math_FunctionWithDerivative):
	def __init__(self, Coeffs: math_Vector) -> None: ...
	def Derivative(self, X: float) -> Tuple[bool, float]: ...
	def Value(self, X: float) -> Tuple[bool, float]: ...
	def Values(self, X: float) -> Tuple[bool, float, float]: ...

class GeomLib_Tool:
	@overload
	@staticmethod
	def Parameter(Curve: Geom_Curve, Point: gp_Pnt, MaxDist: float) -> Tuple[bool, float]: ...
	@overload
	@staticmethod
	def Parameter(Curve: Geom2d_Curve, Point: gp_Pnt2d, MaxDist: float) -> Tuple[bool, float]: ...
	@staticmethod
	def Parameters(Surface: Geom_Surface, Point: gp_Pnt, MaxDist: float) -> Tuple[bool, float, float]: ...

# harray1 classes
# harray2 classes
# hsequence classes

geomlib_AdjustExtremity = geomlib.AdjustExtremity
geomlib_AxeOfInertia = geomlib.AxeOfInertia
geomlib_BuildCurve3d = geomlib.BuildCurve3d
geomlib_CancelDenominatorDerivative = geomlib.CancelDenominatorDerivative
geomlib_DensifyArray1OfReal = geomlib.DensifyArray1OfReal
geomlib_EvalMaxDistanceAlongParameter = geomlib.EvalMaxDistanceAlongParameter
geomlib_EvalMaxParametricDistance = geomlib.EvalMaxParametricDistance
geomlib_ExtendCurveToPoint = geomlib.ExtendCurveToPoint
geomlib_ExtendSurfByLength = geomlib.ExtendSurfByLength
geomlib_FuseIntervals = geomlib.FuseIntervals
geomlib_GTransform = geomlib.GTransform
geomlib_Inertia = geomlib.Inertia
geomlib_IsBSplUClosed = geomlib.IsBSplUClosed
geomlib_IsBSplVClosed = geomlib.IsBSplVClosed
geomlib_IsBzUClosed = geomlib.IsBzUClosed
geomlib_IsBzVClosed = geomlib.IsBzVClosed
geomlib_IsClosed = geomlib.IsClosed
geomlib_NormEstim = geomlib.NormEstim
geomlib_RemovePointsFromArray = geomlib.RemovePointsFromArray
geomlib_SameRange = geomlib.SameRange
geomlib_To3d = geomlib.To3d
GeomLib_Tool_Parameter = GeomLib_Tool.Parameter
GeomLib_Tool_Parameter = GeomLib_Tool.Parameter
GeomLib_Tool_Parameters = GeomLib_Tool.Parameters
