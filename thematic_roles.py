import defs, Global

null = "_none_"

class agent:
    def __init__(self, words):
        self.det, self.descriptors, self.core = null, [], null
        for word in words:
            pos = word.POS
            if pos == POS.det: self.det = word
            elif pos == POS.adj: self.descriptors.append(word)
            elif pos == POS.noun: self.core = word

class action:
    def __init__(self, words):
        self.descriptors, self.core = [], null
        for word in words:
            pos = word.POS
            if pos == POS.adv: self.descriptors.append(word)
            elif pos == POS.verb: self.core = word

#always check whether a theme's isnp field is true or not!
#need to treat it differently depending!
class theme:
    def __init__(self, words):
        self.det, self.descriptors = null, []
        self.isnp = False

        for word in words:
            pos = word.POS
            if pos == POS.det or POS.noun: 
                self.isnp = True
                break
        
        if self.isnp:
            self.core = null
            for word in words:
                pos = word.POS
                if  pos == POS.det: self.det = word
                elif pos == POS.adj: self.descriptors.append(word)
                elif pos == POS.noun: self.core = word

        else:
            self.core = []
            for word in words:
                pos = word.POS
                if pos == POS.adj: self.core.append(word)
