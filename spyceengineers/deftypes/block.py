import spyceengineers.deftypes as deftypes

class Block (deftypes.Definition):
    __typevars__ = ['blockTopology', 'displayName', 'id', 'cubeSize', 'size', 'modelOffset', 'criticalComponent', 'icon',
 'components']
    def __new__(cls, gamedata, d):
        if d['Id']['TypeId'] !=  __class__.__name__:
            try:
                cl = next(c for c in __class__.__subclasses__() if c.__name__ == d['Id']['TypeId'])
                return object.__new__(cl)
            except StopIteration:
                raise RuntimeError("Type %s not found in '%s' (%s)" % (d['Id']['TypeId'], __class__.__name__, ", ".join(k.__name__ for k in __class__.__subclasses__())))
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.blockTopology = d['BlockTopology']
        self.displayName = d['DisplayName']
        self.id = d['Id']
        self.cubeSize = d['CubeSize']
        self.size = d['Size']
        self.modelOffset = d['ModelOffset']
        self.criticalComponent = d['CriticalComponent']
        self.icon = d['Icon']
        self.components = d['Components']

                    
class ShipWelder (Block):
    __typevars__ = ['edgeType', 'buildTimeSeconds', 'damageEffectId', 'damagedSound', 'model', 'useModelIntersection',
 'blockPairName', 'mountPoints', 'center', 'public', 'mirroringZ', 'buildProgressModels']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.edgeType = d['EdgeType']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.damageEffectId = d['DamageEffectId']
        self.damagedSound = d['DamagedSound']
        self.model = d['Model']
        self.useModelIntersection = d['UseModelIntersection']
        self.blockPairName = d['BlockPairName']
        self.mountPoints = d['MountPoints']
        self.center = d['Center']
        self.public = d['Public']
        self.mirroringZ = d['MirroringZ']
        self.buildProgressModels = d['BuildProgressModels']

                    
class OxygenGenerator (Block):
    __typevars__ = ['blueprintClasses', 'buildTimeSeconds', 'mirroringY', 'damageEffectId', 'damagedSound', 'model',
 'producedGases', 'idleSound', 'resourceSinkGroup', 'operationalPowerConsumption', 'mountPoints',
 'buildProgressModels', 'resourceSourceGroup', 'edgeType', 'mirroringZ', 'generateSound',
 'inventorySize', 'standbyPowerConsumption', 'inventoryMaxVolume', 'blockPairName',
 'iceConsumptionPerSecond']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.blueprintClasses = d['BlueprintClasses']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.mirroringY = d['MirroringY']
        self.damageEffectId = d['DamageEffectId']
        self.damagedSound = d['DamagedSound']
        self.model = d['Model']
        self.producedGases = d['ProducedGases']
        self.idleSound = d['IdleSound']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.operationalPowerConsumption = d['OperationalPowerConsumption']
        self.mountPoints = d['MountPoints']
        self.buildProgressModels = d['BuildProgressModels']
        self.resourceSourceGroup = d['ResourceSourceGroup']
        self.edgeType = d['EdgeType']
        self.mirroringZ = d['MirroringZ']
        self.generateSound = d['GenerateSound']
        self.inventorySize = d['InventorySize']
        self.standbyPowerConsumption = d['StandbyPowerConsumption']
        self.inventoryMaxVolume = d['InventoryMaxVolume']
        self.blockPairName = d['BlockPairName']
        self.iceConsumptionPerSecond = d['IceConsumptionPerSecond']

                    
class Refinery (Block):
    __typevars__ = ['blueprintClasses', 'buildTimeSeconds', 'damageEffectId', 'materialEfficiency', 'damagedSound',
 'model', 'resourceSinkGroup', 'operationalPowerConsumption', 'buildProgressModels', 'edgeType',
 'inventorySize', 'standbyPowerConsumption', 'inventoryMaxVolume', 'blockPairName', 'refineSpeed']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.blueprintClasses = d['BlueprintClasses']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.damageEffectId = d['DamageEffectId']
        self.materialEfficiency = d['MaterialEfficiency']
        self.damagedSound = d['DamagedSound']
        self.model = d['Model']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.operationalPowerConsumption = d['OperationalPowerConsumption']
        self.buildProgressModels = d['BuildProgressModels']
        self.edgeType = d['EdgeType']
        self.inventorySize = d['InventorySize']
        self.standbyPowerConsumption = d['StandbyPowerConsumption']
        self.inventoryMaxVolume = d['InventoryMaxVolume']
        self.blockPairName = d['BlockPairName']
        self.refineSpeed = d['RefineSpeed']

                    
class OxygenTank (Block):
    __typevars__ = ['blueprintClasses', 'buildTimeSeconds', 'mirroringY', 'damageEffectId', 'damagedSound', 'model',
 'resourceSinkGroup', 'operationalPowerConsumption', 'mountPoints', 'buildProgressModels',
 'resourceSourceGroup', 'edgeType', 'inventorySize', 'capacity', 'standbyPowerConsumption',
 'inventoryMaxVolume', 'blockPairName', 'storedGasId', 'mirroringZ']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.blueprintClasses = d['BlueprintClasses']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.mirroringY = d['MirroringY']
        self.damageEffectId = d['DamageEffectId']
        self.damagedSound = d['DamagedSound']
        self.model = d['Model']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.operationalPowerConsumption = d['OperationalPowerConsumption']
        self.mountPoints = d['MountPoints']
        self.buildProgressModels = d['BuildProgressModels']
        self.resourceSourceGroup = d['ResourceSourceGroup']
        self.edgeType = d['EdgeType']
        self.inventorySize = d['InventorySize']
        self.capacity = d['Capacity']
        self.standbyPowerConsumption = d['StandbyPowerConsumption']
        self.inventoryMaxVolume = d['InventoryMaxVolume']
        self.blockPairName = d['BlockPairName']
        self.storedGasId = d['StoredGasId']
        self.mirroringZ = d['MirroringZ']

                    
class AirVent (Block):
    __typevars__ = ['buildTimeSeconds', 'mirroringY', 'damageEffectId', 'damagedSound', 'model', 'idleSound',
 'pressurizeSound', 'resourceSinkGroup', 'operationalPowerConsumption', 'mountPoints',
 'ventilationCapacityPerSecond', 'buildProgressModels', 'resourceSourceGroup', 'edgeType',
 'standbyPowerConsumption', 'blockPairName', 'depressurizeSound', 'mirroringZ']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.mirroringY = d['MirroringY']
        self.damageEffectId = d['DamageEffectId']
        self.damagedSound = d['DamagedSound']
        self.model = d['Model']
        self.idleSound = d['IdleSound']
        self.pressurizeSound = d['PressurizeSound']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.operationalPowerConsumption = d['OperationalPowerConsumption']
        self.mountPoints = d['MountPoints']
        self.ventilationCapacityPerSecond = d['VentilationCapacityPerSecond']
        self.buildProgressModels = d['BuildProgressModels']
        self.resourceSourceGroup = d['ResourceSourceGroup']
        self.edgeType = d['EdgeType']
        self.standbyPowerConsumption = d['StandbyPowerConsumption']
        self.blockPairName = d['BlockPairName']
        self.depressurizeSound = d['DepressurizeSound']
        self.mirroringZ = d['MirroringZ']

                    
class Conveyor (Block):
    __typevars__ = ['edgeType', 'buildTimeSeconds', 'damageEffectId', 'damagedSound', 'model', 'blockPairName',
 'mirroringZ', 'buildProgressModels']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.edgeType = d['EdgeType']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.damageEffectId = d['DamageEffectId']
        self.damagedSound = d['DamagedSound']
        self.model = d['Model']
        self.blockPairName = d['BlockPairName']
        self.mirroringZ = d['MirroringZ']
        self.buildProgressModels = d['BuildProgressModels']

                    
class ConveyorConnector (Block):
    __typevars__ = ['edgeType', 'buildTimeSeconds', 'blockPairName', 'model', 'buildProgressModels']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.edgeType = d['EdgeType']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.blockPairName = d['BlockPairName']
        self.model = d['Model']
        self.buildProgressModels = d['BuildProgressModels']

                    
class LandingGear (Block):
    __typevars__ = ['buildTimeSeconds', 'mirroringY', 'damageEffectId', 'damagedSound', 'model', 'lockSound',
 'failedAttachSound', 'mountPoints', 'unlockSound', 'buildProgressModels', 'edgeType',
 'blockPairName', 'mirroringZ']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.mirroringY = d['MirroringY']
        self.damageEffectId = d['DamageEffectId']
        self.damagedSound = d['DamagedSound']
        self.model = d['Model']
        self.lockSound = d['LockSound']
        self.failedAttachSound = d['FailedAttachSound']
        self.mountPoints = d['MountPoints']
        self.unlockSound = d['UnlockSound']
        self.buildProgressModels = d['BuildProgressModels']
        self.edgeType = d['EdgeType']
        self.blockPairName = d['BlockPairName']
        self.mirroringZ = d['MirroringZ']

                    
class CubeBlock (Block):
    __typevars__ = ['edgeType', 'buildTimeSeconds']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.edgeType = d['EdgeType']
        self.buildTimeSeconds = d['BuildTimeSeconds']

                    
class SolarPanel (Block):
    __typevars__ = ['buildTimeSeconds', 'panelOffset', 'damageEffectId', 'damagedSound', 'model', 'twoSidedPanel',
 'mountPoints', 'panelOrientation', 'buildProgressModels', 'maxPowerOutput', 'resourceSourceGroup',
 'edgeType', 'blockPairName']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.panelOffset = d['PanelOffset']
        self.damageEffectId = d['DamageEffectId']
        self.damagedSound = d['DamagedSound']
        self.model = d['Model']
        self.twoSidedPanel = d['TwoSidedPanel']
        self.mountPoints = d['MountPoints']
        self.panelOrientation = d['PanelOrientation']
        self.buildProgressModels = d['BuildProgressModels']
        self.maxPowerOutput = d['MaxPowerOutput']
        self.resourceSourceGroup = d['ResourceSourceGroup']
        self.edgeType = d['EdgeType']
        self.blockPairName = d['BlockPairName']

                    
class DebugSphere2 (Block):
    __typevars__ = ['edgeType', 'requiredPowerInput', 'buildTimeSeconds', 'model', 'mountPoints', 'public',
 'buildProgressModels']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.edgeType = d['EdgeType']
        self.requiredPowerInput = d['RequiredPowerInput']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.model = d['Model']
        self.mountPoints = d['MountPoints']
        self.public = d['Public']
        self.buildProgressModels = d['BuildProgressModels']

                    
class DebugSphere3 (Block):
    __typevars__ = ['edgeType', 'requiredPowerInput', 'buildTimeSeconds', 'model', 'mountPoints', 'public',
 'buildProgressModels']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.edgeType = d['EdgeType']
        self.requiredPowerInput = d['RequiredPowerInput']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.model = d['Model']
        self.mountPoints = d['MountPoints']
        self.public = d['Public']
        self.buildProgressModels = d['BuildProgressModels']

                    
class ExtendedPistonBase (Block):
    __typevars__ = ['buildTimeSeconds', 'primarySound', 'mirroringY', 'damageEffectId', 'damagedSound', 'model',
 'resourceSinkGroup', 'topPart', 'mountPoints', 'buildProgressModels', 'requiredPowerInput',
 'edgeType', 'blockPairName', 'center', 'mirroringZ']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.primarySound = d['PrimarySound']
        self.mirroringY = d['MirroringY']
        self.damageEffectId = d['DamageEffectId']
        self.damagedSound = d['DamagedSound']
        self.model = d['Model']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.topPart = d['TopPart']
        self.mountPoints = d['MountPoints']
        self.buildProgressModels = d['BuildProgressModels']
        self.requiredPowerInput = d['RequiredPowerInput']
        self.edgeType = d['EdgeType']
        self.blockPairName = d['BlockPairName']
        self.center = d['Center']
        self.mirroringZ = d['MirroringZ']

                    
class Door (Block):
    __typevars__ = ['edgeType', 'buildTimeSeconds', 'mirroringY', 'closeSound', 'damageEffectId', 'damagedSound',
 'model', 'maxOpen', 'disassembleRatio', 'resourceSinkGroup', 'blockPairName', 'mountPoints',
 'openSound', 'mirroringZ', 'buildProgressModels']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.edgeType = d['EdgeType']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.mirroringY = d['MirroringY']
        self.closeSound = d['CloseSound']
        self.damageEffectId = d['DamageEffectId']
        self.damagedSound = d['DamagedSound']
        self.model = d['Model']
        self.maxOpen = d['MaxOpen']
        self.disassembleRatio = d['DisassembleRatio']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.blockPairName = d['BlockPairName']
        self.mountPoints = d['MountPoints']
        self.openSound = d['OpenSound']
        self.mirroringZ = d['MirroringZ']
        self.buildProgressModels = d['BuildProgressModels']

                    
class CryoChamber (Block):
    __typevars__ = ['idlePowerConsumption', 'edgeType', 'buildTimeSeconds', 'primarySound', 'mirroringY',
 'isPressurized', 'damageEffectId', 'oxygenCapacity', 'damagedSound', 'model', 'characterAnimation',
 'enableFirstPerson', 'outsideSound', 'insideSound', 'resourceSinkGroup', 'blockPairName',
 'mountPoints', 'overlayTexture', 'mirroringZ', 'buildProgressModels']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.idlePowerConsumption = d['IdlePowerConsumption']
        self.edgeType = d['EdgeType']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.primarySound = d['PrimarySound']
        self.mirroringY = d['MirroringY']
        self.isPressurized = d['IsPressurized']
        self.damageEffectId = d['DamageEffectId']
        self.oxygenCapacity = d['OxygenCapacity']
        self.damagedSound = d['DamagedSound']
        self.model = d['Model']
        self.characterAnimation = d['CharacterAnimation']
        self.enableFirstPerson = d['EnableFirstPerson']
        self.outsideSound = d['OutsideSound']
        self.insideSound = d['InsideSound']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.blockPairName = d['BlockPairName']
        self.mountPoints = d['MountPoints']
        self.overlayTexture = d['OverlayTexture']
        self.mirroringZ = d['MirroringZ']
        self.buildProgressModels = d['BuildProgressModels']

                    
class VirtualMass (Block):
    __typevars__ = ['requiredPowerInput', 'edgeType', 'buildTimeSeconds', 'damageEffectId', 'damagedSound', 'model',
 'resourceSinkGroup', 'virtualMass', 'blockPairName', 'public', 'buildProgressModels']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.requiredPowerInput = d['RequiredPowerInput']
        self.edgeType = d['EdgeType']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.damageEffectId = d['DamageEffectId']
        self.damagedSound = d['DamagedSound']
        self.model = d['Model']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.virtualMass = d['VirtualMass']
        self.blockPairName = d['BlockPairName']
        self.public = d['Public']
        self.buildProgressModels = d['BuildProgressModels']

                    
class TimerBlock (Block):
    __typevars__ = ['edgeType', 'buildTimeSeconds', 'resourceSinkGroup', 'blockPairName', 'model', 'buildProgressModels']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.edgeType = d['EdgeType']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.blockPairName = d['BlockPairName']
        self.model = d['Model']
        self.buildProgressModels = d['BuildProgressModels']

                    
class TerminalBlock (Block):
    __typevars__ = ['edgeType', 'buildTimeSeconds', 'blockPairName', 'mountPoints', 'model', 'mirroringZ',
 'buildProgressModels']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.edgeType = d['EdgeType']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.blockPairName = d['BlockPairName']
        self.mountPoints = d['MountPoints']
        self.model = d['Model']
        self.mirroringZ = d['MirroringZ']
        self.buildProgressModels = d['BuildProgressModels']

                    
class InteriorTurret (Block):
    __typevars__ = ['elevationSpeed', 'buildTimeSeconds', 'idleRotation', 'mirroringY', 'damageEffectId', 'damagedSound',
 'model', 'maxRangeMeters', 'maxAzimuthDegrees', 'resourceSinkGroup', 'useModelIntersection',
 'mountPoints', 'buildProgressModels', 'edgeType', 'rotationSpeed', 'minAzimuthDegrees',
 'maxElevationDegrees', 'inventoryMaxVolume', 'blockPairName', 'overlayTexture',
 'weaponDefinitionId', 'minElevationDegrees', 'mirroringZ']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.elevationSpeed = d['ElevationSpeed']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.idleRotation = d['IdleRotation']
        self.mirroringY = d['MirroringY']
        self.damageEffectId = d['DamageEffectId']
        self.damagedSound = d['DamagedSound']
        self.model = d['Model']
        self.maxRangeMeters = d['MaxRangeMeters']
        self.maxAzimuthDegrees = d['MaxAzimuthDegrees']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.useModelIntersection = d['UseModelIntersection']
        self.mountPoints = d['MountPoints']
        self.buildProgressModels = d['BuildProgressModels']
        self.edgeType = d['EdgeType']
        self.rotationSpeed = d['RotationSpeed']
        self.minAzimuthDegrees = d['MinAzimuthDegrees']
        self.maxElevationDegrees = d['MaxElevationDegrees']
        self.inventoryMaxVolume = d['InventoryMaxVolume']
        self.blockPairName = d['BlockPairName']
        self.overlayTexture = d['OverlayTexture']
        self.weaponDefinitionId = d['WeaponDefinitionId']
        self.minElevationDegrees = d['MinElevationDegrees']
        self.mirroringZ = d['MirroringZ']

                    
class Beacon (Block):
    __typevars__ = ['edgeType', 'buildTimeSeconds', 'damageEffectId', 'damagedSound', 'model', 'resourceSinkGroup',
 'blockPairName', 'buildProgressModels']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.edgeType = d['EdgeType']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.damageEffectId = d['DamageEffectId']
        self.damagedSound = d['DamagedSound']
        self.model = d['Model']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.blockPairName = d['BlockPairName']
        self.buildProgressModels = d['BuildProgressModels']

                    
class Cockpit (Block):
    __typevars__ = ['buildTimeSeconds', 'primarySound', 'mirroringY', 'damageEffectId', 'damagedSound', 'model',
 'mountPoints', 'buildProgressModels', 'edgeType', 'characterAnimation', 'enableFirstPerson',
 'blockPairName', 'enableBuilderCockpit', 'mirroringZ', 'enableShipControl']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.primarySound = d['PrimarySound']
        self.mirroringY = d['MirroringY']
        self.damageEffectId = d['DamageEffectId']
        self.damagedSound = d['DamagedSound']
        self.model = d['Model']
        self.mountPoints = d['MountPoints']
        self.buildProgressModels = d['BuildProgressModels']
        self.edgeType = d['EdgeType']
        self.characterAnimation = d['CharacterAnimation']
        self.enableFirstPerson = d['EnableFirstPerson']
        self.blockPairName = d['BlockPairName']
        self.enableBuilderCockpit = d['EnableBuilderCockpit']
        self.mirroringZ = d['MirroringZ']
        self.enableShipControl = d['EnableShipControl']

                    
class Gyro (Block):
    __typevars__ = ['buildTimeSeconds', 'mirroringY', 'damageEffectId', 'damagedSound', 'model', 'resourceSinkGroup',
 'mountPoints', 'buildProgressModels', 'edgeType', 'requiredPowerInput', 'forceMagnitude',
 'blockPairName', 'mirroringZ']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.mirroringY = d['MirroringY']
        self.damageEffectId = d['DamageEffectId']
        self.damagedSound = d['DamagedSound']
        self.model = d['Model']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.mountPoints = d['MountPoints']
        self.buildProgressModels = d['BuildProgressModels']
        self.edgeType = d['EdgeType']
        self.requiredPowerInput = d['RequiredPowerInput']
        self.forceMagnitude = d['ForceMagnitude']
        self.blockPairName = d['BlockPairName']
        self.mirroringZ = d['MirroringZ']

                    
class Projector (Block):
    __typevars__ = ['requiredPowerInput', 'edgeType', 'buildTimeSeconds', 'damageEffectId', 'damagedSound', 'model',
 'resourceSinkGroup', 'blockPairName', 'mountPoints', 'public', 'buildProgressModels']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.requiredPowerInput = d['RequiredPowerInput']
        self.edgeType = d['EdgeType']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.damageEffectId = d['DamageEffectId']
        self.damagedSound = d['DamagedSound']
        self.model = d['Model']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.blockPairName = d['BlockPairName']
        self.mountPoints = d['MountPoints']
        self.public = d['Public']
        self.buildProgressModels = d['BuildProgressModels']

                    
class RemoteControl (Block):
    __typevars__ = ['buildTimeSeconds', 'mirroringY', 'damageEffectId', 'damagedSound', 'model', 'resourceSinkGroup',
 'mountPoints', 'public', 'buildProgressModels', 'requiredPowerInput', 'edgeType',
 'enableFirstPerson', 'blockPairName', 'enableBuilderCockpit', 'enableShipControl']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.mirroringY = d['MirroringY']
        self.damageEffectId = d['DamageEffectId']
        self.damagedSound = d['DamagedSound']
        self.model = d['Model']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.mountPoints = d['MountPoints']
        self.public = d['Public']
        self.buildProgressModels = d['BuildProgressModels']
        self.requiredPowerInput = d['RequiredPowerInput']
        self.edgeType = d['EdgeType']
        self.enableFirstPerson = d['EnableFirstPerson']
        self.blockPairName = d['BlockPairName']
        self.enableBuilderCockpit = d['EnableBuilderCockpit']
        self.enableShipControl = d['EnableShipControl']

                    
class ShipGrinder (Block):
    __typevars__ = ['edgeType', 'buildTimeSeconds', 'damageEffectId', 'damagedSound', 'model', 'useModelIntersection',
 'blockPairName', 'mountPoints', 'center', 'public', 'mirroringZ', 'buildProgressModels']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.edgeType = d['EdgeType']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.damageEffectId = d['DamageEffectId']
        self.damagedSound = d['DamagedSound']
        self.model = d['Model']
        self.useModelIntersection = d['UseModelIntersection']
        self.blockPairName = d['BlockPairName']
        self.mountPoints = d['MountPoints']
        self.center = d['Center']
        self.public = d['Public']
        self.mirroringZ = d['MirroringZ']
        self.buildProgressModels = d['BuildProgressModels']

                    
class Reactor (Block):
    __typevars__ = ['buildTimeSeconds', 'primarySound', 'mirroringY', 'fuelId', 'damageEffectId', 'damagedSound',
 'model', 'mountPoints', 'buildProgressModels', 'maxPowerOutput', 'resourceSourceGroup', 'edgeType',
 'inventorySize', 'blockPairName', 'mirroringZ']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.primarySound = d['PrimarySound']
        self.mirroringY = d['MirroringY']
        self.fuelId = d['FuelId']
        self.damageEffectId = d['DamageEffectId']
        self.damagedSound = d['DamagedSound']
        self.model = d['Model']
        self.mountPoints = d['MountPoints']
        self.buildProgressModels = d['BuildProgressModels']
        self.maxPowerOutput = d['MaxPowerOutput']
        self.resourceSourceGroup = d['ResourceSourceGroup']
        self.edgeType = d['EdgeType']
        self.inventorySize = d['InventorySize']
        self.blockPairName = d['BlockPairName']
        self.mirroringZ = d['MirroringZ']

                    
class GravityGenerator (Block):
    __typevars__ = ['sound', 'edgeType', 'requiredPowerInput', 'buildTimeSeconds', 'mirroringY', 'damageEffectId',
 'damagedSound', 'model', 'resourceSinkGroup', 'blockPairName', 'mountPoints', 'mirroringZ',
 'buildProgressModels']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.sound = d['Sound']
        self.edgeType = d['EdgeType']
        self.requiredPowerInput = d['RequiredPowerInput']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.mirroringY = d['MirroringY']
        self.damageEffectId = d['DamageEffectId']
        self.damagedSound = d['DamagedSound']
        self.model = d['Model']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.blockPairName = d['BlockPairName']
        self.mountPoints = d['MountPoints']
        self.mirroringZ = d['MirroringZ']
        self.buildProgressModels = d['BuildProgressModels']

                    
class SmallGatlingGun (Block):
    __typevars__ = ['edgeType', 'buildTimeSeconds', 'mirroringY', 'damageEffectId', 'damagedSound', 'model',
 'resourceSinkGroup', 'inventoryMaxVolume', 'blockPairName', 'mountPoints', 'center',
 'weaponDefinitionId', 'mirroringZ', 'buildProgressModels']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.edgeType = d['EdgeType']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.mirroringY = d['MirroringY']
        self.damageEffectId = d['DamageEffectId']
        self.damagedSound = d['DamagedSound']
        self.model = d['Model']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.inventoryMaxVolume = d['InventoryMaxVolume']
        self.blockPairName = d['BlockPairName']
        self.mountPoints = d['MountPoints']
        self.center = d['Center']
        self.weaponDefinitionId = d['WeaponDefinitionId']
        self.mirroringZ = d['MirroringZ']
        self.buildProgressModels = d['BuildProgressModels']

                    
class SoundBlock (Block):
    __typevars__ = ['edgeType', 'buildTimeSeconds', 'mirroringY', 'damageEffectId', 'damagedSound', 'model',
 'resourceSinkGroup', 'blockPairName', 'mountPoints', 'mirroringZ', 'buildProgressModels']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.edgeType = d['EdgeType']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.mirroringY = d['MirroringY']
        self.damageEffectId = d['DamageEffectId']
        self.damagedSound = d['DamagedSound']
        self.model = d['Model']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.blockPairName = d['BlockPairName']
        self.mountPoints = d['MountPoints']
        self.mirroringZ = d['MirroringZ']
        self.buildProgressModels = d['BuildProgressModels']

                    
class AirtightHangarDoor (Block):
    __typevars__ = ['sound', 'edgeType', 'buildTimeSeconds', 'mirroringY', 'damageEffectId', 'damagedSound', 'model',
 'resourceSinkGroup', 'powerConsumptionMoving', 'subpartMovementDistance', 'blockPairName',
 'mountPoints', 'center', 'openingSpeed', 'powerConsumptionIdle', 'mirroringZ', 'buildProgressModels']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.sound = d['Sound']
        self.edgeType = d['EdgeType']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.mirroringY = d['MirroringY']
        self.damageEffectId = d['DamageEffectId']
        self.damagedSound = d['DamagedSound']
        self.model = d['Model']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.powerConsumptionMoving = d['PowerConsumptionMoving']
        self.subpartMovementDistance = d['SubpartMovementDistance']
        self.blockPairName = d['BlockPairName']
        self.mountPoints = d['MountPoints']
        self.center = d['Center']
        self.openingSpeed = d['OpeningSpeed']
        self.powerConsumptionIdle = d['PowerConsumptionIdle']
        self.mirroringZ = d['MirroringZ']
        self.buildProgressModels = d['BuildProgressModels']

                    
class LargeMissileTurret (Block):
    __typevars__ = ['elevationSpeed', 'buildTimeSeconds', 'idleRotation', 'mirroringY', 'damageEffectId', 'damagedSound',
 'model', 'maxRangeMeters', 'maxAzimuthDegrees', 'resourceSinkGroup', 'useModelIntersection',
 'mountPoints', 'buildProgressModels', 'edgeType', 'rotationSpeed', 'minAzimuthDegrees',
 'maxElevationDegrees', 'inventoryMaxVolume', 'blockPairName', 'overlayTexture',
 'weaponDefinitionId', 'minElevationDegrees', 'mirroringZ']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.elevationSpeed = d['ElevationSpeed']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.idleRotation = d['IdleRotation']
        self.mirroringY = d['MirroringY']
        self.damageEffectId = d['DamageEffectId']
        self.damagedSound = d['DamagedSound']
        self.model = d['Model']
        self.maxRangeMeters = d['MaxRangeMeters']
        self.maxAzimuthDegrees = d['MaxAzimuthDegrees']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.useModelIntersection = d['UseModelIntersection']
        self.mountPoints = d['MountPoints']
        self.buildProgressModels = d['BuildProgressModels']
        self.edgeType = d['EdgeType']
        self.rotationSpeed = d['RotationSpeed']
        self.minAzimuthDegrees = d['MinAzimuthDegrees']
        self.maxElevationDegrees = d['MaxElevationDegrees']
        self.inventoryMaxVolume = d['InventoryMaxVolume']
        self.blockPairName = d['BlockPairName']
        self.overlayTexture = d['OverlayTexture']
        self.weaponDefinitionId = d['WeaponDefinitionId']
        self.minElevationDegrees = d['MinElevationDegrees']
        self.mirroringZ = d['MirroringZ']

                    
class Decoy (Block):
    __typevars__ = ['edgeType', 'buildTimeSeconds', 'blockPairName', 'model', 'public', 'buildProgressModels']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.edgeType = d['EdgeType']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.blockPairName = d['BlockPairName']
        self.model = d['Model']
        self.public = d['Public']
        self.buildProgressModels = d['BuildProgressModels']

                    
class SpaceBall (Block):
    __typevars__ = ['requiredPowerInput', 'edgeType', 'buildTimeSeconds', 'model', 'maxVirtualMass', 'buildProgressModels']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.requiredPowerInput = d['RequiredPowerInput']
        self.edgeType = d['EdgeType']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.model = d['Model']
        self.maxVirtualMass = d['MaxVirtualMass']
        self.buildProgressModels = d['BuildProgressModels']

                    
class ReflectorLight (Block):
    __typevars__ = ['buildTimeSeconds', 'damageEffectId', 'damagedSound', 'model', 'resourceSinkGroup', 'lightGlare',
 'lightIntensity', 'mountPoints', 'buildProgressModels', 'lightFalloff', 'reflectorTexture',
 'edgeType', 'requiredPowerInput', 'blockPairName', 'lightRadius', 'mirroringZ']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.damageEffectId = d['DamageEffectId']
        self.damagedSound = d['DamagedSound']
        self.model = d['Model']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.lightGlare = d['LightGlare']
        self.lightIntensity = d['LightIntensity']
        self.mountPoints = d['MountPoints']
        self.buildProgressModels = d['BuildProgressModels']
        self.lightFalloff = d['LightFalloff']
        self.reflectorTexture = d['ReflectorTexture']
        self.edgeType = d['EdgeType']
        self.requiredPowerInput = d['RequiredPowerInput']
        self.blockPairName = d['BlockPairName']
        self.lightRadius = d['LightRadius']
        self.mirroringZ = d['MirroringZ']

                    
class OreDetector (Block):
    __typevars__ = ['edgeType', 'buildTimeSeconds', 'mirroringY', 'damageEffectId', 'damagedSound', 'model',
 'maximumRange', 'resourceSinkGroup', 'blockPairName', 'mountPoints', 'mirroringZ',
 'buildProgressModels']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.edgeType = d['EdgeType']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.mirroringY = d['MirroringY']
        self.damageEffectId = d['DamageEffectId']
        self.damagedSound = d['DamagedSound']
        self.model = d['Model']
        self.maximumRange = d['MaximumRange']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.blockPairName = d['BlockPairName']
        self.mountPoints = d['MountPoints']
        self.mirroringZ = d['MirroringZ']
        self.buildProgressModels = d['BuildProgressModels']

                    
class SensorBlock (Block):
    __typevars__ = ['edgeType', 'buildTimeSeconds', 'mirroringY', 'damageEffectId', 'damagedSound', 'model',
 'resourceSinkGroup', 'blockPairName', 'mountPoints', 'mirroringZ', 'buildProgressModels', 'maxRange']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.edgeType = d['EdgeType']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.mirroringY = d['MirroringY']
        self.damageEffectId = d['DamageEffectId']
        self.damagedSound = d['DamagedSound']
        self.model = d['Model']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.blockPairName = d['BlockPairName']
        self.mountPoints = d['MountPoints']
        self.mirroringZ = d['MirroringZ']
        self.buildProgressModels = d['BuildProgressModels']
        self.maxRange = d['MaxRange']

                    
class PistonBase (Block):
    __typevars__ = ['buildTimeSeconds', 'primarySound', 'mirroringY', 'damageEffectId', 'damagedSound', 'model',
 'resourceSinkGroup', 'topPart', 'mountPoints', 'public', 'buildProgressModels',
 'requiredPowerInput', 'edgeType', 'blockPairName', 'mirroringZ']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.primarySound = d['PrimarySound']
        self.mirroringY = d['MirroringY']
        self.damageEffectId = d['DamageEffectId']
        self.damagedSound = d['DamagedSound']
        self.model = d['Model']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.topPart = d['TopPart']
        self.mountPoints = d['MountPoints']
        self.public = d['Public']
        self.buildProgressModels = d['BuildProgressModels']
        self.requiredPowerInput = d['RequiredPowerInput']
        self.edgeType = d['EdgeType']
        self.blockPairName = d['BlockPairName']
        self.mirroringZ = d['MirroringZ']

                    
class SmallMissileLauncher (Block):
    __typevars__ = ['edgeType', 'buildTimeSeconds', 'damageEffectId', 'damagedSound', 'model', 'resourceSinkGroup',
 'inventoryMaxVolume', 'blockPairName', 'mountPoints', 'center', 'weaponDefinitionId',
 'buildProgressModels']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.edgeType = d['EdgeType']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.damageEffectId = d['DamageEffectId']
        self.damagedSound = d['DamagedSound']
        self.model = d['Model']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.inventoryMaxVolume = d['InventoryMaxVolume']
        self.blockPairName = d['BlockPairName']
        self.mountPoints = d['MountPoints']
        self.center = d['Center']
        self.weaponDefinitionId = d['WeaponDefinitionId']
        self.buildProgressModels = d['BuildProgressModels']

                    
class CargoContainer (Block):
    __typevars__ = ['edgeType', 'buildTimeSeconds', 'blockPairName', 'model', 'inventorySize', 'mirroringZ',
 'buildProgressModels']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.edgeType = d['EdgeType']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.blockPairName = d['BlockPairName']
        self.model = d['Model']
        self.inventorySize = d['InventorySize']
        self.mirroringZ = d['MirroringZ']
        self.buildProgressModels = d['BuildProgressModels']

                    
class Wheel (Block):
    __typevars__ = ['buildTimeSeconds', 'mirroringY', 'damageEffectId', 'damagedSound', 'model', 'useModelIntersection',
 'mountPoints', 'deformationRatio', 'public', 'buildProgressModels', 'edgeType', 'inventorySize',
 'blockPairName', 'mirroringZ']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.mirroringY = d['MirroringY']
        self.damageEffectId = d['DamageEffectId']
        self.damagedSound = d['DamagedSound']
        self.model = d['Model']
        self.useModelIntersection = d['UseModelIntersection']
        self.mountPoints = d['MountPoints']
        self.deformationRatio = d['DeformationRatio']
        self.public = d['Public']
        self.buildProgressModels = d['BuildProgressModels']
        self.edgeType = d['EdgeType']
        self.inventorySize = d['InventorySize']
        self.blockPairName = d['BlockPairName']
        self.mirroringZ = d['MirroringZ']

                    
class MergeBlock (Block):
    __typevars__ = ['edgeType', 'buildTimeSeconds', 'damageEffectId', 'strength', 'damagedSound', 'model', 'mirroringX',
 'blockPairName', 'mountPoints', 'public', 'buildProgressModels']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.edgeType = d['EdgeType']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.damageEffectId = d['DamageEffectId']
        self.strength = d['Strength']
        self.damagedSound = d['DamagedSound']
        self.model = d['Model']
        self.mirroringX = d['MirroringX']
        self.blockPairName = d['BlockPairName']
        self.mountPoints = d['MountPoints']
        self.public = d['Public']
        self.buildProgressModels = d['BuildProgressModels']

                    
class LaserAntenna (Block):
    __typevars__ = ['buildTimeSeconds', 'mirroringY', 'damageEffectId', 'damagedSound', 'model', 'requireLineOfSight',
 'powerInputTurning', 'maxAzimuthDegrees', 'resourceSinkGroup', 'rotationRate', 'mountPoints',
 'buildProgressModels', 'edgeType', 'powerInputIdle', 'minAzimuthDegrees', 'maxElevationDegrees',
 'blockPairName', 'minElevationDegrees', 'powerInputLasing', 'maxRange']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.mirroringY = d['MirroringY']
        self.damageEffectId = d['DamageEffectId']
        self.damagedSound = d['DamagedSound']
        self.model = d['Model']
        self.requireLineOfSight = d['RequireLineOfSight']
        self.powerInputTurning = d['PowerInputTurning']
        self.maxAzimuthDegrees = d['MaxAzimuthDegrees']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.rotationRate = d['RotationRate']
        self.mountPoints = d['MountPoints']
        self.buildProgressModels = d['BuildProgressModels']
        self.edgeType = d['EdgeType']
        self.powerInputIdle = d['PowerInputIdle']
        self.minAzimuthDegrees = d['MinAzimuthDegrees']
        self.maxElevationDegrees = d['MaxElevationDegrees']
        self.blockPairName = d['BlockPairName']
        self.minElevationDegrees = d['MinElevationDegrees']
        self.powerInputLasing = d['PowerInputLasing']
        self.maxRange = d['MaxRange']

                    
class DebugSphere1 (Block):
    __typevars__ = ['edgeType', 'requiredPowerInput', 'buildTimeSeconds', 'model', 'mountPoints', 'public',
 'buildProgressModels']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.edgeType = d['EdgeType']
        self.requiredPowerInput = d['RequiredPowerInput']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.model = d['Model']
        self.mountPoints = d['MountPoints']
        self.public = d['Public']
        self.buildProgressModels = d['BuildProgressModels']

                    
class Assembler (Block):
    __typevars__ = ['blueprintClasses', 'buildTimeSeconds', 'damageEffectId', 'damagedSound', 'model',
 'resourceSinkGroup', 'operationalPowerConsumption', 'buildProgressModels', 'edgeType',
 'inventorySize', 'standbyPowerConsumption', 'inventoryMaxVolume', 'blockPairName']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.blueprintClasses = d['BlueprintClasses']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.damageEffectId = d['DamageEffectId']
        self.damagedSound = d['DamagedSound']
        self.model = d['Model']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.operationalPowerConsumption = d['OperationalPowerConsumption']
        self.buildProgressModels = d['BuildProgressModels']
        self.edgeType = d['EdgeType']
        self.inventorySize = d['InventorySize']
        self.standbyPowerConsumption = d['StandbyPowerConsumption']
        self.inventoryMaxVolume = d['InventoryMaxVolume']
        self.blockPairName = d['BlockPairName']

                    
class BatteryBlock (Block):
    __typevars__ = ['buildTimeSeconds', 'damageEffectId', 'damagedSound', 'model', 'resourceSinkGroup', 'maxStoredPower',
 'public', 'buildProgressModels', 'maxPowerOutput', 'resourceSourceGroup', 'edgeType',
 'requiredPowerInput', 'initialStoredPowerRatio', 'inventorySize', 'blockPairName']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.damageEffectId = d['DamageEffectId']
        self.damagedSound = d['DamagedSound']
        self.model = d['Model']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.maxStoredPower = d['MaxStoredPower']
        self.public = d['Public']
        self.buildProgressModels = d['BuildProgressModels']
        self.maxPowerOutput = d['MaxPowerOutput']
        self.resourceSourceGroup = d['ResourceSourceGroup']
        self.edgeType = d['EdgeType']
        self.requiredPowerInput = d['RequiredPowerInput']
        self.initialStoredPowerRatio = d['InitialStoredPowerRatio']
        self.inventorySize = d['InventorySize']
        self.blockPairName = d['BlockPairName']

                    
class MotorAdvancedRotor (Block):
    __typevars__ = ['edgeType', 'buildTimeSeconds', 'mirroringY', 'model', 'useModelIntersection', 'blockPairName',
 'mountPoints', 'public', 'mirroringZ', 'buildProgressModels']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.edgeType = d['EdgeType']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.mirroringY = d['MirroringY']
        self.model = d['Model']
        self.useModelIntersection = d['UseModelIntersection']
        self.blockPairName = d['BlockPairName']
        self.mountPoints = d['MountPoints']
        self.public = d['Public']
        self.mirroringZ = d['MirroringZ']
        self.buildProgressModels = d['BuildProgressModels']

                    
class MotorSuspension (Block):
    __typevars__ = ['buildTimeSeconds', 'minHeight', 'primarySound', 'mirroringY', 'damageEffectId', 'maxForceMagnitude',
 'damagedSound', 'model', 'resourceSinkGroup', 'useModelIntersection', 'mountPoints', 'rotorPart',
 'buildProgressModels', 'edgeType', 'requiredPowerInput', 'mirroringZ', 'blockPairName',
 'maxHeight', 'propulsionForce']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.minHeight = d['MinHeight']
        self.primarySound = d['PrimarySound']
        self.mirroringY = d['MirroringY']
        self.damageEffectId = d['DamageEffectId']
        self.maxForceMagnitude = d['MaxForceMagnitude']
        self.damagedSound = d['DamagedSound']
        self.model = d['Model']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.useModelIntersection = d['UseModelIntersection']
        self.mountPoints = d['MountPoints']
        self.rotorPart = d['RotorPart']
        self.buildProgressModels = d['BuildProgressModels']
        self.edgeType = d['EdgeType']
        self.requiredPowerInput = d['RequiredPowerInput']
        self.mirroringZ = d['MirroringZ']
        self.blockPairName = d['BlockPairName']
        self.maxHeight = d['MaxHeight']
        self.propulsionForce = d['PropulsionForce']

                    
class JumpDrive (Block):
    __typevars__ = ['edgeType', 'requiredPowerInput', 'buildTimeSeconds', 'powerNeededForJump', 'mirroringY',
 'damageEffectId', 'damagedSound', 'model', 'maxJumpMass', 'resourceSinkGroup', 'blockPairName',
 'mountPoints', 'maxJumpDistance', 'mirroringZ', 'buildProgressModels']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.edgeType = d['EdgeType']
        self.requiredPowerInput = d['RequiredPowerInput']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.powerNeededForJump = d['PowerNeededForJump']
        self.mirroringY = d['MirroringY']
        self.damageEffectId = d['DamageEffectId']
        self.damagedSound = d['DamagedSound']
        self.model = d['Model']
        self.maxJumpMass = d['MaxJumpMass']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.blockPairName = d['BlockPairName']
        self.mountPoints = d['MountPoints']
        self.maxJumpDistance = d['MaxJumpDistance']
        self.mirroringZ = d['MirroringZ']
        self.buildProgressModels = d['BuildProgressModels']

                    
class SmallMissileLauncherReload (Block):
    __typevars__ = ['buildTimeSeconds', 'damageEffectId', 'damagedSound', 'model', 'resourceSinkGroup',
 'inventoryMaxVolume', 'blockPairName', 'mountPoints', 'center', 'weaponDefinitionId',
 'buildProgressModels']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.damageEffectId = d['DamageEffectId']
        self.damagedSound = d['DamagedSound']
        self.model = d['Model']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.inventoryMaxVolume = d['InventoryMaxVolume']
        self.blockPairName = d['BlockPairName']
        self.mountPoints = d['MountPoints']
        self.center = d['Center']
        self.weaponDefinitionId = d['WeaponDefinitionId']
        self.buildProgressModels = d['BuildProgressModels']

                    
class LargeGatlingTurret (Block):
    __typevars__ = ['elevationSpeed', 'buildTimeSeconds', 'idleRotation', 'mirroringY', 'damageEffectId', 'damagedSound',
 'model', 'maxRangeMeters', 'maxAzimuthDegrees', 'resourceSinkGroup', 'useModelIntersection',
 'mountPoints', 'buildProgressModels', 'edgeType', 'rotationSpeed', 'minAzimuthDegrees',
 'maxElevationDegrees', 'inventoryMaxVolume', 'blockPairName', 'overlayTexture',
 'weaponDefinitionId', 'minElevationDegrees', 'mirroringZ']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.elevationSpeed = d['ElevationSpeed']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.idleRotation = d['IdleRotation']
        self.mirroringY = d['MirroringY']
        self.damageEffectId = d['DamageEffectId']
        self.damagedSound = d['DamagedSound']
        self.model = d['Model']
        self.maxRangeMeters = d['MaxRangeMeters']
        self.maxAzimuthDegrees = d['MaxAzimuthDegrees']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.useModelIntersection = d['UseModelIntersection']
        self.mountPoints = d['MountPoints']
        self.buildProgressModels = d['BuildProgressModels']
        self.edgeType = d['EdgeType']
        self.rotationSpeed = d['RotationSpeed']
        self.minAzimuthDegrees = d['MinAzimuthDegrees']
        self.maxElevationDegrees = d['MaxElevationDegrees']
        self.inventoryMaxVolume = d['InventoryMaxVolume']
        self.blockPairName = d['BlockPairName']
        self.overlayTexture = d['OverlayTexture']
        self.weaponDefinitionId = d['WeaponDefinitionId']
        self.minElevationDegrees = d['MinElevationDegrees']
        self.mirroringZ = d['MirroringZ']

                    
class UpgradeModule (Block):
    __typevars__ = ['edgeType', 'damageEffectId', 'damagedSound', 'model', 'mirroringX', 'blockPairName', 'mountPoints',
 'upgrades', 'mirroringZ', 'buildProgressModels']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.edgeType = d['EdgeType']
        self.damageEffectId = d['DamageEffectId']
        self.damagedSound = d['DamagedSound']
        self.model = d['Model']
        self.mirroringX = d['MirroringX']
        self.blockPairName = d['BlockPairName']
        self.mountPoints = d['MountPoints']
        self.upgrades = d['Upgrades']
        self.mirroringZ = d['MirroringZ']
        self.buildProgressModels = d['BuildProgressModels']

                    
class Warhead (Block):
    __typevars__ = ['edgeType', 'buildTimeSeconds', 'warheadExplosionDamage', 'explosionRadius', 'blockPairName',
 'model', 'buildProgressModels']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.edgeType = d['EdgeType']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.warheadExplosionDamage = d['WarheadExplosionDamage']
        self.explosionRadius = d['ExplosionRadius']
        self.blockPairName = d['BlockPairName']
        self.model = d['Model']
        self.buildProgressModels = d['BuildProgressModels']

                    
class MyProgrammableBlock (Block):
    __typevars__ = ['edgeType', 'buildTimeSeconds', 'damageEffectId', 'damagedSound', 'model', 'resourceSinkGroup',
 'blockPairName', 'mountPoints', 'public', 'mirroringZ', 'buildProgressModels']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.edgeType = d['EdgeType']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.damageEffectId = d['DamageEffectId']
        self.damagedSound = d['DamagedSound']
        self.model = d['Model']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.blockPairName = d['BlockPairName']
        self.mountPoints = d['MountPoints']
        self.public = d['Public']
        self.mirroringZ = d['MirroringZ']
        self.buildProgressModels = d['BuildProgressModels']

                    
class ShipConnector (Block):
    __typevars__ = ['edgeType', 'buildTimeSeconds', 'damageEffectId', 'damagedSound', 'model', 'blockPairName',
 'mountPoints', 'mirroringZ', 'buildProgressModels']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.edgeType = d['EdgeType']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.damageEffectId = d['DamageEffectId']
        self.damagedSound = d['DamagedSound']
        self.model = d['Model']
        self.blockPairName = d['BlockPairName']
        self.mountPoints = d['MountPoints']
        self.mirroringZ = d['MirroringZ']
        self.buildProgressModels = d['BuildProgressModels']

                    
class ConveyorSorter (Block):
    __typevars__ = ['edgeType', 'buildTimeSeconds', 'mirroringY', 'damageEffectId', 'damagedSound', 'model',
 'inventorySize', 'powerInput', 'resourceSinkGroup', 'blockPairName', 'mirroringZ',
 'buildProgressModels']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.edgeType = d['EdgeType']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.mirroringY = d['MirroringY']
        self.damageEffectId = d['DamageEffectId']
        self.damagedSound = d['DamagedSound']
        self.model = d['Model']
        self.inventorySize = d['InventorySize']
        self.powerInput = d['PowerInput']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.blockPairName = d['BlockPairName']
        self.mirroringZ = d['MirroringZ']
        self.buildProgressModels = d['BuildProgressModels']

                    
class Passage (Block):
    __typevars__ = ['edgeType', 'buildTimeSeconds', 'mirroringY', 'model', 'blockPairName', 'mountPoints', 'mirroringZ',
 'buildProgressModels']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.edgeType = d['EdgeType']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.mirroringY = d['MirroringY']
        self.model = d['Model']
        self.blockPairName = d['BlockPairName']
        self.mountPoints = d['MountPoints']
        self.mirroringZ = d['MirroringZ']
        self.buildProgressModels = d['BuildProgressModels']

                    
class TextPanel (Block):
    __typevars__ = ['requiredPowerInput', 'edgeType', 'buildTimeSeconds', 'model', 'resourceSinkGroup', 'blockPairName',
 'mountPoints', 'mirroringZ', 'buildProgressModels']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.requiredPowerInput = d['RequiredPowerInput']
        self.edgeType = d['EdgeType']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.model = d['Model']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.blockPairName = d['BlockPairName']
        self.mountPoints = d['MountPoints']
        self.mirroringZ = d['MirroringZ']
        self.buildProgressModels = d['BuildProgressModels']

                    
class MotorAdvancedStator (Block):
    __typevars__ = ['buildTimeSeconds', 'primarySound', 'mirroringY', 'damageEffectId', 'maxForceMagnitude',
 'damagedSound', 'model', 'rotorDisplacementInModel', 'resourceSinkGroup', 'mountPoints', 'public',
 'rotorPart', 'buildProgressModels', 'edgeType', 'requiredPowerInput', 'rotorDisplacementMax',
 'blockPairName', 'rotorDisplacementMin', 'mirroringZ']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.primarySound = d['PrimarySound']
        self.mirroringY = d['MirroringY']
        self.damageEffectId = d['DamageEffectId']
        self.maxForceMagnitude = d['MaxForceMagnitude']
        self.damagedSound = d['DamagedSound']
        self.model = d['Model']
        self.rotorDisplacementInModel = d['RotorDisplacementInModel']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.mountPoints = d['MountPoints']
        self.public = d['Public']
        self.rotorPart = d['RotorPart']
        self.buildProgressModels = d['BuildProgressModels']
        self.edgeType = d['EdgeType']
        self.requiredPowerInput = d['RequiredPowerInput']
        self.rotorDisplacementMax = d['RotorDisplacementMax']
        self.blockPairName = d['BlockPairName']
        self.rotorDisplacementMin = d['RotorDisplacementMin']
        self.mirroringZ = d['MirroringZ']

                    
class ButtonPanel (Block):
    __typevars__ = ['buttonColors', 'buildTimeSeconds', 'mirroringY', 'damageEffectId', 'buttonCount', 'damagedSound',
 'model', 'unassignedButtonColor', 'resourceSinkGroup', 'mountPoints', 'buttonSymbols',
 'buildProgressModels', 'edgeType', 'blockPairName', 'mirroringZ']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.buttonColors = d['ButtonColors']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.mirroringY = d['MirroringY']
        self.damageEffectId = d['DamageEffectId']
        self.buttonCount = d['ButtonCount']
        self.damagedSound = d['DamagedSound']
        self.model = d['Model']
        self.unassignedButtonColor = d['UnassignedButtonColor']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.mountPoints = d['MountPoints']
        self.buttonSymbols = d['ButtonSymbols']
        self.buildProgressModels = d['BuildProgressModels']
        self.edgeType = d['EdgeType']
        self.blockPairName = d['BlockPairName']
        self.mirroringZ = d['MirroringZ']

                    
class Collector (Block):
    __typevars__ = ['buildTimeSeconds', 'mirroringY', 'damageEffectId', 'damagedSound', 'model', 'resourceSinkGroup',
 'mountPoints', 'buildProgressModels', 'edgeType', 'actionSound', 'inventorySize', 'blockPairName',
 'mirroringZ']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.mirroringY = d['MirroringY']
        self.damageEffectId = d['DamageEffectId']
        self.damagedSound = d['DamagedSound']
        self.model = d['Model']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.mountPoints = d['MountPoints']
        self.buildProgressModels = d['BuildProgressModels']
        self.edgeType = d['EdgeType']
        self.actionSound = d['ActionSound']
        self.inventorySize = d['InventorySize']
        self.blockPairName = d['BlockPairName']
        self.mirroringZ = d['MirroringZ']

                    
class Drill (Block):
    __typevars__ = ['buildTimeSeconds', 'mirroringY', 'damageEffectId', 'damagedSound', 'model', 'sensorOffset',
 'resourceSinkGroup', 'useModelIntersection', 'mountPoints', 'deformationRatio',
 'buildProgressModels', 'edgeType', 'sensorRadius', 'blockPairName', 'mirroringZ']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.mirroringY = d['MirroringY']
        self.damageEffectId = d['DamageEffectId']
        self.damagedSound = d['DamagedSound']
        self.model = d['Model']
        self.sensorOffset = d['SensorOffset']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.useModelIntersection = d['UseModelIntersection']
        self.mountPoints = d['MountPoints']
        self.deformationRatio = d['DeformationRatio']
        self.buildProgressModels = d['BuildProgressModels']
        self.edgeType = d['EdgeType']
        self.sensorRadius = d['SensorRadius']
        self.blockPairName = d['BlockPairName']
        self.mirroringZ = d['MirroringZ']

                    
class GravityGeneratorSphere (Block):
    __typevars__ = ['sound', 'edgeType', 'buildTimeSeconds', 'mirroringY', 'consumptionPower', 'damageEffectId',
 'maxRadius', 'model', 'damagedSound', 'basePowerInput', 'resourceSinkGroup', 'blockPairName',
 'mountPoints', 'minRadius', 'mirroringZ', 'buildProgressModels']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.sound = d['Sound']
        self.edgeType = d['EdgeType']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.mirroringY = d['MirroringY']
        self.consumptionPower = d['ConsumptionPower']
        self.damageEffectId = d['DamageEffectId']
        self.maxRadius = d['MaxRadius']
        self.model = d['Model']
        self.damagedSound = d['DamagedSound']
        self.basePowerInput = d['BasePowerInput']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.blockPairName = d['BlockPairName']
        self.mountPoints = d['MountPoints']
        self.minRadius = d['MinRadius']
        self.mirroringZ = d['MirroringZ']
        self.buildProgressModels = d['BuildProgressModels']

                    
class Thrust (Block):
    __typevars__ = ['buildTimeSeconds', 'slowdownFactor', 'primarySound', 'flameDamageLengthScale', 'damageEffectId',
 'damagedSound', 'model', 'flameIdleColor', 'flameGlareSize', 'flamePointMaterial',
 'minPowerConsumption', 'resourceSinkGroup', 'mountPoints', 'flameLengthScale',
 'buildProgressModels', 'edgeType', 'flameVisibilityDistance', 'flameLengthMaterial',
 'flameGlareMaterial', 'flameGlareQuerySize', 'forceMagnitude', 'maxPowerConsumption',
 'flameFullColor', 'blockPairName', 'center', 'mirroringZ']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.slowdownFactor = d['SlowdownFactor']
        self.primarySound = d['PrimarySound']
        self.flameDamageLengthScale = d['FlameDamageLengthScale']
        self.damageEffectId = d['DamageEffectId']
        self.damagedSound = d['DamagedSound']
        self.model = d['Model']
        self.flameIdleColor = d['FlameIdleColor']
        self.flameGlareSize = d['FlameGlareSize']
        self.flamePointMaterial = d['FlamePointMaterial']
        self.minPowerConsumption = d['MinPowerConsumption']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.mountPoints = d['MountPoints']
        self.flameLengthScale = d['FlameLengthScale']
        self.buildProgressModels = d['BuildProgressModels']
        self.edgeType = d['EdgeType']
        self.flameVisibilityDistance = d['FlameVisibilityDistance']
        self.flameLengthMaterial = d['FlameLengthMaterial']
        self.flameGlareMaterial = d['FlameGlareMaterial']
        self.flameGlareQuerySize = d['FlameGlareQuerySize']
        self.forceMagnitude = d['ForceMagnitude']
        self.maxPowerConsumption = d['MaxPowerConsumption']
        self.flameFullColor = d['FlameFullColor']
        self.blockPairName = d['BlockPairName']
        self.center = d['Center']
        self.mirroringZ = d['MirroringZ']

                    
class RadioAntenna (Block):
    __typevars__ = ['edgeType', 'buildTimeSeconds', 'mirroringY', 'damageEffectId', 'damagedSound', 'model',
 'resourceSinkGroup', 'blockPairName', 'mountPoints', 'buildProgressModels']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.edgeType = d['EdgeType']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.mirroringY = d['MirroringY']
        self.damageEffectId = d['DamageEffectId']
        self.damagedSound = d['DamagedSound']
        self.model = d['Model']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.blockPairName = d['BlockPairName']
        self.mountPoints = d['MountPoints']
        self.buildProgressModels = d['BuildProgressModels']

                    
class CameraBlock (Block):
    __typevars__ = ['buildTimeSeconds', 'mirroringY', 'damageEffectId', 'damagedSound', 'model', 'minFov',
 'resourceSinkGroup', 'mountPoints', 'public', 'buildProgressModels', 'edgeType',
 'requiredPowerInput', 'maxFov', 'blockPairName', 'overlayTexture', 'mirroringZ']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.mirroringY = d['MirroringY']
        self.damageEffectId = d['DamageEffectId']
        self.damagedSound = d['DamagedSound']
        self.model = d['Model']
        self.minFov = d['MinFov']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.mountPoints = d['MountPoints']
        self.public = d['Public']
        self.buildProgressModels = d['BuildProgressModels']
        self.edgeType = d['EdgeType']
        self.requiredPowerInput = d['RequiredPowerInput']
        self.maxFov = d['MaxFov']
        self.blockPairName = d['BlockPairName']
        self.overlayTexture = d['OverlayTexture']
        self.mirroringZ = d['MirroringZ']

                    
class PistonTop (Block):
    __typevars__ = ['edgeType', 'buildTimeSeconds', 'mirroringY', 'model', 'useModelIntersection', 'blockPairName',
 'mountPoints', 'public', 'mirroringZ', 'buildProgressModels']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.edgeType = d['EdgeType']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.mirroringY = d['MirroringY']
        self.model = d['Model']
        self.useModelIntersection = d['UseModelIntersection']
        self.blockPairName = d['BlockPairName']
        self.mountPoints = d['MountPoints']
        self.public = d['Public']
        self.mirroringZ = d['MirroringZ']
        self.buildProgressModels = d['BuildProgressModels']

                    
class MedicalRoom (Block):
    __typevars__ = ['edgeType', 'buildTimeSeconds', 'damageEffectId', 'damagedSound', 'model', 'progressSound',
 'idleSound', 'resourceSinkGroup', 'blockPairName', 'mountPoints', 'buildProgressModels']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.edgeType = d['EdgeType']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.damageEffectId = d['DamageEffectId']
        self.damagedSound = d['DamagedSound']
        self.model = d['Model']
        self.progressSound = d['ProgressSound']
        self.idleSound = d['IdleSound']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.blockPairName = d['BlockPairName']
        self.mountPoints = d['MountPoints']
        self.buildProgressModels = d['BuildProgressModels']

                    
class MotorStator (Block):
    __typevars__ = ['buildTimeSeconds', 'primarySound', 'mirroringY', 'damageEffectId', 'maxForceMagnitude',
 'damagedSound', 'model', 'rotorDisplacementInModel', 'resourceSinkGroup', 'mountPoints',
 'buildProgressModels', 'rotorPart', 'edgeType', 'requiredPowerInput', 'rotorDisplacementMax',
 'blockPairName', 'rotorDisplacementMin', 'mirroringZ']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.primarySound = d['PrimarySound']
        self.mirroringY = d['MirroringY']
        self.damageEffectId = d['DamageEffectId']
        self.maxForceMagnitude = d['MaxForceMagnitude']
        self.damagedSound = d['DamagedSound']
        self.model = d['Model']
        self.rotorDisplacementInModel = d['RotorDisplacementInModel']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.mountPoints = d['MountPoints']
        self.buildProgressModels = d['BuildProgressModels']
        self.rotorPart = d['RotorPart']
        self.edgeType = d['EdgeType']
        self.requiredPowerInput = d['RequiredPowerInput']
        self.rotorDisplacementMax = d['RotorDisplacementMax']
        self.blockPairName = d['BlockPairName']
        self.rotorDisplacementMin = d['RotorDisplacementMin']
        self.mirroringZ = d['MirroringZ']

                    
class MotorRotor (Block):
    __typevars__ = ['edgeType', 'buildTimeSeconds', 'mirroringY', 'model', 'useModelIntersection', 'blockPairName',
 'mountPoints', 'mirroringZ', 'buildProgressModels']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.edgeType = d['EdgeType']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.mirroringY = d['MirroringY']
        self.model = d['Model']
        self.useModelIntersection = d['UseModelIntersection']
        self.blockPairName = d['BlockPairName']
        self.mountPoints = d['MountPoints']
        self.mirroringZ = d['MirroringZ']
        self.buildProgressModels = d['BuildProgressModels']

                    
class AirtightSlideDoor (Block):
    __typevars__ = ['sound', 'edgeType', 'buildTimeSeconds', 'mirroringY', 'damageEffectId', 'damagedSound', 'model',
 'disassembleRatio', 'resourceSinkGroup', 'powerConsumptionMoving', 'subpartMovementDistance',
 'blockPairName', 'mountPoints', 'center', 'openingSpeed', 'powerConsumptionIdle', 'mirroringZ',
 'buildProgressModels']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.sound = d['Sound']
        self.edgeType = d['EdgeType']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.mirroringY = d['MirroringY']
        self.damageEffectId = d['DamageEffectId']
        self.damagedSound = d['DamagedSound']
        self.model = d['Model']
        self.disassembleRatio = d['DisassembleRatio']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.powerConsumptionMoving = d['PowerConsumptionMoving']
        self.subpartMovementDistance = d['SubpartMovementDistance']
        self.blockPairName = d['BlockPairName']
        self.mountPoints = d['MountPoints']
        self.center = d['Center']
        self.openingSpeed = d['OpeningSpeed']
        self.powerConsumptionIdle = d['PowerConsumptionIdle']
        self.mirroringZ = d['MirroringZ']
        self.buildProgressModels = d['BuildProgressModels']

                    
class InteriorLight (Block):
    __typevars__ = ['edgeType', 'requiredPowerInput', 'buildTimeSeconds', 'damageEffectId', 'damagedSound', 'model',
 'resourceSinkGroup', 'lightGlare', 'lightIntensity', 'blockPairName', 'mountPoints', 'lightRadius',
 'mirroringZ', 'buildProgressModels', 'lightFalloff']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.edgeType = d['EdgeType']
        self.requiredPowerInput = d['RequiredPowerInput']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.damageEffectId = d['DamageEffectId']
        self.damagedSound = d['DamagedSound']
        self.model = d['Model']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.lightGlare = d['LightGlare']
        self.lightIntensity = d['LightIntensity']
        self.blockPairName = d['BlockPairName']
        self.mountPoints = d['MountPoints']
        self.lightRadius = d['LightRadius']
        self.mirroringZ = d['MirroringZ']
        self.buildProgressModels = d['BuildProgressModels']
        self.lightFalloff = d['LightFalloff']

                    
class OxygenFarm (Block):
    __typevars__ = ['resourceSourceGroup', 'edgeType', 'buildTimeSeconds', 'panelOffset', 'damageEffectId',
 'damagedSound', 'model', 'twoSidedPanel', 'producedGas', 'resourceSinkGroup',
 'operationalPowerConsumption', 'blockPairName', 'mountPoints', 'center', 'panelOrientation',
 'buildProgressModels']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.resourceSourceGroup = d['ResourceSourceGroup']
        self.edgeType = d['EdgeType']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.panelOffset = d['PanelOffset']
        self.damageEffectId = d['DamageEffectId']
        self.damagedSound = d['DamagedSound']
        self.model = d['Model']
        self.twoSidedPanel = d['TwoSidedPanel']
        self.producedGas = d['ProducedGas']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.operationalPowerConsumption = d['OperationalPowerConsumption']
        self.blockPairName = d['BlockPairName']
        self.mountPoints = d['MountPoints']
        self.center = d['Center']
        self.panelOrientation = d['PanelOrientation']
        self.buildProgressModels = d['BuildProgressModels']

__all__ = ['Block', 'ShipWelder', 'OxygenGenerator', 'Refinery', 'OxygenTank', 'AirVent',
 'Conveyor', 'ConveyorConnector', 'LandingGear', 'CubeBlock', 'SolarPanel', 'DebugSphere2',
 'DebugSphere3', 'ExtendedPistonBase', 'Door', 'CryoChamber', 'VirtualMass', 'TimerBlock',
 'TerminalBlock', 'InteriorTurret', 'Beacon', 'Cockpit', 'Gyro', 'Projector', 'RemoteControl',
 'ShipGrinder', 'Reactor', 'GravityGenerator', 'SmallGatlingGun', 'SoundBlock',
 'AirtightHangarDoor', 'LargeMissileTurret', 'Decoy', 'SpaceBall', 'ReflectorLight', 'OreDetector',
 'SensorBlock', 'PistonBase', 'SmallMissileLauncher', 'CargoContainer', 'Wheel', 'MergeBlock',
 'LaserAntenna', 'DebugSphere1', 'Assembler', 'BatteryBlock', 'MotorAdvancedRotor',
 'MotorSuspension', 'JumpDrive', 'SmallMissileLauncherReload', 'LargeGatlingTurret',
 'UpgradeModule', 'Warhead', 'MyProgrammableBlock', 'ShipConnector', 'ConveyorSorter', 'Passage',
 'TextPanel', 'MotorAdvancedStator', 'ButtonPanel', 'Collector', 'Drill', 'GravityGeneratorSphere',
 'Thrust', 'RadioAntenna', 'CameraBlock', 'PistonTop', 'MedicalRoom', 'MotorStator', 'MotorRotor',
 'AirtightSlideDoor', 'InteriorLight', 'OxygenFarm']
