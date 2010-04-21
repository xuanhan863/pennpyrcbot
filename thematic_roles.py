import defs, Global

POS = Global.POS
null = "_none_"

class agent:

    def __init__(self, words):
        self.det, self.descriptors, self.core = null, [], null
        for word in words:
            pos = word.POS
            if pos == POS.det: self.det = word
            elif pos == POS.adj: self.descriptors.append(word)
            elif pos == POS.noun: self.core = word

    def __str__(self):        
        s = "Agent: \n"
        s += ("Determiner: " + self.det.val + "\n")

        desc_strs = []
        for desc in self.descriptors: desc_strs.append(desc.val)
        s += ("Descriptors: " + ", ".join(desc_strs) + "\n")
        
        s += ("Core: " + self.core.val)
        return s


class action:

    def __init__(self, words):
        self.descriptors, self.core = [], null
        for word in words:
            pos = word.POS
            if pos == POS.adv: self.descriptors.append(word)
            elif pos == POS.verb: self.core = word

    def __str__(self):
        s = "Action: \n"

        desc_strs = []
        for desc in self.descriptors: desc_strs.append(desc.val)
        s += ("Descriptors: " + ", ".join(desc_strs) + "\n")
        
        s += ("Core: " + self.core.val)
        returns

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

    def __str__(self):
        s = "Theme: \n"

        if self.isnp:
            s += ("Determiner: " + self.det.val + "\n")

            desc_strs = []
            for desc in self.descriptors: desc_strs.append(desc.val)
            s += ("Descriptors: " + ", ".join(desc_strs) + "\n")
        
            s += ("Core: " + self.core.val)
            return s

        else:
            core_strs = []
            for core in self.core: core_strs.append(core.val)
            s += ("Core: " + ", ".join(core_strs))
            return s
                

            
    
