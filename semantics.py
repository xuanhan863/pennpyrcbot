#--------------------
#sentence types
#--------------------

#Sentences store Agent, Action, and Predicate objects
class Sentence:
    type = "null"
    def __init__(self, agent, action, predicate):
        self.agent, self.action, self.predicate = agent, action, predicate
    def __str__(self):
        return " ".join([str(self.agent), str(self.action), str(self.predicate)]}
    def __repr(self): return str(self)

class Statement(Sentence):
    type = "statement"
    def __init__(self, agent, action, predicate):
        Sentence.__init__(self, agent, action, predicate)

#query (a plain string) can be either tf (true or false), or a wh-word
class Question(Sentence):
    type = "question"
    def __init__(self, agent, action, predicate, query):
        Sentence.__init__(self, agent, action, predicate)
        self.query = query

#--------------------
#thematic roles
#--------------------

#thematic roles store Word objects

class Agent:
    def __init__(self, dp):
        self.det, self.descriptor, self.core = dp.det, dp.descriptor, dp.core
    def __str__(self):
        s = ""
        if self.det: s += (self.det.val + " ")
        if self.descriptor: s += (self.descriptor.val + " ")
        return s + self.core.val
    def __repr__(self): 
        return str(self)
            
#a VP has a predicate field, but an Action does not!
#the VP's predicate will be separately stored in the sentence                
class Action:
    def __init__(self, vprime):        
        self.descriptor, self.core = vprime.descriptor, vprime.core
    def __str__(self):
        s = ""
        if self.descriptor: s += (self.descriptor.val + " ")
        return s + self.core.val
    def __repr__(self):
        return str(self)

#make sure to check with a predicate for its type before you use it!
#the 3 types are theme, infinitive, and linked (plain string)
class Predicate:
    def __init__(self, type, arg): 
        self.type = type
        if self.type == "theme": self.det, self.descriptor, self.core = arg.det, arg.descriptor, arg.core
        elif self.type == "infinitive": self.core = arg
        else: self.core == arg
    def __str__(self):
        if self.type == "theme":
            s = ""
            if self.det: s += (self.det.val + " ")
            if self.descriptor: s += (self.descriptor.val + " ")
            return s + self.core.val
        elif self.type == "infinitive": return "to " + self.core.val
        else: return self.core.val
    def __repr__(self):
        return str(self)

#--------------------
#phrase classes to make my life easier
#--------------------

class NP:
    def __init__(self, descriptor, core):
        self.descriptor, self.core = descriptor, core
    def __str__(self):
        s = ""
        if self.descriptor: s += (self.descriptor.val + " ")
        return s + self.core.val
    def __repr(self):
        return str(self)

class DP:
    def __init__(self, det, np):
        self.det, self.descriptor, self.core = det, np.descriptor, np.core
    def __str__(self): 
        s = ""
        if self.det: s += (self.det.val + " ")
        if self.descriptor: s += (self.descriptor.val + " ")
        return s + self.core.val
    def __repr__(self): 
        return str(self)

class VNaught:
    def __init__(self, core):
        self.core = core
    def __str__(self):
        return self.core.val
    def __repr__(self):
        return str(self)

class VP:
    def __init__(self, descriptor, vnaught):
        self.descriptor, self.core = descriptor, vnaught.core
    def __str__(self):
        s = ""
        if self.descriptor: s += (self.descriptor.val + " ")
        return s + self.core.val   
    def __repr__(self):
        return str(self)

#note that VPrimes have a Predicate object, in keeping with the grammar
class VPrime:
    def __init__(self, vp, pred):
        self.descriptor, self.core, self.predicate = vp.descriptor, vp.core, pred
    def __str__(self):
        s = ""
        if self.descriptor: s += (self.descriptor.val + " ")
        s += (self.core + " ")
        if self.predicate: s += str(self.predicate)
        return s
    def __repr__(self):
        return str(self)
