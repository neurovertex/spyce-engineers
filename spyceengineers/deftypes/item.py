import spyceengineers.deftypes as deftypes
            
__all__ = ['Item', 'Ingot', 'GasContainerObject', 'EntityBase', 'OxygenContainerObject', 'PhysicalGunObject',
 'Ore', 'TreeObject']

class Item (deftypes.Definition):
    __typevars__ = ['size', 'id', 'volume', 'displayName', 'mass']
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
        self.size = d['Size']
        self.id = d['Id']
        self.volume = d['Volume']
        self.displayName = d['DisplayName']
        self.mass = d['Mass']

                    
class Ingot (Item):
    __typevars__ = ['physicalMaterial', 'icon', 'model']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.physicalMaterial = d['PhysicalMaterial']
        self.icon = d['Icon']
        self.model = d['Model']

                    
class GasContainerObject (Item):
    __typevars__ = ['physicalMaterial', 'icon', 'model', 'storedGasId', 'capacity']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.physicalMaterial = d['PhysicalMaterial']
        self.icon = d['Icon']
        self.model = d['Model']
        self.storedGasId = d['StoredGasId']
        self.capacity = d['Capacity']

                    
class EntityBase (Item):
    __typevars__ = ['public', 'icon', 'model', 'canSpawnFromScreen']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.public = d['Public']
        self.icon = d['Icon']
        self.model = d['Model']
        self.canSpawnFromScreen = d['CanSpawnFromScreen']

                    
class OxygenContainerObject (Item):
    __typevars__ = ['physicalMaterial', 'icon', 'model', 'storedGasId', 'capacity']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.physicalMaterial = d['PhysicalMaterial']
        self.icon = d['Icon']
        self.model = d['Model']
        self.storedGasId = d['StoredGasId']
        self.capacity = d['Capacity']

                    
class PhysicalGunObject (Item):
    __typevars__ = ['']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)

                    
class Ore (Item):
    __typevars__ = ['physicalMaterial', 'icon', 'model']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.physicalMaterial = d['PhysicalMaterial']
        self.icon = d['Icon']
        self.model = d['Model']

                    
class TreeObject (Item):
    __typevars__ = ['physicalMaterial', 'canSpawnFromScreen', 'icon', 'model']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.physicalMaterial = d['PhysicalMaterial']
        self.canSpawnFromScreen = d['CanSpawnFromScreen']
        self.icon = d['Icon']
        self.model = d['Model']

__all__ = ['Item', 'Ingot', 'GasContainerObject', 'EntityBase', 'OxygenContainerObject',
 'PhysicalGunObject', 'Ore', 'TreeObject']
