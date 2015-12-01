from spyceengineers.deftypes import Definition
from spyceengineers.deftypes.item import Item
from spyceengineers.deftypes.block import Block

__all__ = ['GameData', 'deftypes']

class GameData:
    def __init__(self):
        pass
    
    def loadFromData(self, data):
        self.items = GameData.PhysicalItemDatabase(self.loadXML(Item, data['items'][1]))
        self.blocks = GameData.CubeBlockDatabase(self.loadXML(Block, data['blocks'][1]))
        
    def loadXML(self, T, root):
        listtags = GameData.findListTags(root)
        data = []
        try:
            for e in root:
                obj = GameData.todict(e, listtags)
                data.append(T(self, obj))
        except:
            self._last_failed = e
            raise RuntimeError("Error while loading")
        return data
    
    def todict(el, listtags):
        if el.tag in listtags:
            return list(GameData.todict(e, listtags) for e in el)
        if len(el) > 0:
            return {i.tag:GameData.todict(i, listtags) for i in el}
        elif len(el.attrib) > 0:
            vals = dict(el.attrib)
            for k,v in vals.items():
                try:
                    vals[k] = int(v)
                except:
                    try:
                        vals[k] = float(v)
                    except:
                        pass
            return vals
        else:
            v = el.text
            try:
                return int(v)
            except:
                try:
                    return float(v)
                except:
                    return v

    def findListTags(el):
        if len(el) > 1 and len(el.findall(el[0].tag)) > 1:
            listtags = set([el.tag])
        else:
            listtags = set()

        for e in el:
            listtags |= GameData.findListTags(e)
        return listtags

    class DictOverlay(dict):
        def __init__(self, dic, overlay):
            super().__init__(dic)
            self.overlay = overlay
            
        def __getitem__(self, key):
            if key in self.overlay:
                return self.overlay[key]
            return super().__getitem__(key)
    
    class CubeBlockDatabase(DictOverlay):
        def __init__(self, defs):
            data = {ty:{v.subtype:v for v in defs if v.type == ty} for ty in set(t.type for t in defs)}
            sizes = set(k.cubeSize for vals in data.values() for k in vals.values())
            overlay = {k:{ty:{sty:v for sty,v in stys.items() if v.cubeSize == k} for ty,stys in data.items()} for k in sizes}
            for si,tys in overlay.items():
                for ty in list(dict(tys).keys()):
                    if len(tys[ty]) == 0:
                        del tys[ty]
            for ty in data.keys():
                data[ty] = GameData.DictOverlay(data[ty], {s:{k:v for k,v in data[ty].items() if v.cubeSize == s} for s in sizes})
            super().__init__(data, overlay)
    
    class PhysicalItemDatabase(dict):
        def __init__(self, defs):
            super().__init__({ty:{v.subtype:v for v in defs if v.type == ty} for ty in set(t.type for t in defs)})