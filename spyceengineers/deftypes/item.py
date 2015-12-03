import spyceengineers.deftypes as deftypes

class Item (deftypes.Definition):
    __typevars__ = ['mass', 'displayName', 'id', 'size', 'volume']
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
        self.mass = d['Mass']
        self.displayName = d['DisplayName']
        self.id = d['Id']
        self.size = d['Size']
        self.volume = d['Volume']

                    
class Ingot (Item):
    __typevars__ = ['model', 'icon', 'physicalMaterial']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.model = d['Model']
        self.icon = d['Icon']
        self.physicalMaterial = d['PhysicalMaterial']

                    
class EntityBase (Item):
    __typevars__ = ['public', 'canSpawnFromScreen', 'model', 'icon']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.public = d['Public']
        self.canSpawnFromScreen = d['CanSpawnFromScreen']
        self.model = d['Model']
        self.icon = d['Icon']

                    
class GasContainerObject (Item):
    __typevars__ = ['model', 'storedGasId', 'icon', 'physicalMaterial', 'capacity']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.model = d['Model']
        self.storedGasId = d['StoredGasId']
        self.icon = d['Icon']
        self.physicalMaterial = d['PhysicalMaterial']
        self.capacity = d['Capacity']

                    
class PhysicalGunObject (Item):
    __typevars__ = ['']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)

                    
class OxygenContainerObject (Item):
    __typevars__ = ['model', 'storedGasId', 'icon', 'physicalMaterial', 'capacity']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.model = d['Model']
        self.storedGasId = d['StoredGasId']
        self.icon = d['Icon']
        self.physicalMaterial = d['PhysicalMaterial']
        self.capacity = d['Capacity']

                    
class TreeObject (Item):
    __typevars__ = ['canSpawnFromScreen', 'model', 'icon', 'physicalMaterial']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.canSpawnFromScreen = d['CanSpawnFromScreen']
        self.model = d['Model']
        self.icon = d['Icon']
        self.physicalMaterial = d['PhysicalMaterial']

                    
class Ore (Item):
    __typevars__ = ['model', 'icon', 'physicalMaterial']

    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
        self.model = d['Model']
        self.icon = d['Icon']
        self.physicalMaterial = d['PhysicalMaterial']

__all__ = ['Item', 'Ingot', 'EntityBase', 'GasContainerObject', 'PhysicalGunObject',
 'OxygenContainerObject', 'TreeObject', 'Ore']
