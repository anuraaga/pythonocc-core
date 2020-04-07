from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TCollection import *
from OCC.Core.StepData import *
from OCC.Core.StepBasic import *

#the following typedef cannot be wrapped as is
StepRepr_SequenceOfMaterialPropertyRepresentation = NewType('StepRepr_SequenceOfMaterialPropertyRepresentation', Any)
#the following typedef cannot be wrapped as is
StepRepr_SequenceOfRepresentationItem = NewType('StepRepr_SequenceOfRepresentationItem', Any)

class StepRepr_Array1OfMaterialPropertyRepresentation:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, theLower: int, theUpper: int) -> None: ...
    def __getitem__(self, index: int) -> False: ...
    def __setitem__(self, index: int, value: False) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[False]: ...
    def next(self) -> False: ...
    __next__ = next
    def Init(self, theValue: False) -> None: ...
    def Size(self) -> int: ...
    def Length(self) -> int: ...
    def IsEmpty(self) -> bool: ...
    def Lower(self) -> int: ...
    def Upper(self) -> int: ...
    def IsDetectable(self) -> bool: ...
    def IsAllocated(self) -> bool: ...
    def First(self) -> False: ...
    def Last(self) -> False: ...
    def Value(self, theIndex: int) -> False: ...
    def SetValue(self, theIndex: int, theValue: False) -> None: ...

class StepRepr_Array1OfPropertyDefinitionRepresentation:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, theLower: int, theUpper: int) -> None: ...
    def __getitem__(self, index: int) -> False: ...
    def __setitem__(self, index: int, value: False) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[False]: ...
    def next(self) -> False: ...
    __next__ = next
    def Init(self, theValue: False) -> None: ...
    def Size(self) -> int: ...
    def Length(self) -> int: ...
    def IsEmpty(self) -> bool: ...
    def Lower(self) -> int: ...
    def Upper(self) -> int: ...
    def IsDetectable(self) -> bool: ...
    def IsAllocated(self) -> bool: ...
    def First(self) -> False: ...
    def Last(self) -> False: ...
    def Value(self, theIndex: int) -> False: ...
    def SetValue(self, theIndex: int, theValue: False) -> None: ...

class StepRepr_Array1OfRepresentationItem:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, theLower: int, theUpper: int) -> None: ...
    def __getitem__(self, index: int) -> False: ...
    def __setitem__(self, index: int, value: False) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[False]: ...
    def next(self) -> False: ...
    __next__ = next
    def Init(self, theValue: False) -> None: ...
    def Size(self) -> int: ...
    def Length(self) -> int: ...
    def IsEmpty(self) -> bool: ...
    def Lower(self) -> int: ...
    def Upper(self) -> int: ...
    def IsDetectable(self) -> bool: ...
    def IsAllocated(self) -> bool: ...
    def First(self) -> False: ...
    def Last(self) -> False: ...
    def Value(self, theIndex: int) -> False: ...
    def SetValue(self, theIndex: int, theValue: False) -> None: ...

class StepRepr_Array1OfShapeAspect:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, theLower: int, theUpper: int) -> None: ...
    def __getitem__(self, index: int) -> False: ...
    def __setitem__(self, index: int, value: False) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[False]: ...
    def next(self) -> False: ...
    __next__ = next
    def Init(self, theValue: False) -> None: ...
    def Size(self) -> int: ...
    def Length(self) -> int: ...
    def IsEmpty(self) -> bool: ...
    def Lower(self) -> int: ...
    def Upper(self) -> int: ...
    def IsDetectable(self) -> bool: ...
    def IsAllocated(self) -> bool: ...
    def First(self) -> False: ...
    def Last(self) -> False: ...
    def Value(self, theIndex: int) -> False: ...
    def SetValue(self, theIndex: int, theValue: False) -> None: ...

class StepRepr_AssemblyComponentUsageSubstitute(Standard_Transient):
	def __init__(self) -> None: ...
	def Base(self) -> StepRepr_AssemblyComponentUsage: ...
	def Definition(self) -> TCollection_HAsciiString: ...
	def Init(self, aName: TCollection_HAsciiString, aDef: TCollection_HAsciiString, aBase: StepRepr_AssemblyComponentUsage, aSubs: StepRepr_AssemblyComponentUsage) -> None: ...
	def Name(self) -> TCollection_HAsciiString: ...
	def SetBase(self, aBase: StepRepr_AssemblyComponentUsage) -> None: ...
	def SetDefinition(self, aDef: TCollection_HAsciiString) -> None: ...
	def SetName(self, aName: TCollection_HAsciiString) -> None: ...
	def SetSubstitute(self, aSubstitute: StepRepr_AssemblyComponentUsage) -> None: ...
	def Substitute(self) -> StepRepr_AssemblyComponentUsage: ...

class StepRepr_CharacterizedDefinition(StepData_SelectType):
	def __init__(self) -> None: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def CharacterizedObject(self) -> StepBasic_CharacterizedObject: ...
	def DocumentFile(self) -> StepBasic_DocumentFile: ...
	def ProductDefinition(self) -> StepBasic_ProductDefinition: ...
	def ProductDefinitionRelationship(self) -> StepBasic_ProductDefinitionRelationship: ...
	def ProductDefinitionShape(self) -> StepRepr_ProductDefinitionShape: ...
	def ShapeAspect(self) -> StepRepr_ShapeAspect: ...
	def ShapeAspectRelationship(self) -> StepRepr_ShapeAspectRelationship: ...

class StepRepr_ConfigurationDesign(Standard_Transient):
	def __init__(self) -> None: ...
	def Configuration(self) -> StepRepr_ConfigurationItem: ...
	def Design(self) -> StepRepr_ConfigurationDesignItem: ...
	def Init(self, aConfiguration: StepRepr_ConfigurationItem, aDesign: StepRepr_ConfigurationDesignItem) -> None: ...
	def SetConfiguration(self, Configuration: StepRepr_ConfigurationItem) -> None: ...
	def SetDesign(self, Design: StepRepr_ConfigurationDesignItem) -> None: ...

class StepRepr_ConfigurationDesignItem(StepData_SelectType):
	def __init__(self) -> None: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def ProductDefinition(self) -> StepBasic_ProductDefinition: ...
	def ProductDefinitionFormation(self) -> StepBasic_ProductDefinitionFormation: ...

class StepRepr_ConfigurationEffectivity(StepBasic_ProductDefinitionEffectivity):
	def __init__(self) -> None: ...
	def Configuration(self) -> StepRepr_ConfigurationDesign: ...
	def Init(self, aEffectivity_Id: TCollection_HAsciiString, aProductDefinitionEffectivity_Usage: StepBasic_ProductDefinitionRelationship, aConfiguration: StepRepr_ConfigurationDesign) -> None: ...
	def SetConfiguration(self, Configuration: StepRepr_ConfigurationDesign) -> None: ...

class StepRepr_ConfigurationItem(Standard_Transient):
	def __init__(self) -> None: ...
	def Description(self) -> TCollection_HAsciiString: ...
	def HasDescription(self) -> bool: ...
	def HasPurpose(self) -> bool: ...
	def Id(self) -> TCollection_HAsciiString: ...
	def Init(self, aId: TCollection_HAsciiString, aName: TCollection_HAsciiString, hasDescription: bool, aDescription: TCollection_HAsciiString, aItemConcept: StepRepr_ProductConcept, hasPurpose: bool, aPurpose: TCollection_HAsciiString) -> None: ...
	def ItemConcept(self) -> StepRepr_ProductConcept: ...
	def Name(self) -> TCollection_HAsciiString: ...
	def Purpose(self) -> TCollection_HAsciiString: ...
	def SetDescription(self, Description: TCollection_HAsciiString) -> None: ...
	def SetId(self, Id: TCollection_HAsciiString) -> None: ...
	def SetItemConcept(self, ItemConcept: StepRepr_ProductConcept) -> None: ...
	def SetName(self, Name: TCollection_HAsciiString) -> None: ...
	def SetPurpose(self, Purpose: TCollection_HAsciiString) -> None: ...

class StepRepr_DataEnvironment(Standard_Transient):
	def __init__(self) -> None: ...
	def Description(self) -> TCollection_HAsciiString: ...
	def Elements(self) -> StepRepr_HArray1OfPropertyDefinitionRepresentation: ...
	def Init(self, aName: TCollection_HAsciiString, aDescription: TCollection_HAsciiString, aElements: StepRepr_HArray1OfPropertyDefinitionRepresentation) -> None: ...
	def Name(self) -> TCollection_HAsciiString: ...
	def SetDescription(self, Description: TCollection_HAsciiString) -> None: ...
	def SetElements(self, Elements: StepRepr_HArray1OfPropertyDefinitionRepresentation) -> None: ...
	def SetName(self, Name: TCollection_HAsciiString) -> None: ...

class StepRepr_FunctionallyDefinedTransformation(Standard_Transient):
	def __init__(self) -> None: ...
	def Description(self) -> TCollection_HAsciiString: ...
	def Init(self, aName: TCollection_HAsciiString, aDescription: TCollection_HAsciiString) -> None: ...
	def Name(self) -> TCollection_HAsciiString: ...
	def SetDescription(self, aDescription: TCollection_HAsciiString) -> None: ...
	def SetName(self, aName: TCollection_HAsciiString) -> None: ...

class StepRepr_ItemDefinedTransformation(Standard_Transient):
	def __init__(self) -> None: ...
	def Description(self) -> TCollection_HAsciiString: ...
	def Init(self, aName: TCollection_HAsciiString, aDescription: TCollection_HAsciiString, aTransformItem1: StepRepr_RepresentationItem, aTransformItem2: StepRepr_RepresentationItem) -> None: ...
	def Name(self) -> TCollection_HAsciiString: ...
	def SetDescription(self, aDescription: TCollection_HAsciiString) -> None: ...
	def SetName(self, aName: TCollection_HAsciiString) -> None: ...
	def SetTransformItem1(self, aItem: StepRepr_RepresentationItem) -> None: ...
	def SetTransformItem2(self, aItem: StepRepr_RepresentationItem) -> None: ...
	def TransformItem1(self) -> StepRepr_RepresentationItem: ...
	def TransformItem2(self) -> StepRepr_RepresentationItem: ...

class StepRepr_MaterialDesignation(Standard_Transient):
	def __init__(self) -> None: ...
	def Init(self, aName: TCollection_HAsciiString, aOfDefinition: StepRepr_CharacterizedDefinition) -> None: ...
	def Name(self) -> TCollection_HAsciiString: ...
	def OfDefinition(self) -> StepRepr_CharacterizedDefinition: ...
	def SetName(self, aName: TCollection_HAsciiString) -> None: ...
	def SetOfDefinition(self, aOfDefinition: StepRepr_CharacterizedDefinition) -> None: ...

class StepRepr_ProductConcept(Standard_Transient):
	def __init__(self) -> None: ...
	def Description(self) -> TCollection_HAsciiString: ...
	def HasDescription(self) -> bool: ...
	def Id(self) -> TCollection_HAsciiString: ...
	def Init(self, aId: TCollection_HAsciiString, aName: TCollection_HAsciiString, hasDescription: bool, aDescription: TCollection_HAsciiString, aMarketContext: StepBasic_ProductConceptContext) -> None: ...
	def MarketContext(self) -> StepBasic_ProductConceptContext: ...
	def Name(self) -> TCollection_HAsciiString: ...
	def SetDescription(self, Description: TCollection_HAsciiString) -> None: ...
	def SetId(self, Id: TCollection_HAsciiString) -> None: ...
	def SetMarketContext(self, MarketContext: StepBasic_ProductConceptContext) -> None: ...
	def SetName(self, Name: TCollection_HAsciiString) -> None: ...

class StepRepr_ProductDefinitionUsage(StepBasic_ProductDefinitionRelationship):
	def __init__(self) -> None: ...

class StepRepr_PropertyDefinition(Standard_Transient):
	def __init__(self) -> None: ...
	def Definition(self) -> StepRepr_CharacterizedDefinition: ...
	def Description(self) -> TCollection_HAsciiString: ...
	def HasDescription(self) -> bool: ...
	def Init(self, aName: TCollection_HAsciiString, hasDescription: bool, aDescription: TCollection_HAsciiString, aDefinition: StepRepr_CharacterizedDefinition) -> None: ...
	def Name(self) -> TCollection_HAsciiString: ...
	def SetDefinition(self, Definition: StepRepr_CharacterizedDefinition) -> None: ...
	def SetDescription(self, Description: TCollection_HAsciiString) -> None: ...
	def SetName(self, Name: TCollection_HAsciiString) -> None: ...

class StepRepr_PropertyDefinitionRelationship(Standard_Transient):
	def __init__(self) -> None: ...
	def Description(self) -> TCollection_HAsciiString: ...
	def Init(self, aName: TCollection_HAsciiString, aDescription: TCollection_HAsciiString, aRelatingPropertyDefinition: StepRepr_PropertyDefinition, aRelatedPropertyDefinition: StepRepr_PropertyDefinition) -> None: ...
	def Name(self) -> TCollection_HAsciiString: ...
	def RelatedPropertyDefinition(self) -> StepRepr_PropertyDefinition: ...
	def RelatingPropertyDefinition(self) -> StepRepr_PropertyDefinition: ...
	def SetDescription(self, Description: TCollection_HAsciiString) -> None: ...
	def SetName(self, Name: TCollection_HAsciiString) -> None: ...
	def SetRelatedPropertyDefinition(self, RelatedPropertyDefinition: StepRepr_PropertyDefinition) -> None: ...
	def SetRelatingPropertyDefinition(self, RelatingPropertyDefinition: StepRepr_PropertyDefinition) -> None: ...

class StepRepr_PropertyDefinitionRepresentation(Standard_Transient):
	def __init__(self) -> None: ...
	def Definition(self) -> StepRepr_RepresentedDefinition: ...
	def Init(self, aDefinition: StepRepr_RepresentedDefinition, aUsedRepresentation: StepRepr_Representation) -> None: ...
	def SetDefinition(self, Definition: StepRepr_RepresentedDefinition) -> None: ...
	def SetUsedRepresentation(self, UsedRepresentation: StepRepr_Representation) -> None: ...
	def UsedRepresentation(self) -> StepRepr_Representation: ...

class StepRepr_Representation(Standard_Transient):
	def __init__(self) -> None: ...
	def ContextOfItems(self) -> StepRepr_RepresentationContext: ...
	def Init(self, aName: TCollection_HAsciiString, aItems: StepRepr_HArray1OfRepresentationItem, aContextOfItems: StepRepr_RepresentationContext) -> None: ...
	def Items(self) -> StepRepr_HArray1OfRepresentationItem: ...
	def ItemsValue(self, num: int) -> StepRepr_RepresentationItem: ...
	def Name(self) -> TCollection_HAsciiString: ...
	def NbItems(self) -> int: ...
	def SetContextOfItems(self, aContextOfItems: StepRepr_RepresentationContext) -> None: ...
	def SetItems(self, aItems: StepRepr_HArray1OfRepresentationItem) -> None: ...
	def SetName(self, aName: TCollection_HAsciiString) -> None: ...

class StepRepr_RepresentationContext(Standard_Transient):
	def __init__(self) -> None: ...
	def ContextIdentifier(self) -> TCollection_HAsciiString: ...
	def ContextType(self) -> TCollection_HAsciiString: ...
	def Init(self, aContextIdentifier: TCollection_HAsciiString, aContextType: TCollection_HAsciiString) -> None: ...
	def SetContextIdentifier(self, aContextIdentifier: TCollection_HAsciiString) -> None: ...
	def SetContextType(self, aContextType: TCollection_HAsciiString) -> None: ...

class StepRepr_RepresentationItem(Standard_Transient):
	def __init__(self) -> None: ...
	def Init(self, aName: TCollection_HAsciiString) -> None: ...
	def Name(self) -> TCollection_HAsciiString: ...
	def SetName(self, aName: TCollection_HAsciiString) -> None: ...

class StepRepr_RepresentationMap(Standard_Transient):
	def __init__(self) -> None: ...
	def Init(self, aMappingOrigin: StepRepr_RepresentationItem, aMappedRepresentation: StepRepr_Representation) -> None: ...
	def MappedRepresentation(self) -> StepRepr_Representation: ...
	def MappingOrigin(self) -> StepRepr_RepresentationItem: ...
	def SetMappedRepresentation(self, aMappedRepresentation: StepRepr_Representation) -> None: ...
	def SetMappingOrigin(self, aMappingOrigin: StepRepr_RepresentationItem) -> None: ...

class StepRepr_RepresentationRelationship(Standard_Transient):
	def __init__(self) -> None: ...
	def Description(self) -> TCollection_HAsciiString: ...
	def Init(self, aName: TCollection_HAsciiString, aDescription: TCollection_HAsciiString, aRep1: StepRepr_Representation, aRep2: StepRepr_Representation) -> None: ...
	def Name(self) -> TCollection_HAsciiString: ...
	def Rep1(self) -> StepRepr_Representation: ...
	def Rep2(self) -> StepRepr_Representation: ...
	def SetDescription(self, aDescription: TCollection_HAsciiString) -> None: ...
	def SetName(self, aName: TCollection_HAsciiString) -> None: ...
	def SetRep1(self, aRep1: StepRepr_Representation) -> None: ...
	def SetRep2(self, aRep2: StepRepr_Representation) -> None: ...

class StepRepr_RepresentedDefinition(StepData_SelectType):
	def __init__(self) -> None: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def GeneralProperty(self) -> StepBasic_GeneralProperty: ...
	def PropertyDefinition(self) -> StepRepr_PropertyDefinition: ...
	def PropertyDefinitionRelationship(self) -> StepRepr_PropertyDefinitionRelationship: ...
	def ShapeAspect(self) -> StepRepr_ShapeAspect: ...
	def ShapeAspectRelationship(self) -> StepRepr_ShapeAspectRelationship: ...

class StepRepr_ShapeAspect(Standard_Transient):
	def __init__(self) -> None: ...
	def Description(self) -> TCollection_HAsciiString: ...
	def Init(self, aName: TCollection_HAsciiString, aDescription: TCollection_HAsciiString, aOfShape: StepRepr_ProductDefinitionShape, aProductDefinitional: StepData_Logical) -> None: ...
	def Name(self) -> TCollection_HAsciiString: ...
	def OfShape(self) -> StepRepr_ProductDefinitionShape: ...
	def ProductDefinitional(self) -> StepData_Logical: ...
	def SetDescription(self, aDescription: TCollection_HAsciiString) -> None: ...
	def SetName(self, aName: TCollection_HAsciiString) -> None: ...
	def SetOfShape(self, aOfShape: StepRepr_ProductDefinitionShape) -> None: ...
	def SetProductDefinitional(self, aProductDefinitional: StepData_Logical) -> None: ...

class StepRepr_ShapeAspectRelationship(Standard_Transient):
	def __init__(self) -> None: ...
	def Description(self) -> TCollection_HAsciiString: ...
	def HasDescription(self) -> bool: ...
	def Init(self, aName: TCollection_HAsciiString, hasDescription: bool, aDescription: TCollection_HAsciiString, aRelatingShapeAspect: StepRepr_ShapeAspect, aRelatedShapeAspect: StepRepr_ShapeAspect) -> None: ...
	def Name(self) -> TCollection_HAsciiString: ...
	def RelatedShapeAspect(self) -> StepRepr_ShapeAspect: ...
	def RelatingShapeAspect(self) -> StepRepr_ShapeAspect: ...
	def SetDescription(self, Description: TCollection_HAsciiString) -> None: ...
	def SetName(self, Name: TCollection_HAsciiString) -> None: ...
	def SetRelatedShapeAspect(self, RelatedShapeAspect: StepRepr_ShapeAspect) -> None: ...
	def SetRelatingShapeAspect(self, RelatingShapeAspect: StepRepr_ShapeAspect) -> None: ...

class StepRepr_ShapeDefinition(StepData_SelectType):
	def __init__(self) -> None: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def ProductDefinitionShape(self) -> StepRepr_ProductDefinitionShape: ...
	def ShapeAspect(self) -> StepRepr_ShapeAspect: ...
	def ShapeAspectRelationship(self) -> StepRepr_ShapeAspectRelationship: ...

class StepRepr_SuppliedPartRelationship(StepBasic_ProductDefinitionRelationship):
	def __init__(self) -> None: ...

class StepRepr_Transformation(StepData_SelectType):
	def __init__(self) -> None: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def FunctionallyDefinedTransformation(self) -> StepRepr_FunctionallyDefinedTransformation: ...
	def ItemDefinedTransformation(self) -> StepRepr_ItemDefinedTransformation: ...

class StepRepr_AssemblyComponentUsage(StepRepr_ProductDefinitionUsage):
	def __init__(self) -> None: ...
	def HasReferenceDesignator(self) -> bool: ...
	@overload
	def Init(self, aProductDefinitionRelationship_Id: TCollection_HAsciiString, aProductDefinitionRelationship_Name: TCollection_HAsciiString, hasProductDefinitionRelationship_Description: bool, aProductDefinitionRelationship_Description: TCollection_HAsciiString, aProductDefinitionRelationship_RelatingProductDefinition: StepBasic_ProductDefinition, aProductDefinitionRelationship_RelatedProductDefinition: StepBasic_ProductDefinition, hasReferenceDesignator: bool, aReferenceDesignator: TCollection_HAsciiString) -> None: ...
	@overload
	def Init(self, aProductDefinitionRelationship_Id: TCollection_HAsciiString, aProductDefinitionRelationship_Name: TCollection_HAsciiString, hasProductDefinitionRelationship_Description: bool, aProductDefinitionRelationship_Description: TCollection_HAsciiString, aProductDefinitionRelationship_RelatingProductDefinition: StepBasic_ProductDefinitionOrReference, aProductDefinitionRelationship_RelatedProductDefinition: StepBasic_ProductDefinitionOrReference, hasReferenceDesignator: bool, aReferenceDesignator: TCollection_HAsciiString) -> None: ...
	def ReferenceDesignator(self) -> TCollection_HAsciiString: ...
	def SetReferenceDesignator(self, ReferenceDesignator: TCollection_HAsciiString) -> None: ...

class StepRepr_CharacterizedRepresentation(StepRepr_Representation):
	def __init__(self) -> None: ...
	def Description(self) -> TCollection_HAsciiString: ...
	def Init(self, theName: TCollection_HAsciiString, theDescription: TCollection_HAsciiString, theItems: StepRepr_HArray1OfRepresentationItem, theContextOfItems: StepRepr_RepresentationContext) -> None: ...
	def SetDescription(self, theDescription: TCollection_HAsciiString) -> None: ...

class StepRepr_CompShAspAndDatumFeatAndShAsp(StepRepr_ShapeAspect):
	def __init__(self) -> None: ...

class StepRepr_CompositeShapeAspect(StepRepr_ShapeAspect):
	def __init__(self) -> None: ...

class StepRepr_CompoundRepresentationItem(StepRepr_RepresentationItem):
	def __init__(self) -> None: ...
	def Init(self, aName: TCollection_HAsciiString, item_element: StepRepr_HArray1OfRepresentationItem) -> None: ...
	def ItemElement(self) -> StepRepr_HArray1OfRepresentationItem: ...
	def ItemElementValue(self, num: int) -> StepRepr_RepresentationItem: ...
	def NbItemElement(self) -> int: ...
	def SetItemElement(self, item_element: StepRepr_HArray1OfRepresentationItem) -> None: ...
	def SetItemElementValue(self, num: int, anelement: StepRepr_RepresentationItem) -> None: ...

class StepRepr_ConstructiveGeometryRepresentation(StepRepr_Representation):
	def __init__(self) -> None: ...

class StepRepr_ConstructiveGeometryRepresentationRelationship(StepRepr_RepresentationRelationship):
	def __init__(self) -> None: ...

class StepRepr_DefinitionalRepresentation(StepRepr_Representation):
	def __init__(self) -> None: ...

class StepRepr_DerivedShapeAspect(StepRepr_ShapeAspect):
	def __init__(self) -> None: ...

class StepRepr_DescriptiveRepresentationItem(StepRepr_RepresentationItem):
	def __init__(self) -> None: ...
	def Description(self) -> TCollection_HAsciiString: ...
	def Init(self, aName: TCollection_HAsciiString, aDescription: TCollection_HAsciiString) -> None: ...
	def SetDescription(self, aDescription: TCollection_HAsciiString) -> None: ...

class StepRepr_ExternallyDefinedRepresentation(StepRepr_Representation):
	def __init__(self) -> None: ...

class StepRepr_FeatureForDatumTargetRelationship(StepRepr_ShapeAspectRelationship):
	def __init__(self) -> None: ...

class StepRepr_GlobalUncertaintyAssignedContext(StepRepr_RepresentationContext):
	def __init__(self) -> None: ...
	def Init(self, aContextIdentifier: TCollection_HAsciiString, aContextType: TCollection_HAsciiString, aUncertainty: StepBasic_HArray1OfUncertaintyMeasureWithUnit) -> None: ...
	def NbUncertainty(self) -> int: ...
	def SetUncertainty(self, aUncertainty: StepBasic_HArray1OfUncertaintyMeasureWithUnit) -> None: ...
	def Uncertainty(self) -> StepBasic_HArray1OfUncertaintyMeasureWithUnit: ...
	def UncertaintyValue(self, num: int) -> StepBasic_UncertaintyMeasureWithUnit: ...

class StepRepr_GlobalUnitAssignedContext(StepRepr_RepresentationContext):
	def __init__(self) -> None: ...
	def Init(self, aContextIdentifier: TCollection_HAsciiString, aContextType: TCollection_HAsciiString, aUnits: StepBasic_HArray1OfNamedUnit) -> None: ...
	def NbUnits(self) -> int: ...
	def SetUnits(self, aUnits: StepBasic_HArray1OfNamedUnit) -> None: ...
	def Units(self) -> StepBasic_HArray1OfNamedUnit: ...
	def UnitsValue(self, num: int) -> StepBasic_NamedUnit: ...

class StepRepr_IntegerRepresentationItem(StepRepr_RepresentationItem):
	def __init__(self) -> None: ...
	def Init(self, theName: TCollection_HAsciiString, theValue: int) -> None: ...
	def SetValue(self, theValue: int) -> None: ...
	def Value(self) -> int: ...

class StepRepr_MakeFromUsageOption(StepRepr_ProductDefinitionUsage):
	def __init__(self) -> None: ...
	@overload
	def Init(self, aProductDefinitionRelationship_Id: TCollection_HAsciiString, aProductDefinitionRelationship_Name: TCollection_HAsciiString, hasProductDefinitionRelationship_Description: bool, aProductDefinitionRelationship_Description: TCollection_HAsciiString, aProductDefinitionRelationship_RelatingProductDefinition: StepBasic_ProductDefinition, aProductDefinitionRelationship_RelatedProductDefinition: StepBasic_ProductDefinition, aRanking: int, aRankingRationale: TCollection_HAsciiString, aQuantity: StepBasic_MeasureWithUnit) -> None: ...
	@overload
	def Init(self, aProductDefinitionRelationship_Id: TCollection_HAsciiString, aProductDefinitionRelationship_Name: TCollection_HAsciiString, hasProductDefinitionRelationship_Description: bool, aProductDefinitionRelationship_Description: TCollection_HAsciiString, aProductDefinitionRelationship_RelatingProductDefinition: StepBasic_ProductDefinitionOrReference, aProductDefinitionRelationship_RelatedProductDefinition: StepBasic_ProductDefinitionOrReference, aRanking: int, aRankingRationale: TCollection_HAsciiString, aQuantity: StepBasic_MeasureWithUnit) -> None: ...
	def Quantity(self) -> StepBasic_MeasureWithUnit: ...
	def Ranking(self) -> int: ...
	def RankingRationale(self) -> TCollection_HAsciiString: ...
	def SetQuantity(self, Quantity: StepBasic_MeasureWithUnit) -> None: ...
	def SetRanking(self, Ranking: int) -> None: ...
	def SetRankingRationale(self, RankingRationale: TCollection_HAsciiString) -> None: ...

class StepRepr_MappedItem(StepRepr_RepresentationItem):
	def __init__(self) -> None: ...
	def Init(self, aName: TCollection_HAsciiString, aMappingSource: StepRepr_RepresentationMap, aMappingTarget: StepRepr_RepresentationItem) -> None: ...
	def MappingSource(self) -> StepRepr_RepresentationMap: ...
	def MappingTarget(self) -> StepRepr_RepresentationItem: ...
	def SetMappingSource(self, aMappingSource: StepRepr_RepresentationMap) -> None: ...
	def SetMappingTarget(self, aMappingTarget: StepRepr_RepresentationItem) -> None: ...

class StepRepr_MaterialProperty(StepRepr_PropertyDefinition):
	def __init__(self) -> None: ...

class StepRepr_MaterialPropertyRepresentation(StepRepr_PropertyDefinitionRepresentation):
	def __init__(self) -> None: ...
	def DependentEnvironment(self) -> StepRepr_DataEnvironment: ...
	def Init(self, aPropertyDefinitionRepresentation_Definition: StepRepr_RepresentedDefinition, aPropertyDefinitionRepresentation_UsedRepresentation: StepRepr_Representation, aDependentEnvironment: StepRepr_DataEnvironment) -> None: ...
	def SetDependentEnvironment(self, DependentEnvironment: StepRepr_DataEnvironment) -> None: ...

class StepRepr_MeasureRepresentationItem(StepRepr_RepresentationItem):
	def __init__(self) -> None: ...
	def Init(self, aName: TCollection_HAsciiString, aValueComponent: StepBasic_MeasureValueMember, aUnitComponent: StepBasic_Unit) -> None: ...
	def Measure(self) -> StepBasic_MeasureWithUnit: ...
	def SetMeasure(self, Measure: StepBasic_MeasureWithUnit) -> None: ...

class StepRepr_ParametricRepresentationContext(StepRepr_RepresentationContext):
	def __init__(self) -> None: ...

class StepRepr_ProductDefinitionShape(StepRepr_PropertyDefinition):
	def __init__(self) -> None: ...

class StepRepr_ReprItemAndMeasureWithUnit(StepRepr_RepresentationItem):
	def __init__(self) -> None: ...
	def GetMeasureRepresentationItem(self) -> StepRepr_MeasureRepresentationItem: ...
	def GetMeasureWithUnit(self) -> StepBasic_MeasureWithUnit: ...
	def GetRepresentationItem(self) -> StepRepr_RepresentationItem: ...
	def Init(self, aMWU: StepBasic_MeasureWithUnit, aRI: StepRepr_RepresentationItem) -> None: ...
	def SetMeasureWithUnit(self, aMWU: StepBasic_MeasureWithUnit) -> None: ...

class StepRepr_ShapeAspectDerivingRelationship(StepRepr_ShapeAspectRelationship):
	def __init__(self) -> None: ...

class StepRepr_ShapeAspectTransition(StepRepr_ShapeAspectRelationship):
	def __init__(self) -> None: ...

class StepRepr_ShapeRepresentationRelationship(StepRepr_RepresentationRelationship):
	def __init__(self) -> None: ...

class StepRepr_StructuralResponseProperty(StepRepr_PropertyDefinition):
	def __init__(self) -> None: ...

class StepRepr_StructuralResponsePropertyDefinitionRepresentation(StepRepr_PropertyDefinitionRepresentation):
	def __init__(self) -> None: ...

class StepRepr_ValueRepresentationItem(StepRepr_RepresentationItem):
	def __init__(self) -> None: ...
	def Init(self, theName: TCollection_HAsciiString, theValueComponentMember: StepBasic_MeasureValueMember) -> None: ...
	def SetValueComponentMember(self, theValueComponentMember: StepBasic_MeasureValueMember) -> None: ...
	def ValueComponentMember(self) -> StepBasic_MeasureValueMember: ...

class StepRepr_Apex(StepRepr_DerivedShapeAspect):
	def __init__(self) -> None: ...

class StepRepr_CentreOfSymmetry(StepRepr_DerivedShapeAspect):
	def __init__(self) -> None: ...

class StepRepr_CompGroupShAspAndCompShAspAndDatumFeatAndShAsp(StepRepr_CompShAspAndDatumFeatAndShAsp):
	def __init__(self) -> None: ...

class StepRepr_CompositeGroupShapeAspect(StepRepr_CompositeShapeAspect):
	def __init__(self) -> None: ...

class StepRepr_ContinuosShapeAspect(StepRepr_CompositeShapeAspect):
	def __init__(self) -> None: ...

class StepRepr_Extension(StepRepr_DerivedShapeAspect):
	def __init__(self) -> None: ...

class StepRepr_GeometricAlignment(StepRepr_DerivedShapeAspect):
	def __init__(self) -> None: ...

class StepRepr_NextAssemblyUsageOccurrence(StepRepr_AssemblyComponentUsage):
	def __init__(self) -> None: ...

class StepRepr_ParallelOffset(StepRepr_DerivedShapeAspect):
	def __init__(self) -> None: ...
	def Init(self, theName: TCollection_HAsciiString, theDescription: TCollection_HAsciiString, theOfShape: StepRepr_ProductDefinitionShape, theProductDefinitional: StepData_Logical, theOffset: StepBasic_MeasureWithUnit) -> None: ...
	def Offset(self) -> StepBasic_MeasureWithUnit: ...
	def SetOffset(self, theOffset: StepBasic_MeasureWithUnit) -> None: ...

class StepRepr_PerpendicularTo(StepRepr_DerivedShapeAspect):
	def __init__(self) -> None: ...

class StepRepr_PromissoryUsageOccurrence(StepRepr_AssemblyComponentUsage):
	def __init__(self) -> None: ...

class StepRepr_QuantifiedAssemblyComponentUsage(StepRepr_AssemblyComponentUsage):
	def __init__(self) -> None: ...
	@overload
	def Init(self, aProductDefinitionRelationship_Id: TCollection_HAsciiString, aProductDefinitionRelationship_Name: TCollection_HAsciiString, hasProductDefinitionRelationship_Description: bool, aProductDefinitionRelationship_Description: TCollection_HAsciiString, aProductDefinitionRelationship_RelatingProductDefinition: StepBasic_ProductDefinition, aProductDefinitionRelationship_RelatedProductDefinition: StepBasic_ProductDefinition, hasAssemblyComponentUsage_ReferenceDesignator: bool, aAssemblyComponentUsage_ReferenceDesignator: TCollection_HAsciiString, aQuantity: StepBasic_MeasureWithUnit) -> None: ...
	@overload
	def Init(self, aProductDefinitionRelationship_Id: TCollection_HAsciiString, aProductDefinitionRelationship_Name: TCollection_HAsciiString, hasProductDefinitionRelationship_Description: bool, aProductDefinitionRelationship_Description: TCollection_HAsciiString, aProductDefinitionRelationship_RelatingProductDefinition: StepBasic_ProductDefinitionOrReference, aProductDefinitionRelationship_RelatedProductDefinition: StepBasic_ProductDefinitionOrReference, hasAssemblyComponentUsage_ReferenceDesignator: bool, aAssemblyComponentUsage_ReferenceDesignator: TCollection_HAsciiString, aQuantity: StepBasic_MeasureWithUnit) -> None: ...
	def Quantity(self) -> StepBasic_MeasureWithUnit: ...
	def SetQuantity(self, Quantity: StepBasic_MeasureWithUnit) -> None: ...

class StepRepr_ReprItemAndLengthMeasureWithUnit(StepRepr_ReprItemAndMeasureWithUnit):
	def __init__(self) -> None: ...
	def GetLengthMeasureWithUnit(self) -> StepBasic_LengthMeasureWithUnit: ...
	def SetLengthMeasureWithUnit(self, aLMWU: StepBasic_LengthMeasureWithUnit) -> None: ...

class StepRepr_ReprItemAndPlaneAngleMeasureWithUnit(StepRepr_ReprItemAndMeasureWithUnit):
	def __init__(self) -> None: ...
	def GetPlaneAngleMeasureWithUnit(self) -> StepBasic_PlaneAngleMeasureWithUnit: ...
	def SetPlaneAngleMeasureWithUnit(self, aLMWU: StepBasic_PlaneAngleMeasureWithUnit) -> None: ...

class StepRepr_RepresentationRelationshipWithTransformation(StepRepr_ShapeRepresentationRelationship):
	def __init__(self) -> None: ...
	def Init(self, aName: TCollection_HAsciiString, aDescription: TCollection_HAsciiString, aRep1: StepRepr_Representation, aRep2: StepRepr_Representation, aTransf: StepRepr_Transformation) -> None: ...
	def SetTransformationOperator(self, aTrans: StepRepr_Transformation) -> None: ...
	def TransformationOperator(self) -> StepRepr_Transformation: ...

class StepRepr_SpecifiedHigherUsageOccurrence(StepRepr_AssemblyComponentUsage):
	def __init__(self) -> None: ...
	@overload
	def Init(self, aProductDefinitionRelationship_Id: TCollection_HAsciiString, aProductDefinitionRelationship_Name: TCollection_HAsciiString, hasProductDefinitionRelationship_Description: bool, aProductDefinitionRelationship_Description: TCollection_HAsciiString, aProductDefinitionRelationship_RelatingProductDefinition: StepBasic_ProductDefinition, aProductDefinitionRelationship_RelatedProductDefinition: StepBasic_ProductDefinition, hasAssemblyComponentUsage_ReferenceDesignator: bool, aAssemblyComponentUsage_ReferenceDesignator: TCollection_HAsciiString, aUpperUsage: StepRepr_AssemblyComponentUsage, aNextUsage: StepRepr_NextAssemblyUsageOccurrence) -> None: ...
	@overload
	def Init(self, aProductDefinitionRelationship_Id: TCollection_HAsciiString, aProductDefinitionRelationship_Name: TCollection_HAsciiString, hasProductDefinitionRelationship_Description: bool, aProductDefinitionRelationship_Description: TCollection_HAsciiString, aProductDefinitionRelationship_RelatingProductDefinition: StepBasic_ProductDefinitionOrReference, aProductDefinitionRelationship_RelatedProductDefinition: StepBasic_ProductDefinitionOrReference, hasAssemblyComponentUsage_ReferenceDesignator: bool, aAssemblyComponentUsage_ReferenceDesignator: TCollection_HAsciiString, aUpperUsage: StepRepr_AssemblyComponentUsage, aNextUsage: StepRepr_NextAssemblyUsageOccurrence) -> None: ...
	def NextUsage(self) -> StepRepr_NextAssemblyUsageOccurrence: ...
	def SetNextUsage(self, NextUsage: StepRepr_NextAssemblyUsageOccurrence) -> None: ...
	def SetUpperUsage(self, UpperUsage: StepRepr_AssemblyComponentUsage) -> None: ...
	def UpperUsage(self) -> StepRepr_AssemblyComponentUsage: ...

class StepRepr_Tangent(StepRepr_DerivedShapeAspect):
	def __init__(self) -> None: ...

class StepRepr_ValueRange(StepRepr_CompoundRepresentationItem):
	def __init__(self) -> None: ...

class StepRepr_AllAroundShapeAspect(StepRepr_ContinuosShapeAspect):
	def __init__(self) -> None: ...

class StepRepr_BetweenShapeAspect(StepRepr_ContinuosShapeAspect):
	def __init__(self) -> None: ...

class StepRepr_ReprItemAndLengthMeasureWithUnitAndQRI(StepRepr_ReprItemAndMeasureWithUnitAndQRI):
	def __init__(self) -> None: ...
	def GetLengthMeasureWithUnit(self) -> StepBasic_LengthMeasureWithUnit: ...
	def SetLengthMeasureWithUnit(self, aLMWU: StepBasic_LengthMeasureWithUnit) -> None: ...

class StepRepr_ReprItemAndPlaneAngleMeasureWithUnitAndQRI(StepRepr_ReprItemAndMeasureWithUnitAndQRI):
	def __init__(self) -> None: ...
	def GetPlaneAngleMeasureWithUnit(self) -> StepBasic_PlaneAngleMeasureWithUnit: ...
	def SetPlaneAngleMeasureWithUnit(self, aLMWU: StepBasic_PlaneAngleMeasureWithUnit) -> None: ...

class StepRepr_ShapeRepresentationRelationshipWithTransformation(StepRepr_RepresentationRelationshipWithTransformation):
	def __init__(self) -> None: ...

#classnotwrapped
class StepRepr_ReprItemAndMeasureWithUnitAndQRI: ...

# harray1 classes

class StepRepr_HArray1OfMaterialPropertyRepresentation(StepRepr_Array1OfMaterialPropertyRepresentation, Standard_Transient):
    def __init__(self, theLower: int, theUpper: int) -> None: ...
    def Array1(self) -> StepRepr_Array1OfMaterialPropertyRepresentation: ...


class StepRepr_HArray1OfRepresentationItem(StepRepr_Array1OfRepresentationItem, Standard_Transient):
    def __init__(self, theLower: int, theUpper: int) -> None: ...
    def Array1(self) -> StepRepr_Array1OfRepresentationItem: ...


class StepRepr_HArray1OfPropertyDefinitionRepresentation(StepRepr_Array1OfPropertyDefinitionRepresentation, Standard_Transient):
    def __init__(self, theLower: int, theUpper: int) -> None: ...
    def Array1(self) -> StepRepr_Array1OfPropertyDefinitionRepresentation: ...


class StepRepr_HArray1OfShapeAspect(StepRepr_Array1OfShapeAspect, Standard_Transient):
    def __init__(self, theLower: int, theUpper: int) -> None: ...
    def Array1(self) -> StepRepr_Array1OfShapeAspect: ...

# harray2 classes
# hsequence classes

class StepRepr_HSequenceOfRepresentationItem(StepRepr_SequenceOfRepresentationItem, Standard_Transient):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, other: StepRepr_SequenceOfRepresentationItem) -> None: ...
    def Sequence(self) -> StepRepr_SequenceOfRepresentationItem: ...
    def Append(self, theSequence: StepRepr_SequenceOfRepresentationItem) -> None: ...


class StepRepr_HSequenceOfMaterialPropertyRepresentation(StepRepr_SequenceOfMaterialPropertyRepresentation, Standard_Transient):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, other: StepRepr_SequenceOfMaterialPropertyRepresentation) -> None: ...
    def Sequence(self) -> StepRepr_SequenceOfMaterialPropertyRepresentation: ...
    def Append(self, theSequence: StepRepr_SequenceOfMaterialPropertyRepresentation) -> None: ...


