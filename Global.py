import os, sys, cPickle, defs

execfile("startup.py") ##make sure all of our bin files are generated.

def lookup(str):
	"""Returns a Word object for the given string.  This is the interface
that should be used to "lookup" a word in the bot's knowledge base."""
	return Word(str)

POS=defs.POS

class Word:
	POS=POS.null;
	def __init__(self, str):
		self.val=str
	pass
class Noun(Word):
	POS=POS.noun
	def __init__(self,str):
		Word.__init__(self.str)
	pass
class Adj(Word):
	POS=POS.adj
	def __init__(self,str):
		Word.__init__(self.str)
	pass
class Adv(Word):
	POS=POS.adv
	def __init__(self,str):
		Word.__init__(self.str)
	pass
class Verb(Word):
	POS=POS.verb
	def __init__(self,str):
		Word.__init__(self.str)
	pass
class Det(Word):
	POS=POS.det
	def __init__(self,str):
		Word.__init__(self.str)
	pass
nouns=defs.loadFile("noun.bin") #now load the binaries
adjs=defs.loadFile("adjective.bin")
verbs=defs.loadFile("verb.bin")
advs=defs.loadFile("adverb.bin")
dets=defs.loadFile("determiners.bin")
