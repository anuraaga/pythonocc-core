from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TDataXtd import *
from OCC.Core.AIS import *
from OCC.Core.TCollection import *
from OCC.Core.TDF import *


class TPrsStd_ConstraintTools:
	@staticmethod
	def ComputeAngle(aConst: TDataXtd_Constraint, anAIS: AIS_InteractiveObject) -> None: ...
	@staticmethod
	def ComputeAngleForOneFace(aConst: TDataXtd_Constraint, anAIS: AIS_InteractiveObject) -> None: ...
	@staticmethod
	def ComputeCoincident(aConst: TDataXtd_Constraint, anAIS: AIS_InteractiveObject) -> None: ...
	@staticmethod
	def ComputeConcentric(aConst: TDataXtd_Constraint, anAIS: AIS_InteractiveObject) -> None: ...
	@staticmethod
	def ComputeDiameter(aConst: TDataXtd_Constraint, anAIS: AIS_InteractiveObject) -> None: ...
	@staticmethod
	def ComputeDistance(aConst: TDataXtd_Constraint, anAIS: AIS_InteractiveObject) -> None: ...
	@staticmethod
	def ComputeEqualDistance(aConst: TDataXtd_Constraint, anAIS: AIS_InteractiveObject) -> None: ...
	@staticmethod
	def ComputeEqualRadius(aConst: TDataXtd_Constraint, anAIS: AIS_InteractiveObject) -> None: ...
	@staticmethod
	def ComputeFix(aConst: TDataXtd_Constraint, anAIS: AIS_InteractiveObject) -> None: ...
	@staticmethod
	def ComputeMaxRadius(aConst: TDataXtd_Constraint, anAIS: AIS_InteractiveObject) -> None: ...
	@staticmethod
	def ComputeMidPoint(aConst: TDataXtd_Constraint, anAIS: AIS_InteractiveObject) -> None: ...
	@staticmethod
	def ComputeMinRadius(aConst: TDataXtd_Constraint, anAIS: AIS_InteractiveObject) -> None: ...
	@staticmethod
	def ComputeOffset(aConst: TDataXtd_Constraint, anAIS: AIS_InteractiveObject) -> None: ...
	@staticmethod
	def ComputeOthers(aConst: TDataXtd_Constraint, anAIS: AIS_InteractiveObject) -> None: ...
	@staticmethod
	def ComputeParallel(aConst: TDataXtd_Constraint, anAIS: AIS_InteractiveObject) -> None: ...
	@staticmethod
	def ComputePerpendicular(aConst: TDataXtd_Constraint, anAIS: AIS_InteractiveObject) -> None: ...
	@staticmethod
	def ComputePlacement(aConst: TDataXtd_Constraint, anAIS: AIS_InteractiveObject) -> None: ...
	@staticmethod
	def ComputeRadius(aConst: TDataXtd_Constraint, anAIS: AIS_InteractiveObject) -> None: ...
	@staticmethod
	def ComputeRound(aConst: TDataXtd_Constraint, anAIS: AIS_InteractiveObject) -> None: ...
	@staticmethod
	def ComputeSymmetry(aConst: TDataXtd_Constraint, anAIS: AIS_InteractiveObject) -> None: ...
	@staticmethod
	def ComputeTangent(aConst: TDataXtd_Constraint, anAIS: AIS_InteractiveObject) -> None: ...
	@staticmethod
	def ComputeTextAndValue(aConst: TDataXtd_Constraint, aText: TCollection_ExtendedString, anIsAngle: bool) -> float: ...
	@staticmethod
	def UpdateOnlyValue(aConst: TDataXtd_Constraint, anAIS: AIS_InteractiveObject) -> None: ...

class TPrsStd_Driver(Standard_Transient):
	def Update(self, L: TDF_Label, ais: AIS_InteractiveObject) -> bool: ...

class TPrsStd_DriverTable(Standard_Transient):
	def __init__(self) -> None: ...
	def AddDriver(self, guid: Standard_GUID, driver: TPrsStd_Driver) -> bool: ...
	def Clear(self) -> None: ...
	def FindDriver(self, guid: Standard_GUID, driver: TPrsStd_Driver) -> bool: ...
	@staticmethod
	def Get() -> TPrsStd_DriverTable: ...
	def InitStandardDrivers(self) -> None: ...
	def RemoveDriver(self, guid: Standard_GUID) -> bool: ...

class TPrsStd_AxisDriver(TPrsStd_Driver):
	def __init__(self) -> None: ...
	def Update(self, aLabel: TDF_Label, anAISObject: AIS_InteractiveObject) -> bool: ...

class TPrsStd_ConstraintDriver(TPrsStd_Driver):
	def __init__(self) -> None: ...
	def Update(self, aLabel: TDF_Label, anAISObject: AIS_InteractiveObject) -> bool: ...

class TPrsStd_GeometryDriver(TPrsStd_Driver):
	def __init__(self) -> None: ...
	def Update(self, aLabel: TDF_Label, anAISObject: AIS_InteractiveObject) -> bool: ...

class TPrsStd_NamedShapeDriver(TPrsStd_Driver):
	def __init__(self) -> None: ...
	def Update(self, aLabel: TDF_Label, anAISObject: AIS_InteractiveObject) -> bool: ...

class TPrsStd_PlaneDriver(TPrsStd_Driver):
	def __init__(self) -> None: ...
	def Update(self, aLabel: TDF_Label, anAISObject: AIS_InteractiveObject) -> bool: ...

class TPrsStd_PointDriver(TPrsStd_Driver):
	def __init__(self) -> None: ...
	def Update(self, aLabel: TDF_Label, anAISObject: AIS_InteractiveObject) -> bool: ...

# harray1 classes
# harray2 classes
# hsequence classes

TPrsStd_ConstraintTools_ComputeAngle = TPrsStd_ConstraintTools.ComputeAngle
TPrsStd_ConstraintTools_ComputeAngleForOneFace = TPrsStd_ConstraintTools.ComputeAngleForOneFace
TPrsStd_ConstraintTools_ComputeCoincident = TPrsStd_ConstraintTools.ComputeCoincident
TPrsStd_ConstraintTools_ComputeConcentric = TPrsStd_ConstraintTools.ComputeConcentric
TPrsStd_ConstraintTools_ComputeDiameter = TPrsStd_ConstraintTools.ComputeDiameter
TPrsStd_ConstraintTools_ComputeDistance = TPrsStd_ConstraintTools.ComputeDistance
TPrsStd_ConstraintTools_ComputeEqualDistance = TPrsStd_ConstraintTools.ComputeEqualDistance
TPrsStd_ConstraintTools_ComputeEqualRadius = TPrsStd_ConstraintTools.ComputeEqualRadius
TPrsStd_ConstraintTools_ComputeFix = TPrsStd_ConstraintTools.ComputeFix
TPrsStd_ConstraintTools_ComputeMaxRadius = TPrsStd_ConstraintTools.ComputeMaxRadius
TPrsStd_ConstraintTools_ComputeMidPoint = TPrsStd_ConstraintTools.ComputeMidPoint
TPrsStd_ConstraintTools_ComputeMinRadius = TPrsStd_ConstraintTools.ComputeMinRadius
TPrsStd_ConstraintTools_ComputeOffset = TPrsStd_ConstraintTools.ComputeOffset
TPrsStd_ConstraintTools_ComputeOthers = TPrsStd_ConstraintTools.ComputeOthers
TPrsStd_ConstraintTools_ComputeParallel = TPrsStd_ConstraintTools.ComputeParallel
TPrsStd_ConstraintTools_ComputePerpendicular = TPrsStd_ConstraintTools.ComputePerpendicular
TPrsStd_ConstraintTools_ComputePlacement = TPrsStd_ConstraintTools.ComputePlacement
TPrsStd_ConstraintTools_ComputeRadius = TPrsStd_ConstraintTools.ComputeRadius
TPrsStd_ConstraintTools_ComputeRound = TPrsStd_ConstraintTools.ComputeRound
TPrsStd_ConstraintTools_ComputeSymmetry = TPrsStd_ConstraintTools.ComputeSymmetry
TPrsStd_ConstraintTools_ComputeTangent = TPrsStd_ConstraintTools.ComputeTangent
TPrsStd_ConstraintTools_ComputeTextAndValue = TPrsStd_ConstraintTools.ComputeTextAndValue
TPrsStd_ConstraintTools_UpdateOnlyValue = TPrsStd_ConstraintTools.UpdateOnlyValue
TPrsStd_DriverTable_Get = TPrsStd_DriverTable.Get
