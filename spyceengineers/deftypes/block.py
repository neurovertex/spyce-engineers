import spyceengineers.deftypes as deftypes
            
__all__ = ['Block', 'MotorAdvancedRotor', 'SmallGatlingGun', 'LargeMissileTurret', 'OxygenTank',
 'ReflectorLight', 'CargoContainer', 'Wheel', 'MergeBlock', 'MotorStator', 'Refinery',
 'RemoteControl', 'ShipConnector', 'Door', 'ShipWelder', 'SoundBlock', 'Collector', 'LandingGear',
 'LargeGatlingTurret', 'ConveyorConnector', 'InteriorLight', 'SolarPanel', 'PistonBase', 'Drill',
 'Warhead', 'GravityGenerator', 'Thrust', 'CubeBlock', 'Assembler', 'PistonTop', 'CryoChamber',
 'LaserAntenna', 'Passage', 'SpaceBall', 'TerminalBlock', 'CameraBlock', 'OxygenFarm', 'Projector',
 'AirtightSlideDoor', 'DebugSphere2', 'OreDetector', 'MyProgrammableBlock', 'Cockpit',
 'UpgradeModule', 'MedicalRoom', 'JumpDrive', 'DebugSphere1', 'ShipGrinder',
 'SmallMissileLauncherReload', 'BatteryBlock', 'InteriorTurret', 'AirVent', 'ExtendedPistonBase',
 'AirtightHangarDoor', 'Conveyor', 'SensorBlock', 'TextPanel', 'GravityGeneratorSphere', 'Gyro',
 'MotorRotor', 'MotorSuspension', 'ButtonPanel', 'Decoy', 'SmallMissileLauncher', 'RadioAntenna',
 'Beacon', 'ConveyorSorter', 'OxygenGenerator', 'VirtualMass', 'DebugSphere3', 'TimerBlock',
 'Reactor', 'MotorAdvancedStator']

class Block (deftypes.Definition):
    __typevars__ = ['cubeSize', 'modelOffset', 'components', 'icon', 'size', 'id', 'displayName', 'blockTopology',
 'criticalComponent']
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
        self.cubeSize = d['CubeSize']
        self.modelOffset = d['ModelOffset']
        self.components = d['Components']
        self.icon = d['Icon']
        self.size = d['Size']
        self.id = d['Id']
        self.displayName = d['DisplayName']
        self.blockTopology = d['BlockTopology']
        self.criticalComponent = d['CriticalComponent']

                    
class MotorAdvancedRotor (Block):
    __typevars__ = ['mirroringZ', 'model', 'mountPoints', 'buildTimeSeconds', 'edgeType', 'blockPairName', 'public',
 'buildProgressModels', 'mirroringY', 'useModelIntersection']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.mirroringZ = d['MirroringZ']
        self.model = d['Model']
        self.mountPoints = d['MountPoints']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.edgeType = d['EdgeType']
        self.blockPairName = d['BlockPairName']
        self.public = d['Public']
        self.buildProgressModels = d['BuildProgressModels']
        self.mirroringY = d['MirroringY']
        self.useModelIntersection = d['UseModelIntersection']

                    
class SmallGatlingGun (Block):
    __typevars__ = ['resourceSinkGroup', 'mirroringZ', 'model', 'inventoryMaxVolume', 'damageEffectId', 'mountPoints',
 'buildTimeSeconds', 'edgeType', 'damagedSound', 'center', 'blockPairName', 'buildProgressModels',
 'weaponDefinitionId', 'mirroringY']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.mirroringZ = d['MirroringZ']
        self.model = d['Model']
        self.inventoryMaxVolume = d['InventoryMaxVolume']
        self.damageEffectId = d['DamageEffectId']
        self.mountPoints = d['MountPoints']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.edgeType = d['EdgeType']
        self.damagedSound = d['DamagedSound']
        self.center = d['Center']
        self.blockPairName = d['BlockPairName']
        self.buildProgressModels = d['BuildProgressModels']
        self.weaponDefinitionId = d['WeaponDefinitionId']
        self.mirroringY = d['MirroringY']

                    
class LargeMissileTurret (Block):
    __typevars__ = ['overlayTexture', 'maxAzimuthDegrees', 'minElevationDegrees', 'inventoryMaxVolume', 'damageEffectId',
 'elevationSpeed', 'mountPoints', 'buildTimeSeconds', 'rotationSpeed', 'edgeType',
 'buildProgressModels', 'weaponDefinitionId', 'resourceSinkGroup', 'mirroringZ', 'model',
 'maxElevationDegrees', 'minAzimuthDegrees', 'damagedSound', 'maxRangeMeters', 'blockPairName',
 'idleRotation', 'mirroringY', 'useModelIntersection']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.overlayTexture = d['OverlayTexture']
        self.maxAzimuthDegrees = d['MaxAzimuthDegrees']
        self.minElevationDegrees = d['MinElevationDegrees']
        self.inventoryMaxVolume = d['InventoryMaxVolume']
        self.damageEffectId = d['DamageEffectId']
        self.elevationSpeed = d['ElevationSpeed']
        self.mountPoints = d['MountPoints']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.rotationSpeed = d['RotationSpeed']
        self.edgeType = d['EdgeType']
        self.buildProgressModels = d['BuildProgressModels']
        self.weaponDefinitionId = d['WeaponDefinitionId']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.mirroringZ = d['MirroringZ']
        self.model = d['Model']
        self.maxElevationDegrees = d['MaxElevationDegrees']
        self.minAzimuthDegrees = d['MinAzimuthDegrees']
        self.damagedSound = d['DamagedSound']
        self.maxRangeMeters = d['MaxRangeMeters']
        self.blockPairName = d['BlockPairName']
        self.idleRotation = d['IdleRotation']
        self.mirroringY = d['MirroringY']
        self.useModelIntersection = d['UseModelIntersection']

                    
class OxygenTank (Block):
    __typevars__ = ['standbyPowerConsumption', 'inventoryMaxVolume', 'damageEffectId', 'mountPoints', 'blueprintClasses',
 'buildTimeSeconds', 'edgeType', 'buildProgressModels', 'resourceSinkGroup', 'mirroringZ', 'model',
 'inventorySize', 'operationalPowerConsumption', 'damagedSound', 'blockPairName',
 'resourceSourceGroup', 'mirroringY', 'storedGasId', 'capacity']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.standbyPowerConsumption = d['StandbyPowerConsumption']
        self.inventoryMaxVolume = d['InventoryMaxVolume']
        self.damageEffectId = d['DamageEffectId']
        self.mountPoints = d['MountPoints']
        self.blueprintClasses = d['BlueprintClasses']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.edgeType = d['EdgeType']
        self.buildProgressModels = d['BuildProgressModels']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.mirroringZ = d['MirroringZ']
        self.model = d['Model']
        self.inventorySize = d['InventorySize']
        self.operationalPowerConsumption = d['OperationalPowerConsumption']
        self.damagedSound = d['DamagedSound']
        self.blockPairName = d['BlockPairName']
        self.resourceSourceGroup = d['ResourceSourceGroup']
        self.mirroringY = d['MirroringY']
        self.storedGasId = d['StoredGasId']
        self.capacity = d['Capacity']

                    
class ReflectorLight (Block):
    __typevars__ = ['lightGlare', 'damageEffectId', 'mountPoints', 'buildTimeSeconds', 'edgeType', 'buildProgressModels',
 'lightRadius', 'resourceSinkGroup', 'requiredPowerInput', 'lightFalloff', 'mirroringZ', 'model',
 'reflectorTexture', 'damagedSound', 'blockPairName', 'lightIntensity']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.lightGlare = d['LightGlare']
        self.damageEffectId = d['DamageEffectId']
        self.mountPoints = d['MountPoints']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.edgeType = d['EdgeType']
        self.buildProgressModels = d['BuildProgressModels']
        self.lightRadius = d['LightRadius']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.requiredPowerInput = d['RequiredPowerInput']
        self.lightFalloff = d['LightFalloff']
        self.mirroringZ = d['MirroringZ']
        self.model = d['Model']
        self.reflectorTexture = d['ReflectorTexture']
        self.damagedSound = d['DamagedSound']
        self.blockPairName = d['BlockPairName']
        self.lightIntensity = d['LightIntensity']

                    
class CargoContainer (Block):
    __typevars__ = ['blockPairName', 'buildProgressModels', 'mirroringZ', 'model', 'buildTimeSeconds', 'inventorySize',
 'edgeType']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.blockPairName = d['BlockPairName']
        self.buildProgressModels = d['BuildProgressModels']
        self.mirroringZ = d['MirroringZ']
        self.model = d['Model']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.inventorySize = d['InventorySize']
        self.edgeType = d['EdgeType']

                    
class Wheel (Block):
    __typevars__ = ['damageEffectId', 'mountPoints', 'buildTimeSeconds', 'edgeType', 'deformationRatio', 'public',
 'buildProgressModels', 'mirroringZ', 'model', 'inventorySize', 'damagedSound', 'blockPairName',
 'mirroringY', 'useModelIntersection']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.damageEffectId = d['DamageEffectId']
        self.mountPoints = d['MountPoints']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.edgeType = d['EdgeType']
        self.deformationRatio = d['DeformationRatio']
        self.public = d['Public']
        self.buildProgressModels = d['BuildProgressModels']
        self.mirroringZ = d['MirroringZ']
        self.model = d['Model']
        self.inventorySize = d['InventorySize']
        self.damagedSound = d['DamagedSound']
        self.blockPairName = d['BlockPairName']
        self.mirroringY = d['MirroringY']
        self.useModelIntersection = d['UseModelIntersection']

                    
class MergeBlock (Block):
    __typevars__ = ['model', 'mirroringX', 'damageEffectId', 'mountPoints', 'strength', 'buildTimeSeconds', 'edgeType',
 'damagedSound', 'blockPairName', 'public', 'buildProgressModels']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.model = d['Model']
        self.mirroringX = d['MirroringX']
        self.damageEffectId = d['DamageEffectId']
        self.mountPoints = d['MountPoints']
        self.strength = d['Strength']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.edgeType = d['EdgeType']
        self.damagedSound = d['DamagedSound']
        self.blockPairName = d['BlockPairName']
        self.public = d['Public']
        self.buildProgressModels = d['BuildProgressModels']

                    
class MotorStator (Block):
    __typevars__ = ['damageEffectId', 'rotorPart', 'mountPoints', 'buildTimeSeconds', 'rotorDisplacementMin', 'edgeType',
 'buildProgressModels', 'rotorDisplacementMax', 'primarySound', 'resourceSinkGroup',
 'requiredPowerInput', 'mirroringZ', 'model', 'maxForceMagnitude', 'rotorDisplacementInModel',
 'damagedSound', 'blockPairName', 'mirroringY']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.damageEffectId = d['DamageEffectId']
        self.rotorPart = d['RotorPart']
        self.mountPoints = d['MountPoints']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.rotorDisplacementMin = d['RotorDisplacementMin']
        self.edgeType = d['EdgeType']
        self.buildProgressModels = d['BuildProgressModels']
        self.rotorDisplacementMax = d['RotorDisplacementMax']
        self.primarySound = d['PrimarySound']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.requiredPowerInput = d['RequiredPowerInput']
        self.mirroringZ = d['MirroringZ']
        self.model = d['Model']
        self.maxForceMagnitude = d['MaxForceMagnitude']
        self.rotorDisplacementInModel = d['RotorDisplacementInModel']
        self.damagedSound = d['DamagedSound']
        self.blockPairName = d['BlockPairName']
        self.mirroringY = d['MirroringY']

                    
class Refinery (Block):
    __typevars__ = ['standbyPowerConsumption', 'inventoryMaxVolume', 'damageEffectId', 'buildTimeSeconds',
 'blueprintClasses', 'edgeType', 'buildProgressModels', 'refineSpeed', 'resourceSinkGroup', 'model',
 'materialEfficiency', 'inventorySize', 'operationalPowerConsumption', 'damagedSound',
 'blockPairName']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.standbyPowerConsumption = d['StandbyPowerConsumption']
        self.inventoryMaxVolume = d['InventoryMaxVolume']
        self.damageEffectId = d['DamageEffectId']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.blueprintClasses = d['BlueprintClasses']
        self.edgeType = d['EdgeType']
        self.buildProgressModels = d['BuildProgressModels']
        self.refineSpeed = d['RefineSpeed']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.model = d['Model']
        self.materialEfficiency = d['MaterialEfficiency']
        self.inventorySize = d['InventorySize']
        self.operationalPowerConsumption = d['OperationalPowerConsumption']
        self.damagedSound = d['DamagedSound']
        self.blockPairName = d['BlockPairName']

                    
class RemoteControl (Block):
    __typevars__ = ['enableBuilderCockpit', 'damageEffectId', 'mountPoints', 'buildTimeSeconds', 'edgeType', 'public',
 'buildProgressModels', 'enableFirstPerson', 'enableShipControl', 'resourceSinkGroup',
 'requiredPowerInput', 'model', 'damagedSound', 'blockPairName', 'mirroringY']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.enableBuilderCockpit = d['EnableBuilderCockpit']
        self.damageEffectId = d['DamageEffectId']
        self.mountPoints = d['MountPoints']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.edgeType = d['EdgeType']
        self.public = d['Public']
        self.buildProgressModels = d['BuildProgressModels']
        self.enableFirstPerson = d['EnableFirstPerson']
        self.enableShipControl = d['EnableShipControl']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.requiredPowerInput = d['RequiredPowerInput']
        self.model = d['Model']
        self.damagedSound = d['DamagedSound']
        self.blockPairName = d['BlockPairName']
        self.mirroringY = d['MirroringY']

                    
class ShipConnector (Block):
    __typevars__ = ['mirroringZ', 'model', 'damageEffectId', 'buildTimeSeconds', 'mountPoints', 'edgeType',
 'damagedSound', 'blockPairName', 'buildProgressModels']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.mirroringZ = d['MirroringZ']
        self.model = d['Model']
        self.damageEffectId = d['DamageEffectId']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.mountPoints = d['MountPoints']
        self.edgeType = d['EdgeType']
        self.damagedSound = d['DamagedSound']
        self.blockPairName = d['BlockPairName']
        self.buildProgressModels = d['BuildProgressModels']

                    
class Door (Block):
    __typevars__ = ['resourceSinkGroup', 'mirroringZ', 'model', 'damageEffectId', 'closeSound', 'mountPoints',
 'buildTimeSeconds', 'edgeType', 'damagedSound', 'blockPairName', 'disassembleRatio',
 'buildProgressModels', 'openSound', 'maxOpen', 'mirroringY']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.mirroringZ = d['MirroringZ']
        self.model = d['Model']
        self.damageEffectId = d['DamageEffectId']
        self.closeSound = d['CloseSound']
        self.mountPoints = d['MountPoints']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.edgeType = d['EdgeType']
        self.damagedSound = d['DamagedSound']
        self.blockPairName = d['BlockPairName']
        self.disassembleRatio = d['DisassembleRatio']
        self.buildProgressModels = d['BuildProgressModels']
        self.openSound = d['OpenSound']
        self.maxOpen = d['MaxOpen']
        self.mirroringY = d['MirroringY']

                    
class ShipWelder (Block):
    __typevars__ = ['mirroringZ', 'model', 'damageEffectId', 'mountPoints', 'buildTimeSeconds', 'edgeType',
 'damagedSound', 'center', 'blockPairName', 'public', 'buildProgressModels', 'useModelIntersection']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.mirroringZ = d['MirroringZ']
        self.model = d['Model']
        self.damageEffectId = d['DamageEffectId']
        self.mountPoints = d['MountPoints']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.edgeType = d['EdgeType']
        self.damagedSound = d['DamagedSound']
        self.center = d['Center']
        self.blockPairName = d['BlockPairName']
        self.public = d['Public']
        self.buildProgressModels = d['BuildProgressModels']
        self.useModelIntersection = d['UseModelIntersection']

                    
class SoundBlock (Block):
    __typevars__ = ['resourceSinkGroup', 'mirroringZ', 'model', 'damageEffectId', 'mountPoints', 'buildTimeSeconds',
 'edgeType', 'damagedSound', 'blockPairName', 'buildProgressModels', 'mirroringY']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.mirroringZ = d['MirroringZ']
        self.model = d['Model']
        self.damageEffectId = d['DamageEffectId']
        self.mountPoints = d['MountPoints']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.edgeType = d['EdgeType']
        self.damagedSound = d['DamagedSound']
        self.blockPairName = d['BlockPairName']
        self.buildProgressModels = d['BuildProgressModels']
        self.mirroringY = d['MirroringY']

                    
class Collector (Block):
    __typevars__ = ['damageEffectId', 'buildTimeSeconds', 'mountPoints', 'edgeType', 'buildProgressModels',
 'actionSound', 'resourceSinkGroup', 'mirroringZ', 'model', 'inventorySize', 'damagedSound',
 'blockPairName', 'mirroringY']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.damageEffectId = d['DamageEffectId']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.mountPoints = d['MountPoints']
        self.edgeType = d['EdgeType']
        self.buildProgressModels = d['BuildProgressModels']
        self.actionSound = d['ActionSound']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.mirroringZ = d['MirroringZ']
        self.model = d['Model']
        self.inventorySize = d['InventorySize']
        self.damagedSound = d['DamagedSound']
        self.blockPairName = d['BlockPairName']
        self.mirroringY = d['MirroringY']

                    
class LandingGear (Block):
    __typevars__ = ['damageEffectId', 'mountPoints', 'buildTimeSeconds', 'edgeType', 'unlockSound', 'lockSound',
 'buildProgressModels', 'mirroringZ', 'model', 'failedAttachSound', 'damagedSound', 'blockPairName',
 'mirroringY']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.damageEffectId = d['DamageEffectId']
        self.mountPoints = d['MountPoints']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.edgeType = d['EdgeType']
        self.unlockSound = d['UnlockSound']
        self.lockSound = d['LockSound']
        self.buildProgressModels = d['BuildProgressModels']
        self.mirroringZ = d['MirroringZ']
        self.model = d['Model']
        self.failedAttachSound = d['FailedAttachSound']
        self.damagedSound = d['DamagedSound']
        self.blockPairName = d['BlockPairName']
        self.mirroringY = d['MirroringY']

                    
class LargeGatlingTurret (Block):
    __typevars__ = ['overlayTexture', 'maxAzimuthDegrees', 'minElevationDegrees', 'inventoryMaxVolume', 'damageEffectId',
 'elevationSpeed', 'mountPoints', 'buildTimeSeconds', 'rotationSpeed', 'edgeType',
 'buildProgressModels', 'weaponDefinitionId', 'resourceSinkGroup', 'mirroringZ', 'model',
 'maxElevationDegrees', 'minAzimuthDegrees', 'damagedSound', 'maxRangeMeters', 'blockPairName',
 'idleRotation', 'mirroringY', 'useModelIntersection']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.overlayTexture = d['OverlayTexture']
        self.maxAzimuthDegrees = d['MaxAzimuthDegrees']
        self.minElevationDegrees = d['MinElevationDegrees']
        self.inventoryMaxVolume = d['InventoryMaxVolume']
        self.damageEffectId = d['DamageEffectId']
        self.elevationSpeed = d['ElevationSpeed']
        self.mountPoints = d['MountPoints']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.rotationSpeed = d['RotationSpeed']
        self.edgeType = d['EdgeType']
        self.buildProgressModels = d['BuildProgressModels']
        self.weaponDefinitionId = d['WeaponDefinitionId']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.mirroringZ = d['MirroringZ']
        self.model = d['Model']
        self.maxElevationDegrees = d['MaxElevationDegrees']
        self.minAzimuthDegrees = d['MinAzimuthDegrees']
        self.damagedSound = d['DamagedSound']
        self.maxRangeMeters = d['MaxRangeMeters']
        self.blockPairName = d['BlockPairName']
        self.idleRotation = d['IdleRotation']
        self.mirroringY = d['MirroringY']
        self.useModelIntersection = d['UseModelIntersection']

                    
class ConveyorConnector (Block):
    __typevars__ = ['blockPairName', 'buildProgressModels', 'model', 'buildTimeSeconds', 'edgeType']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.blockPairName = d['BlockPairName']
        self.buildProgressModels = d['BuildProgressModels']
        self.model = d['Model']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.edgeType = d['EdgeType']

                    
class InteriorLight (Block):
    __typevars__ = ['resourceSinkGroup', 'lightGlare', 'requiredPowerInput', 'lightFalloff', 'mirroringZ', 'model',
 'damageEffectId', 'mountPoints', 'buildTimeSeconds', 'edgeType', 'damagedSound', 'blockPairName',
 'buildProgressModels', 'lightIntensity', 'lightRadius']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.lightGlare = d['LightGlare']
        self.requiredPowerInput = d['RequiredPowerInput']
        self.lightFalloff = d['LightFalloff']
        self.mirroringZ = d['MirroringZ']
        self.model = d['Model']
        self.damageEffectId = d['DamageEffectId']
        self.mountPoints = d['MountPoints']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.edgeType = d['EdgeType']
        self.damagedSound = d['DamagedSound']
        self.blockPairName = d['BlockPairName']
        self.buildProgressModels = d['BuildProgressModels']
        self.lightIntensity = d['LightIntensity']
        self.lightRadius = d['LightRadius']

                    
class SolarPanel (Block):
    __typevars__ = ['panelOffset', 'twoSidedPanel', 'damageEffectId', 'mountPoints', 'buildTimeSeconds', 'edgeType',
 'buildProgressModels', 'model', 'panelOrientation', 'maxPowerOutput', 'damagedSound',
 'blockPairName', 'resourceSourceGroup']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.panelOffset = d['PanelOffset']
        self.twoSidedPanel = d['TwoSidedPanel']
        self.damageEffectId = d['DamageEffectId']
        self.mountPoints = d['MountPoints']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.edgeType = d['EdgeType']
        self.buildProgressModels = d['BuildProgressModels']
        self.model = d['Model']
        self.panelOrientation = d['PanelOrientation']
        self.maxPowerOutput = d['MaxPowerOutput']
        self.damagedSound = d['DamagedSound']
        self.blockPairName = d['BlockPairName']
        self.resourceSourceGroup = d['ResourceSourceGroup']

                    
class PistonBase (Block):
    __typevars__ = ['topPart', 'damageEffectId', 'mountPoints', 'buildTimeSeconds', 'edgeType', 'public',
 'buildProgressModels', 'primarySound', 'resourceSinkGroup', 'requiredPowerInput', 'mirroringZ',
 'model', 'damagedSound', 'blockPairName', 'mirroringY']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.topPart = d['TopPart']
        self.damageEffectId = d['DamageEffectId']
        self.mountPoints = d['MountPoints']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.edgeType = d['EdgeType']
        self.public = d['Public']
        self.buildProgressModels = d['BuildProgressModels']
        self.primarySound = d['PrimarySound']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.requiredPowerInput = d['RequiredPowerInput']
        self.mirroringZ = d['MirroringZ']
        self.model = d['Model']
        self.damagedSound = d['DamagedSound']
        self.blockPairName = d['BlockPairName']
        self.mirroringY = d['MirroringY']

                    
class Drill (Block):
    __typevars__ = ['damageEffectId', 'mountPoints', 'buildTimeSeconds', 'sensorOffset', 'edgeType', 'sensorRadius',
 'deformationRatio', 'buildProgressModels', 'resourceSinkGroup', 'mirroringZ', 'model',
 'damagedSound', 'blockPairName', 'mirroringY', 'useModelIntersection']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.damageEffectId = d['DamageEffectId']
        self.mountPoints = d['MountPoints']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.sensorOffset = d['SensorOffset']
        self.edgeType = d['EdgeType']
        self.sensorRadius = d['SensorRadius']
        self.deformationRatio = d['DeformationRatio']
        self.buildProgressModels = d['BuildProgressModels']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.mirroringZ = d['MirroringZ']
        self.model = d['Model']
        self.damagedSound = d['DamagedSound']
        self.blockPairName = d['BlockPairName']
        self.mirroringY = d['MirroringY']
        self.useModelIntersection = d['UseModelIntersection']

                    
class Warhead (Block):
    __typevars__ = ['explosionRadius', 'blockPairName', 'buildProgressModels', 'model', 'buildTimeSeconds',
 'warheadExplosionDamage', 'edgeType']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.explosionRadius = d['ExplosionRadius']
        self.blockPairName = d['BlockPairName']
        self.buildProgressModels = d['BuildProgressModels']
        self.model = d['Model']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.warheadExplosionDamage = d['WarheadExplosionDamage']
        self.edgeType = d['EdgeType']

                    
class GravityGenerator (Block):
    __typevars__ = ['resourceSinkGroup', 'requiredPowerInput', 'mirroringZ', 'model', 'damageEffectId', 'mountPoints',
 'buildTimeSeconds', 'edgeType', 'damagedSound', 'blockPairName', 'buildProgressModels',
 'mirroringY', 'sound']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.requiredPowerInput = d['RequiredPowerInput']
        self.mirroringZ = d['MirroringZ']
        self.model = d['Model']
        self.damageEffectId = d['DamageEffectId']
        self.mountPoints = d['MountPoints']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.edgeType = d['EdgeType']
        self.damagedSound = d['DamagedSound']
        self.blockPairName = d['BlockPairName']
        self.buildProgressModels = d['BuildProgressModels']
        self.mirroringY = d['MirroringY']
        self.sound = d['Sound']

                    
class Thrust (Block):
    __typevars__ = ['flameIdleColor', 'forceMagnitude', 'damageEffectId', 'mountPoints', 'buildTimeSeconds',
 'flameGlareSize', 'edgeType', 'center', 'buildProgressModels', 'flameFullColor',
 'flameGlareMaterial', 'flameLengthMaterial', 'primarySound', 'resourceSinkGroup', 'mirroringZ',
 'flameGlareQuerySize', 'model', 'flameVisibilityDistance', 'slowdownFactor', 'minPowerConsumption',
 'flameDamageLengthScale', 'maxPowerConsumption', 'damagedSound', 'blockPairName',
 'flamePointMaterial', 'flameLengthScale']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.flameIdleColor = d['FlameIdleColor']
        self.forceMagnitude = d['ForceMagnitude']
        self.damageEffectId = d['DamageEffectId']
        self.mountPoints = d['MountPoints']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.flameGlareSize = d['FlameGlareSize']
        self.edgeType = d['EdgeType']
        self.center = d['Center']
        self.buildProgressModels = d['BuildProgressModels']
        self.flameFullColor = d['FlameFullColor']
        self.flameGlareMaterial = d['FlameGlareMaterial']
        self.flameLengthMaterial = d['FlameLengthMaterial']
        self.primarySound = d['PrimarySound']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.mirroringZ = d['MirroringZ']
        self.flameGlareQuerySize = d['FlameGlareQuerySize']
        self.model = d['Model']
        self.flameVisibilityDistance = d['FlameVisibilityDistance']
        self.slowdownFactor = d['SlowdownFactor']
        self.minPowerConsumption = d['MinPowerConsumption']
        self.flameDamageLengthScale = d['FlameDamageLengthScale']
        self.maxPowerConsumption = d['MaxPowerConsumption']
        self.damagedSound = d['DamagedSound']
        self.blockPairName = d['BlockPairName']
        self.flamePointMaterial = d['FlamePointMaterial']
        self.flameLengthScale = d['FlameLengthScale']

                    
class CubeBlock (Block):
    __typevars__ = ['buildTimeSeconds', 'edgeType']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.edgeType = d['EdgeType']

                    
class Assembler (Block):
    __typevars__ = ['standbyPowerConsumption', 'inventoryMaxVolume', 'damageEffectId', 'buildTimeSeconds',
 'blueprintClasses', 'edgeType', 'buildProgressModels', 'resourceSinkGroup', 'model',
 'inventorySize', 'operationalPowerConsumption', 'damagedSound', 'blockPairName']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.standbyPowerConsumption = d['StandbyPowerConsumption']
        self.inventoryMaxVolume = d['InventoryMaxVolume']
        self.damageEffectId = d['DamageEffectId']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.blueprintClasses = d['BlueprintClasses']
        self.edgeType = d['EdgeType']
        self.buildProgressModels = d['BuildProgressModels']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.model = d['Model']
        self.inventorySize = d['InventorySize']
        self.operationalPowerConsumption = d['OperationalPowerConsumption']
        self.damagedSound = d['DamagedSound']
        self.blockPairName = d['BlockPairName']

                    
class PistonTop (Block):
    __typevars__ = ['mirroringZ', 'model', 'mountPoints', 'buildTimeSeconds', 'edgeType', 'blockPairName', 'public',
 'buildProgressModels', 'mirroringY', 'useModelIntersection']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.mirroringZ = d['MirroringZ']
        self.model = d['Model']
        self.mountPoints = d['MountPoints']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.edgeType = d['EdgeType']
        self.blockPairName = d['BlockPairName']
        self.public = d['Public']
        self.buildProgressModels = d['BuildProgressModels']
        self.mirroringY = d['MirroringY']
        self.useModelIntersection = d['UseModelIntersection']

                    
class CryoChamber (Block):
    __typevars__ = ['resourceSinkGroup', 'overlayTexture', 'oxygenCapacity', 'mirroringZ', 'model', 'outsideSound',
 'damageEffectId', 'insideSound', 'mountPoints', 'buildTimeSeconds', 'characterAnimation',
 'edgeType', 'damagedSound', 'idlePowerConsumption', 'blockPairName', 'buildProgressModels',
 'enableFirstPerson', 'isPressurized', 'primarySound', 'mirroringY']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.overlayTexture = d['OverlayTexture']
        self.oxygenCapacity = d['OxygenCapacity']
        self.mirroringZ = d['MirroringZ']
        self.model = d['Model']
        self.outsideSound = d['OutsideSound']
        self.damageEffectId = d['DamageEffectId']
        self.insideSound = d['InsideSound']
        self.mountPoints = d['MountPoints']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.characterAnimation = d['CharacterAnimation']
        self.edgeType = d['EdgeType']
        self.damagedSound = d['DamagedSound']
        self.idlePowerConsumption = d['IdlePowerConsumption']
        self.blockPairName = d['BlockPairName']
        self.buildProgressModels = d['BuildProgressModels']
        self.enableFirstPerson = d['EnableFirstPerson']
        self.isPressurized = d['IsPressurized']
        self.primarySound = d['PrimarySound']
        self.mirroringY = d['MirroringY']

                    
class LaserAntenna (Block):
    __typevars__ = ['maxAzimuthDegrees', 'minElevationDegrees', 'damageEffectId', 'mountPoints', 'buildTimeSeconds',
 'edgeType', 'buildProgressModels', 'maxRange', 'powerInputLasing', 'resourceSinkGroup',
 'rotationRate', 'model', 'maxElevationDegrees', 'minAzimuthDegrees', 'damagedSound',
 'blockPairName', 'powerInputIdle', 'powerInputTurning', 'mirroringY', 'requireLineOfSight']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.maxAzimuthDegrees = d['MaxAzimuthDegrees']
        self.minElevationDegrees = d['MinElevationDegrees']
        self.damageEffectId = d['DamageEffectId']
        self.mountPoints = d['MountPoints']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.edgeType = d['EdgeType']
        self.buildProgressModels = d['BuildProgressModels']
        self.maxRange = d['MaxRange']
        self.powerInputLasing = d['PowerInputLasing']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.rotationRate = d['RotationRate']
        self.model = d['Model']
        self.maxElevationDegrees = d['MaxElevationDegrees']
        self.minAzimuthDegrees = d['MinAzimuthDegrees']
        self.damagedSound = d['DamagedSound']
        self.blockPairName = d['BlockPairName']
        self.powerInputIdle = d['PowerInputIdle']
        self.powerInputTurning = d['PowerInputTurning']
        self.mirroringY = d['MirroringY']
        self.requireLineOfSight = d['RequireLineOfSight']

                    
class Passage (Block):
    __typevars__ = ['mirroringZ', 'model', 'mountPoints', 'buildTimeSeconds', 'edgeType', 'blockPairName',
 'buildProgressModels', 'mirroringY']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.mirroringZ = d['MirroringZ']
        self.model = d['Model']
        self.mountPoints = d['MountPoints']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.edgeType = d['EdgeType']
        self.blockPairName = d['BlockPairName']
        self.buildProgressModels = d['BuildProgressModels']
        self.mirroringY = d['MirroringY']

                    
class SpaceBall (Block):
    __typevars__ = ['requiredPowerInput', 'buildProgressModels', 'model', 'maxVirtualMass', 'buildTimeSeconds', 'edgeType']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.requiredPowerInput = d['RequiredPowerInput']
        self.buildProgressModels = d['BuildProgressModels']
        self.model = d['Model']
        self.maxVirtualMass = d['MaxVirtualMass']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.edgeType = d['EdgeType']

                    
class TerminalBlock (Block):
    __typevars__ = ['blockPairName', 'buildProgressModels', 'mirroringZ', 'model', 'mountPoints', 'buildTimeSeconds',
 'edgeType']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.blockPairName = d['BlockPairName']
        self.buildProgressModels = d['BuildProgressModels']
        self.mirroringZ = d['MirroringZ']
        self.model = d['Model']
        self.mountPoints = d['MountPoints']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.edgeType = d['EdgeType']

                    
class CameraBlock (Block):
    __typevars__ = ['overlayTexture', 'damageEffectId', 'mountPoints', 'buildTimeSeconds', 'edgeType', 'public',
 'buildProgressModels', 'minFov', 'resourceSinkGroup', 'requiredPowerInput', 'mirroringZ', 'model',
 'damagedSound', 'maxFov', 'blockPairName', 'mirroringY']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.overlayTexture = d['OverlayTexture']
        self.damageEffectId = d['DamageEffectId']
        self.mountPoints = d['MountPoints']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.edgeType = d['EdgeType']
        self.public = d['Public']
        self.buildProgressModels = d['BuildProgressModels']
        self.minFov = d['MinFov']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.requiredPowerInput = d['RequiredPowerInput']
        self.mirroringZ = d['MirroringZ']
        self.model = d['Model']
        self.damagedSound = d['DamagedSound']
        self.maxFov = d['MaxFov']
        self.blockPairName = d['BlockPairName']
        self.mirroringY = d['MirroringY']

                    
class OxygenFarm (Block):
    __typevars__ = ['resourceSinkGroup', 'panelOffset', 'producedGas', 'twoSidedPanel', 'model', 'damageEffectId',
 'mountPoints', 'buildTimeSeconds', 'panelOrientation', 'edgeType', 'operationalPowerConsumption',
 'damagedSound', 'center', 'blockPairName', 'buildProgressModels', 'resourceSourceGroup']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.panelOffset = d['PanelOffset']
        self.producedGas = d['ProducedGas']
        self.twoSidedPanel = d['TwoSidedPanel']
        self.model = d['Model']
        self.damageEffectId = d['DamageEffectId']
        self.mountPoints = d['MountPoints']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.panelOrientation = d['PanelOrientation']
        self.edgeType = d['EdgeType']
        self.operationalPowerConsumption = d['OperationalPowerConsumption']
        self.damagedSound = d['DamagedSound']
        self.center = d['Center']
        self.blockPairName = d['BlockPairName']
        self.buildProgressModels = d['BuildProgressModels']
        self.resourceSourceGroup = d['ResourceSourceGroup']

                    
class Projector (Block):
    __typevars__ = ['resourceSinkGroup', 'requiredPowerInput', 'model', 'damageEffectId', 'mountPoints',
 'buildTimeSeconds', 'edgeType', 'damagedSound', 'blockPairName', 'public', 'buildProgressModels']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.requiredPowerInput = d['RequiredPowerInput']
        self.model = d['Model']
        self.damageEffectId = d['DamageEffectId']
        self.mountPoints = d['MountPoints']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.edgeType = d['EdgeType']
        self.damagedSound = d['DamagedSound']
        self.blockPairName = d['BlockPairName']
        self.public = d['Public']
        self.buildProgressModels = d['BuildProgressModels']

                    
class AirtightSlideDoor (Block):
    __typevars__ = ['resourceSinkGroup', 'openingSpeed', 'mirroringZ', 'model', 'damageEffectId', 'powerConsumptionIdle',
 'powerConsumptionMoving', 'mountPoints', 'buildTimeSeconds', 'edgeType', 'damagedSound', 'center',
 'blockPairName', 'disassembleRatio', 'buildProgressModels', 'mirroringY', 'sound',
 'subpartMovementDistance']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.openingSpeed = d['OpeningSpeed']
        self.mirroringZ = d['MirroringZ']
        self.model = d['Model']
        self.damageEffectId = d['DamageEffectId']
        self.powerConsumptionIdle = d['PowerConsumptionIdle']
        self.powerConsumptionMoving = d['PowerConsumptionMoving']
        self.mountPoints = d['MountPoints']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.edgeType = d['EdgeType']
        self.damagedSound = d['DamagedSound']
        self.center = d['Center']
        self.blockPairName = d['BlockPairName']
        self.disassembleRatio = d['DisassembleRatio']
        self.buildProgressModels = d['BuildProgressModels']
        self.mirroringY = d['MirroringY']
        self.sound = d['Sound']
        self.subpartMovementDistance = d['SubpartMovementDistance']

                    
class DebugSphere2 (Block):
    __typevars__ = ['requiredPowerInput', 'model', 'mountPoints', 'buildTimeSeconds', 'edgeType', 'public',
 'buildProgressModels']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.requiredPowerInput = d['RequiredPowerInput']
        self.model = d['Model']
        self.mountPoints = d['MountPoints']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.edgeType = d['EdgeType']
        self.public = d['Public']
        self.buildProgressModels = d['BuildProgressModels']

                    
class OreDetector (Block):
    __typevars__ = ['resourceSinkGroup', 'mirroringZ', 'model', 'damageEffectId', 'mountPoints', 'buildTimeSeconds',
 'edgeType', 'maximumRange', 'damagedSound', 'blockPairName', 'buildProgressModels', 'mirroringY']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.mirroringZ = d['MirroringZ']
        self.model = d['Model']
        self.damageEffectId = d['DamageEffectId']
        self.mountPoints = d['MountPoints']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.edgeType = d['EdgeType']
        self.maximumRange = d['MaximumRange']
        self.damagedSound = d['DamagedSound']
        self.blockPairName = d['BlockPairName']
        self.buildProgressModels = d['BuildProgressModels']
        self.mirroringY = d['MirroringY']

                    
class MyProgrammableBlock (Block):
    __typevars__ = ['resourceSinkGroup', 'mirroringZ', 'model', 'damageEffectId', 'buildTimeSeconds', 'mountPoints',
 'edgeType', 'damagedSound', 'blockPairName', 'public', 'buildProgressModels']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.mirroringZ = d['MirroringZ']
        self.model = d['Model']
        self.damageEffectId = d['DamageEffectId']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.mountPoints = d['MountPoints']
        self.edgeType = d['EdgeType']
        self.damagedSound = d['DamagedSound']
        self.blockPairName = d['BlockPairName']
        self.public = d['Public']
        self.buildProgressModels = d['BuildProgressModels']

                    
class Cockpit (Block):
    __typevars__ = ['enableBuilderCockpit', 'damageEffectId', 'mountPoints', 'buildTimeSeconds', 'edgeType',
 'buildProgressModels', 'enableFirstPerson', 'enableShipControl', 'primarySound', 'mirroringZ',
 'model', 'characterAnimation', 'damagedSound', 'blockPairName', 'mirroringY']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.enableBuilderCockpit = d['EnableBuilderCockpit']
        self.damageEffectId = d['DamageEffectId']
        self.mountPoints = d['MountPoints']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.edgeType = d['EdgeType']
        self.buildProgressModels = d['BuildProgressModels']
        self.enableFirstPerson = d['EnableFirstPerson']
        self.enableShipControl = d['EnableShipControl']
        self.primarySound = d['PrimarySound']
        self.mirroringZ = d['MirroringZ']
        self.model = d['Model']
        self.characterAnimation = d['CharacterAnimation']
        self.damagedSound = d['DamagedSound']
        self.blockPairName = d['BlockPairName']
        self.mirroringY = d['MirroringY']

                    
class UpgradeModule (Block):
    __typevars__ = ['mirroringZ', 'model', 'upgrades', 'mirroringX', 'damageEffectId', 'mountPoints', 'edgeType',
 'damagedSound', 'blockPairName', 'buildProgressModels']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.mirroringZ = d['MirroringZ']
        self.model = d['Model']
        self.upgrades = d['Upgrades']
        self.mirroringX = d['MirroringX']
        self.damageEffectId = d['DamageEffectId']
        self.mountPoints = d['MountPoints']
        self.edgeType = d['EdgeType']
        self.damagedSound = d['DamagedSound']
        self.blockPairName = d['BlockPairName']
        self.buildProgressModels = d['BuildProgressModels']

                    
class MedicalRoom (Block):
    __typevars__ = ['resourceSinkGroup', 'model', 'damageEffectId', 'mountPoints', 'buildTimeSeconds', 'idleSound',
 'edgeType', 'damagedSound', 'blockPairName', 'buildProgressModels', 'progressSound']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.model = d['Model']
        self.damageEffectId = d['DamageEffectId']
        self.mountPoints = d['MountPoints']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.idleSound = d['IdleSound']
        self.edgeType = d['EdgeType']
        self.damagedSound = d['DamagedSound']
        self.blockPairName = d['BlockPairName']
        self.buildProgressModels = d['BuildProgressModels']
        self.progressSound = d['ProgressSound']

                    
class JumpDrive (Block):
    __typevars__ = ['resourceSinkGroup', 'requiredPowerInput', 'mirroringZ', 'model', 'damageEffectId', 'mountPoints',
 'buildTimeSeconds', 'powerNeededForJump', 'edgeType', 'damagedSound', 'maxJumpDistance',
 'blockPairName', 'buildProgressModels', 'maxJumpMass', 'mirroringY']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.requiredPowerInput = d['RequiredPowerInput']
        self.mirroringZ = d['MirroringZ']
        self.model = d['Model']
        self.damageEffectId = d['DamageEffectId']
        self.mountPoints = d['MountPoints']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.powerNeededForJump = d['PowerNeededForJump']
        self.edgeType = d['EdgeType']
        self.damagedSound = d['DamagedSound']
        self.maxJumpDistance = d['MaxJumpDistance']
        self.blockPairName = d['BlockPairName']
        self.buildProgressModels = d['BuildProgressModels']
        self.maxJumpMass = d['MaxJumpMass']
        self.mirroringY = d['MirroringY']

                    
class DebugSphere1 (Block):
    __typevars__ = ['requiredPowerInput', 'model', 'mountPoints', 'buildTimeSeconds', 'edgeType', 'public',
 'buildProgressModels']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.requiredPowerInput = d['RequiredPowerInput']
        self.model = d['Model']
        self.mountPoints = d['MountPoints']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.edgeType = d['EdgeType']
        self.public = d['Public']
        self.buildProgressModels = d['BuildProgressModels']

                    
class ShipGrinder (Block):
    __typevars__ = ['mirroringZ', 'model', 'damageEffectId', 'mountPoints', 'buildTimeSeconds', 'edgeType',
 'damagedSound', 'center', 'blockPairName', 'public', 'buildProgressModels', 'useModelIntersection']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.mirroringZ = d['MirroringZ']
        self.model = d['Model']
        self.damageEffectId = d['DamageEffectId']
        self.mountPoints = d['MountPoints']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.edgeType = d['EdgeType']
        self.damagedSound = d['DamagedSound']
        self.center = d['Center']
        self.blockPairName = d['BlockPairName']
        self.public = d['Public']
        self.buildProgressModels = d['BuildProgressModels']
        self.useModelIntersection = d['UseModelIntersection']

                    
class SmallMissileLauncherReload (Block):
    __typevars__ = ['resourceSinkGroup', 'model', 'inventoryMaxVolume', 'damageEffectId', 'mountPoints',
 'buildTimeSeconds', 'damagedSound', 'center', 'blockPairName', 'buildProgressModels',
 'weaponDefinitionId']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.model = d['Model']
        self.inventoryMaxVolume = d['InventoryMaxVolume']
        self.damageEffectId = d['DamageEffectId']
        self.mountPoints = d['MountPoints']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.damagedSound = d['DamagedSound']
        self.center = d['Center']
        self.blockPairName = d['BlockPairName']
        self.buildProgressModels = d['BuildProgressModels']
        self.weaponDefinitionId = d['WeaponDefinitionId']

                    
class BatteryBlock (Block):
    __typevars__ = ['damageEffectId', 'initialStoredPowerRatio', 'buildTimeSeconds', 'edgeType', 'public',
 'buildProgressModels', 'resourceSinkGroup', 'requiredPowerInput', 'model', 'maxStoredPower',
 'inventorySize', 'maxPowerOutput', 'damagedSound', 'blockPairName', 'resourceSourceGroup']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.damageEffectId = d['DamageEffectId']
        self.initialStoredPowerRatio = d['InitialStoredPowerRatio']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.edgeType = d['EdgeType']
        self.public = d['Public']
        self.buildProgressModels = d['BuildProgressModels']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.requiredPowerInput = d['RequiredPowerInput']
        self.model = d['Model']
        self.maxStoredPower = d['MaxStoredPower']
        self.inventorySize = d['InventorySize']
        self.maxPowerOutput = d['MaxPowerOutput']
        self.damagedSound = d['DamagedSound']
        self.blockPairName = d['BlockPairName']
        self.resourceSourceGroup = d['ResourceSourceGroup']

                    
class InteriorTurret (Block):
    __typevars__ = ['overlayTexture', 'maxAzimuthDegrees', 'minElevationDegrees', 'inventoryMaxVolume', 'damageEffectId',
 'elevationSpeed', 'mountPoints', 'buildTimeSeconds', 'rotationSpeed', 'edgeType',
 'buildProgressModels', 'weaponDefinitionId', 'resourceSinkGroup', 'mirroringZ', 'model',
 'maxElevationDegrees', 'minAzimuthDegrees', 'damagedSound', 'maxRangeMeters', 'blockPairName',
 'idleRotation', 'mirroringY', 'useModelIntersection']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.overlayTexture = d['OverlayTexture']
        self.maxAzimuthDegrees = d['MaxAzimuthDegrees']
        self.minElevationDegrees = d['MinElevationDegrees']
        self.inventoryMaxVolume = d['InventoryMaxVolume']
        self.damageEffectId = d['DamageEffectId']
        self.elevationSpeed = d['ElevationSpeed']
        self.mountPoints = d['MountPoints']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.rotationSpeed = d['RotationSpeed']
        self.edgeType = d['EdgeType']
        self.buildProgressModels = d['BuildProgressModels']
        self.weaponDefinitionId = d['WeaponDefinitionId']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.mirroringZ = d['MirroringZ']
        self.model = d['Model']
        self.maxElevationDegrees = d['MaxElevationDegrees']
        self.minAzimuthDegrees = d['MinAzimuthDegrees']
        self.damagedSound = d['DamagedSound']
        self.maxRangeMeters = d['MaxRangeMeters']
        self.blockPairName = d['BlockPairName']
        self.idleRotation = d['IdleRotation']
        self.mirroringY = d['MirroringY']
        self.useModelIntersection = d['UseModelIntersection']

                    
class AirVent (Block):
    __typevars__ = ['ventilationCapacityPerSecond', 'standbyPowerConsumption', 'depressurizeSound', 'damageEffectId',
 'mountPoints', 'buildTimeSeconds', 'idleSound', 'edgeType', 'pressurizeSound',
 'buildProgressModels', 'resourceSinkGroup', 'mirroringZ', 'model', 'operationalPowerConsumption',
 'damagedSound', 'blockPairName', 'resourceSourceGroup', 'mirroringY']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.ventilationCapacityPerSecond = d['VentilationCapacityPerSecond']
        self.standbyPowerConsumption = d['StandbyPowerConsumption']
        self.depressurizeSound = d['DepressurizeSound']
        self.damageEffectId = d['DamageEffectId']
        self.mountPoints = d['MountPoints']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.idleSound = d['IdleSound']
        self.edgeType = d['EdgeType']
        self.pressurizeSound = d['PressurizeSound']
        self.buildProgressModels = d['BuildProgressModels']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.mirroringZ = d['MirroringZ']
        self.model = d['Model']
        self.operationalPowerConsumption = d['OperationalPowerConsumption']
        self.damagedSound = d['DamagedSound']
        self.blockPairName = d['BlockPairName']
        self.resourceSourceGroup = d['ResourceSourceGroup']
        self.mirroringY = d['MirroringY']

                    
class ExtendedPistonBase (Block):
    __typevars__ = ['topPart', 'damageEffectId', 'mountPoints', 'buildTimeSeconds', 'edgeType', 'center',
 'buildProgressModels', 'primarySound', 'resourceSinkGroup', 'requiredPowerInput', 'mirroringZ',
 'model', 'damagedSound', 'blockPairName', 'mirroringY']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.topPart = d['TopPart']
        self.damageEffectId = d['DamageEffectId']
        self.mountPoints = d['MountPoints']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.edgeType = d['EdgeType']
        self.center = d['Center']
        self.buildProgressModels = d['BuildProgressModels']
        self.primarySound = d['PrimarySound']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.requiredPowerInput = d['RequiredPowerInput']
        self.mirroringZ = d['MirroringZ']
        self.model = d['Model']
        self.damagedSound = d['DamagedSound']
        self.blockPairName = d['BlockPairName']
        self.mirroringY = d['MirroringY']

                    
class AirtightHangarDoor (Block):
    __typevars__ = ['resourceSinkGroup', 'openingSpeed', 'mirroringZ', 'model', 'damageEffectId', 'powerConsumptionIdle',
 'powerConsumptionMoving', 'mountPoints', 'buildTimeSeconds', 'edgeType', 'damagedSound', 'center',
 'blockPairName', 'buildProgressModels', 'mirroringY', 'sound', 'subpartMovementDistance']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.openingSpeed = d['OpeningSpeed']
        self.mirroringZ = d['MirroringZ']
        self.model = d['Model']
        self.damageEffectId = d['DamageEffectId']
        self.powerConsumptionIdle = d['PowerConsumptionIdle']
        self.powerConsumptionMoving = d['PowerConsumptionMoving']
        self.mountPoints = d['MountPoints']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.edgeType = d['EdgeType']
        self.damagedSound = d['DamagedSound']
        self.center = d['Center']
        self.blockPairName = d['BlockPairName']
        self.buildProgressModels = d['BuildProgressModels']
        self.mirroringY = d['MirroringY']
        self.sound = d['Sound']
        self.subpartMovementDistance = d['SubpartMovementDistance']

                    
class Conveyor (Block):
    __typevars__ = ['mirroringZ', 'model', 'damageEffectId', 'buildTimeSeconds', 'edgeType', 'damagedSound',
 'blockPairName', 'buildProgressModels']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.mirroringZ = d['MirroringZ']
        self.model = d['Model']
        self.damageEffectId = d['DamageEffectId']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.edgeType = d['EdgeType']
        self.damagedSound = d['DamagedSound']
        self.blockPairName = d['BlockPairName']
        self.buildProgressModels = d['BuildProgressModels']

                    
class SensorBlock (Block):
    __typevars__ = ['resourceSinkGroup', 'mirroringZ', 'model', 'damageEffectId', 'mountPoints', 'buildTimeSeconds',
 'edgeType', 'damagedSound', 'blockPairName', 'buildProgressModels', 'maxRange', 'mirroringY']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.mirroringZ = d['MirroringZ']
        self.model = d['Model']
        self.damageEffectId = d['DamageEffectId']
        self.mountPoints = d['MountPoints']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.edgeType = d['EdgeType']
        self.damagedSound = d['DamagedSound']
        self.blockPairName = d['BlockPairName']
        self.buildProgressModels = d['BuildProgressModels']
        self.maxRange = d['MaxRange']
        self.mirroringY = d['MirroringY']

                    
class TextPanel (Block):
    __typevars__ = ['resourceSinkGroup', 'requiredPowerInput', 'mirroringZ', 'model', 'mountPoints', 'buildTimeSeconds',
 'edgeType', 'blockPairName', 'buildProgressModels']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.requiredPowerInput = d['RequiredPowerInput']
        self.mirroringZ = d['MirroringZ']
        self.model = d['Model']
        self.mountPoints = d['MountPoints']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.edgeType = d['EdgeType']
        self.blockPairName = d['BlockPairName']
        self.buildProgressModels = d['BuildProgressModels']

                    
class GravityGeneratorSphere (Block):
    __typevars__ = ['resourceSinkGroup', 'mirroringZ', 'model', 'damageEffectId', 'minRadius', 'mountPoints',
 'buildTimeSeconds', 'maxRadius', 'edgeType', 'consumptionPower', 'damagedSound', 'blockPairName',
 'buildProgressModels', 'basePowerInput', 'mirroringY', 'sound']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.mirroringZ = d['MirroringZ']
        self.model = d['Model']
        self.damageEffectId = d['DamageEffectId']
        self.minRadius = d['MinRadius']
        self.mountPoints = d['MountPoints']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.maxRadius = d['MaxRadius']
        self.edgeType = d['EdgeType']
        self.consumptionPower = d['ConsumptionPower']
        self.damagedSound = d['DamagedSound']
        self.blockPairName = d['BlockPairName']
        self.buildProgressModels = d['BuildProgressModels']
        self.basePowerInput = d['BasePowerInput']
        self.mirroringY = d['MirroringY']
        self.sound = d['Sound']

                    
class Gyro (Block):
    __typevars__ = ['forceMagnitude', 'damageEffectId', 'mountPoints', 'buildTimeSeconds', 'edgeType',
 'buildProgressModels', 'resourceSinkGroup', 'requiredPowerInput', 'mirroringZ', 'model',
 'damagedSound', 'blockPairName', 'mirroringY']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.forceMagnitude = d['ForceMagnitude']
        self.damageEffectId = d['DamageEffectId']
        self.mountPoints = d['MountPoints']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.edgeType = d['EdgeType']
        self.buildProgressModels = d['BuildProgressModels']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.requiredPowerInput = d['RequiredPowerInput']
        self.mirroringZ = d['MirroringZ']
        self.model = d['Model']
        self.damagedSound = d['DamagedSound']
        self.blockPairName = d['BlockPairName']
        self.mirroringY = d['MirroringY']

                    
class MotorRotor (Block):
    __typevars__ = ['mirroringZ', 'model', 'mountPoints', 'buildTimeSeconds', 'edgeType', 'blockPairName',
 'buildProgressModels', 'mirroringY', 'useModelIntersection']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.mirroringZ = d['MirroringZ']
        self.model = d['Model']
        self.mountPoints = d['MountPoints']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.edgeType = d['EdgeType']
        self.blockPairName = d['BlockPairName']
        self.buildProgressModels = d['BuildProgressModels']
        self.mirroringY = d['MirroringY']
        self.useModelIntersection = d['UseModelIntersection']

                    
class MotorSuspension (Block):
    __typevars__ = ['damageEffectId', 'rotorPart', 'mountPoints', 'buildTimeSeconds', 'edgeType', 'buildProgressModels',
 'propulsionForce', 'primarySound', 'resourceSinkGroup', 'requiredPowerInput', 'mirroringZ',
 'model', 'maxForceMagnitude', 'maxHeight', 'damagedSound', 'blockPairName', 'minHeight',
 'mirroringY', 'useModelIntersection']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.damageEffectId = d['DamageEffectId']
        self.rotorPart = d['RotorPart']
        self.mountPoints = d['MountPoints']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.edgeType = d['EdgeType']
        self.buildProgressModels = d['BuildProgressModels']
        self.propulsionForce = d['PropulsionForce']
        self.primarySound = d['PrimarySound']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.requiredPowerInput = d['RequiredPowerInput']
        self.mirroringZ = d['MirroringZ']
        self.model = d['Model']
        self.maxForceMagnitude = d['MaxForceMagnitude']
        self.maxHeight = d['MaxHeight']
        self.damagedSound = d['DamagedSound']
        self.blockPairName = d['BlockPairName']
        self.minHeight = d['MinHeight']
        self.mirroringY = d['MirroringY']
        self.useModelIntersection = d['UseModelIntersection']

                    
class ButtonPanel (Block):
    __typevars__ = ['unassignedButtonColor', 'buttonCount', 'damageEffectId', 'buttonColors', 'mountPoints',
 'buildTimeSeconds', 'edgeType', 'buildProgressModels', 'resourceSinkGroup', 'mirroringZ', 'model',
 'buttonSymbols', 'damagedSound', 'blockPairName', 'mirroringY']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.unassignedButtonColor = d['UnassignedButtonColor']
        self.buttonCount = d['ButtonCount']
        self.damageEffectId = d['DamageEffectId']
        self.buttonColors = d['ButtonColors']
        self.mountPoints = d['MountPoints']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.edgeType = d['EdgeType']
        self.buildProgressModels = d['BuildProgressModels']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.mirroringZ = d['MirroringZ']
        self.model = d['Model']
        self.buttonSymbols = d['ButtonSymbols']
        self.damagedSound = d['DamagedSound']
        self.blockPairName = d['BlockPairName']
        self.mirroringY = d['MirroringY']

                    
class Decoy (Block):
    __typevars__ = ['blockPairName', 'public', 'buildProgressModels', 'model', 'buildTimeSeconds', 'edgeType']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.blockPairName = d['BlockPairName']
        self.public = d['Public']
        self.buildProgressModels = d['BuildProgressModels']
        self.model = d['Model']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.edgeType = d['EdgeType']

                    
class SmallMissileLauncher (Block):
    __typevars__ = ['resourceSinkGroup', 'model', 'inventoryMaxVolume', 'damageEffectId', 'mountPoints',
 'buildTimeSeconds', 'edgeType', 'damagedSound', 'center', 'blockPairName', 'buildProgressModels',
 'weaponDefinitionId']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.model = d['Model']
        self.inventoryMaxVolume = d['InventoryMaxVolume']
        self.damageEffectId = d['DamageEffectId']
        self.mountPoints = d['MountPoints']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.edgeType = d['EdgeType']
        self.damagedSound = d['DamagedSound']
        self.center = d['Center']
        self.blockPairName = d['BlockPairName']
        self.buildProgressModels = d['BuildProgressModels']
        self.weaponDefinitionId = d['WeaponDefinitionId']

                    
class RadioAntenna (Block):
    __typevars__ = ['resourceSinkGroup', 'model', 'damageEffectId', 'mountPoints', 'buildTimeSeconds', 'edgeType',
 'damagedSound', 'blockPairName', 'buildProgressModels', 'mirroringY']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.model = d['Model']
        self.damageEffectId = d['DamageEffectId']
        self.mountPoints = d['MountPoints']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.edgeType = d['EdgeType']
        self.damagedSound = d['DamagedSound']
        self.blockPairName = d['BlockPairName']
        self.buildProgressModels = d['BuildProgressModels']
        self.mirroringY = d['MirroringY']

                    
class Beacon (Block):
    __typevars__ = ['resourceSinkGroup', 'model', 'damageEffectId', 'buildTimeSeconds', 'edgeType', 'damagedSound',
 'blockPairName', 'buildProgressModels']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.model = d['Model']
        self.damageEffectId = d['DamageEffectId']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.edgeType = d['EdgeType']
        self.damagedSound = d['DamagedSound']
        self.blockPairName = d['BlockPairName']
        self.buildProgressModels = d['BuildProgressModels']

                    
class ConveyorSorter (Block):
    __typevars__ = ['resourceSinkGroup', 'mirroringZ', 'model', 'damageEffectId', 'buildTimeSeconds', 'inventorySize',
 'edgeType', 'damagedSound', 'blockPairName', 'buildProgressModels', 'powerInput', 'mirroringY']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.mirroringZ = d['MirroringZ']
        self.model = d['Model']
        self.damageEffectId = d['DamageEffectId']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.inventorySize = d['InventorySize']
        self.edgeType = d['EdgeType']
        self.damagedSound = d['DamagedSound']
        self.blockPairName = d['BlockPairName']
        self.buildProgressModels = d['BuildProgressModels']
        self.powerInput = d['PowerInput']
        self.mirroringY = d['MirroringY']

                    
class OxygenGenerator (Block):
    __typevars__ = ['standbyPowerConsumption', 'inventoryMaxVolume', 'damageEffectId', 'producedGases', 'mountPoints',
 'buildTimeSeconds', 'blueprintClasses', 'idleSound', 'edgeType', 'buildProgressModels',
 'resourceSinkGroup', 'mirroringZ', 'model', 'iceConsumptionPerSecond', 'generateSound',
 'inventorySize', 'operationalPowerConsumption', 'damagedSound', 'blockPairName',
 'resourceSourceGroup', 'mirroringY']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.standbyPowerConsumption = d['StandbyPowerConsumption']
        self.inventoryMaxVolume = d['InventoryMaxVolume']
        self.damageEffectId = d['DamageEffectId']
        self.producedGases = d['ProducedGases']
        self.mountPoints = d['MountPoints']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.blueprintClasses = d['BlueprintClasses']
        self.idleSound = d['IdleSound']
        self.edgeType = d['EdgeType']
        self.buildProgressModels = d['BuildProgressModels']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.mirroringZ = d['MirroringZ']
        self.model = d['Model']
        self.iceConsumptionPerSecond = d['IceConsumptionPerSecond']
        self.generateSound = d['GenerateSound']
        self.inventorySize = d['InventorySize']
        self.operationalPowerConsumption = d['OperationalPowerConsumption']
        self.damagedSound = d['DamagedSound']
        self.blockPairName = d['BlockPairName']
        self.resourceSourceGroup = d['ResourceSourceGroup']
        self.mirroringY = d['MirroringY']

                    
class VirtualMass (Block):
    __typevars__ = ['resourceSinkGroup', 'requiredPowerInput', 'model', 'damageEffectId', 'buildTimeSeconds', 'edgeType',
 'damagedSound', 'blockPairName', 'public', 'buildProgressModels', 'virtualMass']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.requiredPowerInput = d['RequiredPowerInput']
        self.model = d['Model']
        self.damageEffectId = d['DamageEffectId']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.edgeType = d['EdgeType']
        self.damagedSound = d['DamagedSound']
        self.blockPairName = d['BlockPairName']
        self.public = d['Public']
        self.buildProgressModels = d['BuildProgressModels']
        self.virtualMass = d['VirtualMass']

                    
class DebugSphere3 (Block):
    __typevars__ = ['requiredPowerInput', 'model', 'mountPoints', 'buildTimeSeconds', 'edgeType', 'public',
 'buildProgressModels']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.requiredPowerInput = d['RequiredPowerInput']
        self.model = d['Model']
        self.mountPoints = d['MountPoints']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.edgeType = d['EdgeType']
        self.public = d['Public']
        self.buildProgressModels = d['BuildProgressModels']

                    
class TimerBlock (Block):
    __typevars__ = ['resourceSinkGroup', 'blockPairName', 'buildProgressModels', 'model', 'buildTimeSeconds', 'edgeType']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.blockPairName = d['BlockPairName']
        self.buildProgressModels = d['BuildProgressModels']
        self.model = d['Model']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.edgeType = d['EdgeType']

                    
class Reactor (Block):
    __typevars__ = ['damageEffectId', 'mountPoints', 'buildTimeSeconds', 'edgeType', 'buildProgressModels', 'fuelId',
 'primarySound', 'mirroringZ', 'model', 'inventorySize', 'maxPowerOutput', 'damagedSound',
 'blockPairName', 'resourceSourceGroup', 'mirroringY']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.damageEffectId = d['DamageEffectId']
        self.mountPoints = d['MountPoints']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.edgeType = d['EdgeType']
        self.buildProgressModels = d['BuildProgressModels']
        self.fuelId = d['FuelId']
        self.primarySound = d['PrimarySound']
        self.mirroringZ = d['MirroringZ']
        self.model = d['Model']
        self.inventorySize = d['InventorySize']
        self.maxPowerOutput = d['MaxPowerOutput']
        self.damagedSound = d['DamagedSound']
        self.blockPairName = d['BlockPairName']
        self.resourceSourceGroup = d['ResourceSourceGroup']
        self.mirroringY = d['MirroringY']

                    
class MotorAdvancedStator (Block):
    __typevars__ = ['damageEffectId', 'rotorPart', 'mountPoints', 'buildTimeSeconds', 'rotorDisplacementMin', 'edgeType',
 'public', 'buildProgressModels', 'rotorDisplacementMax', 'primarySound', 'resourceSinkGroup',
 'requiredPowerInput', 'mirroringZ', 'model', 'maxForceMagnitude', 'rotorDisplacementInModel',
 'damagedSound', 'blockPairName', 'mirroringY']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.damageEffectId = d['DamageEffectId']
        self.rotorPart = d['RotorPart']
        self.mountPoints = d['MountPoints']
        self.buildTimeSeconds = d['BuildTimeSeconds']
        self.rotorDisplacementMin = d['RotorDisplacementMin']
        self.edgeType = d['EdgeType']
        self.public = d['Public']
        self.buildProgressModels = d['BuildProgressModels']
        self.rotorDisplacementMax = d['RotorDisplacementMax']
        self.primarySound = d['PrimarySound']
        self.resourceSinkGroup = d['ResourceSinkGroup']
        self.requiredPowerInput = d['RequiredPowerInput']
        self.mirroringZ = d['MirroringZ']
        self.model = d['Model']
        self.maxForceMagnitude = d['MaxForceMagnitude']
        self.rotorDisplacementInModel = d['RotorDisplacementInModel']
        self.damagedSound = d['DamagedSound']
        self.blockPairName = d['BlockPairName']
        self.mirroringY = d['MirroringY']

__all__ = ['Block', 'MotorAdvancedRotor', 'SmallGatlingGun', 'LargeMissileTurret', 'OxygenTank',
 'ReflectorLight', 'CargoContainer', 'Wheel', 'MergeBlock', 'MotorStator', 'Refinery',
 'RemoteControl', 'ShipConnector', 'Door', 'ShipWelder', 'SoundBlock', 'Collector', 'LandingGear',
 'LargeGatlingTurret', 'ConveyorConnector', 'InteriorLight', 'SolarPanel', 'PistonBase', 'Drill',
 'Warhead', 'GravityGenerator', 'Thrust', 'CubeBlock', 'Assembler', 'PistonTop', 'CryoChamber',
 'LaserAntenna', 'Passage', 'SpaceBall', 'TerminalBlock', 'CameraBlock', 'OxygenFarm', 'Projector',
 'AirtightSlideDoor', 'DebugSphere2', 'OreDetector', 'MyProgrammableBlock', 'Cockpit',
 'UpgradeModule', 'MedicalRoom', 'JumpDrive', 'DebugSphere1', 'ShipGrinder',
 'SmallMissileLauncherReload', 'BatteryBlock', 'InteriorTurret', 'AirVent', 'ExtendedPistonBase',
 'AirtightHangarDoor', 'Conveyor', 'SensorBlock', 'TextPanel', 'GravityGeneratorSphere', 'Gyro',
 'MotorRotor', 'MotorSuspension', 'ButtonPanel', 'Decoy', 'SmallMissileLauncher', 'RadioAntenna',
 'Beacon', 'ConveyorSorter', 'OxygenGenerator', 'VirtualMass', 'DebugSphere3', 'TimerBlock',
 'Reactor', 'MotorAdvancedStator']
