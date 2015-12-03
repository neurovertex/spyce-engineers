#import spyceengineers.deftypes.block
#import spyceengineers.deftypes.item

__all__ = ['Definition', 'physicalitem', 'cubeblock']

class Definition(object):
    __typevars__ = ['displayName', 'id', 'size']
    
    def __new__(cls, gamedata ,d):
        return super().__new__(cls)
    
    def __init__(self, gamedata ,d):
        self._gamedata = gamedata
        self._data = d;
        self.type = d['Id']['TypeId']
        self.subtype = d['Id']['SubtypeId']
        self.displayName = d['DisplayName']
        self.name = gamedata.locale[self.displayName] if self.displayName in gamedata.locale else "<%s>"%self.displayName
        if self.type == None:
            raise RuntimeError("Should not be none")
        if self.subtype == None:
            self.subtype = "_"+ self.type
    
    def __str__(self):
        return "<%s.%s:%s>"% (self.__class__.__name__, self.subtype, self.name)
    
    def __repr__(self):
        return "<%s/%s>"% (self.__class__.__name__, self.subtype)