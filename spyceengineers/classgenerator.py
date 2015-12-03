import xml.etree.ElementTree as xml
from os.path import exists
from os import mkdir

MAX_LINE_LEN = 100

def breakline(line, maxlen, separator):
    if len(line) <= maxlen:
        return line
    else:
        i = line[:maxlen].rfind(",")
        return "%s\n%s"% (line[:i+1], breakline(line[i+1:], maxlen, separator))
    
def generateClassFiles(types, todir="."):
    todir += "/deftypes"
    if not exists(todir):
        mkdir(todir)
    for key in types.keys():
        if key == "locale":
            continue
        c,r = types[key]        
        defkeys = set()
        defoptkeys = {}
        for i in r:
            keys = set()
            tid = i.find('Id').find('TypeId').text
            for k in i:
                keys.add(k.tag)

            if tid not in defoptkeys:
                defoptkeys[tid] = set(keys)
            else:
                defoptkeys[tid] &= keys

            if len(defkeys) == 0:
                defkeys |= keys
            else:
                defkeys &= keys

        for k in defoptkeys.keys():
            defoptkeys[k] -= defkeys

        with open("%s/%s.py" % (todir, c.lower()), 'w') as f: # Package __init__.py
            print(f.name)
            typeIds = set(t.find('Id').find('TypeId').text for t in r)
            f.write("""import spyceengineers.deftypes as deftypes

class %s (deftypes.Definition):
    __typevars__ = ['%s']
    def __new__(cls, gamedata, d):
        if d['Id']['TypeId'] !=  __class__.__name__:
            try:
                cl = next(c for c in __class__.__subclasses__() if c.__name__ == d['Id']['TypeId'])
                return object.__new__(cl)
            except StopIteration:
                raise RuntimeError("Type %%s not found in '%%s' (%%s)" %% (d['Id']['TypeId'], __class__.__name__, ", ".join(k.__name__ for k in __class__.__subclasses__())))
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
""" % (c, breakline("', '".join(var[0].lower() + var[1:] for var in defkeys), MAX_LINE_LEN, ',')))
            for var in defkeys:
                f.write("        self.%s = d['%s']\n"% (var[0].lower() + var[1:], var))
            for t in typeIds:
                if t == c:
                    if len(defoptkeys[t]) > 0:
                        raise RuntimeError("Type Class named like base class with specific type vars : %s"%c)
                    else:
                        continue
                f.write("""
                    
class %s (%s):
""" % (t,c))
                f.write("    __typevars__ = ['%s']\n"% breakline("', '".join(var[0].lower() + var[1:] for var in defoptkeys[t]), MAX_LINE_LEN, ','))
                f.write("""\n    def __new__(cls, gamedata, d):
        return super().__new__(cls, gamedata, d)

    def __init__(self, gamedata, d):
        super().__init__(gamedata, d)
""")
                for var in defoptkeys[t]:
                    f.write("        self.%s = d['%s']\n"% (var[0].lower() + var[1:], var))
            f.write(breakline("\n__all__ = ['%s']\n" % ("', '".join([c] + [t for t in typeIds if t != c])), MAX_LINE_LEN, ','))

def loadFromDataDir(d, locale=None):
    datafiles = {"items": ("PhysicalItem", "Item"), "blocks": ("CubeBlock", "Block"), "components":("Component", "Component")}
    data = {k:(v[1], xml.parse("%s/%ss.sbc"%(d,v[0])).getroot()[0]) for k,v in datafiles.items()}
    data['locale'] = {'default': xml.parse("%s/Localization/MyTexts.resx"%d).getroot()}
    if locale != None:
        data['locale']['requested'] = xml.parse("%s/Localization/MyTexts.%s.resx"% (d,locale)).getroot()
    return data
        