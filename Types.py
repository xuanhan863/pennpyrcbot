class POS:
        noun, verb, adj, adv, det, wh, aux, cop, null = range(9)

parse_tag_symbol = "@"
class Word:
        POS=POS.null;
	parse_tag = parse_tag_symbol+"nil"
        def __init__(self, str,category):
                self.val=str
		self.cat=category
	def category(self):
		"""Guaranteed to return the tag for the category which this word is a member of."""
		return self.cat
	def __str__(self):
		return "%s(%s):%s"%(self.val,self.cat,self.__class__.__name__,)
	def __repr__(self):
		return "%s(%s,%s)"%(self.__class__.__name__,self.val,self.cat)
class Noun(Word):
        POS=POS.noun
	parse_tag = parse_tag_symbol + "noun_"
        def __init__(self,str,category):
                Word.__init__(self,str,category)
class Adj(Word):
        POS=POS.adj
	parse_tag = parse_tag_symbol + "adj_"
        def __init__(self,str, category):
                Word.__init__(self,str,category)
class Adv(Word):
        POS=POS.adv
	parse_tag = parse_tag_symbol + "adv_"
        def __init__(self,str,category):
                Word.__init__(self,str,category)
class Verb(Word):
        POS=POS.verb
	parse_tag = parse_tag_symbol + "verb_"
        def __init__(self,str,category):
                Word.__init__(self,str,category)
class Det(Word):
        POS=POS.det
	parse_tag = parse_tag_symbol + "det_"
        def __init__(self,str,category):
                Word.__init__(self,str,category)

class Aux(Word):
	POS=POS.aux
	parse_tag = parse_tag_symbol + "aux_"
	def __init__(self,str,category):
                Word.__init__(self,str,category)

class Cop(Word):
	POS=POS.cop
	parse_tag = parse_tag_symbol + "cop_"
	def __init__(self,str,category):
                Word.__init__(self,str,category)

class Wh(Word):
	POS = POS.wh
	parse_tag = parse_tag_symbol + "wh_"
	def __init__(self, str, category):
		Word.__init__(self, str, category)
	

class Category:
        """Defines an object representing a category of words.  Included are a parent category and lists of common agents, actions, and descriptors associated with this category."""
        def __init__(self,name):
                self.tag = name  ##### name of this category                
                self.parentCat = None
                self.commonAgents = [] #common nouns associated with this   
                self.commonActions = [] #common actions/verbs               
                self.commonDescs = [] #take a guess                         
        def addAgent(self, newAgent):
                """Adds an agent this category's list of common agents."""
                self.commonAgents.append(newAgent)
        def addAction(self,newAction):
                """Adds an action this category's list of common actions."""
                self.commonActions.append(newAction)
        def addDesc(self,newDesc):
                """Adds an descriptor this category's list of common ones."""
                self.commonDescs.append(newDesc)
        def getAgents(self):
                """Gets a list of this category's common agents"""
                return list(self.commonAgents) #clone that sh*t               
        def getActions(self):
                """Gets a list of this category's common actions"""
                return list(self.commonActions)
        def getDescs(self):
                """Gets a list of this category's common descriptors"""
                return list(self.commonDescs)
        def __str__(self):
                return "Category: '%s' is subtype of '%s'.  Common actions %s, agents %s, descs %s."%(self.tag, self.parentCat, self.commonActions, self.commonAgents, self.commonDescs)
        def __repr__(self):
                return str(self)
        @staticmethod
	def lineToCat(line,cat_lookup, word_lookup):
                """This is a factory function which Converts a string into a Category instance.  Arguments 2 and 3 should be functions to lookup categories and words."""
                args=line.strip().split(" ") #break line into chunks
                assert(len(args) <= 5) #no sophisticated error checking
                c = Category(args[0]) #chunk 1                         
                if args[1] != "null": #chunk 2                         
                        try:
                                c.parentCat=cat_lookup(args[1])
			except KeyError:
                                print "The category '%s' has not yet been defined."%(args[1],)
                                return None
                for group in args[2:]:  #break up next 3 chunks
                        members=group.split(":")  #figure out the type
                        if members[0] == "action":
                                push=c.addAction
                        elif members[0] == "agent":
                                push = c.addAgent
                        elif members[0] == "desc":
                                push = c.addDesc
                        else: raise Hell, "Unknown type tag."
                        members=members[1:] #cut the tag off          
                        for word in members:
                                if word.strip() != "":
                                        try:  #for now.  should abstract this
                                                push(word_lookup(word.strip()))
                                        except KeyError:
                                                print "Specified critical word '%s' does not exist."%(word.strip(),)
                return c
