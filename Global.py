import os, sys, cPickle, defs

execfile("startup.py") ##make sure all of our bin files are generated.

POS=defs.POS
Category=defs.Category #deal with this later
Word = defs.Word
Noun = defs.Noun
Adj = defs.Adj
Adv = defs.Adv
Det = defs.Det

words=defs.loadFile("masterwordtable.bin")
#cats = defs.loadFile("cat.bin") for later
def lookup(str):
	"""Returns a Word object for the given string.  This is the interface that should be used to "lookup" a word in the bot's knowledge base."""
	return words[str]
