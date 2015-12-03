import spyceengineers.deftypes as deftypes

class Component (deftypes.Definition):
    __typevars__ = ['maxIntegrity', 'mass', 'displayName', 'id', 'model', 'size', 'volume', 'icon', 'dropProbability',
 'physicalMaterial']
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
        self.maxIntegrity = d['MaxIntegrity']
        self.mass = d['Mass']
        self.displayName = d['DisplayName']
        self.id = d['Id']
        self.model = d['Model']
        self.size = d['Size']
        self.volume = d['Volume']
        self.icon = d['Icon']
        self.dropProbability = d['DropProbability']
        self.physicalMaterial = d['PhysicalMaterial']

__all__ = ['Component']
