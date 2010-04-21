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
	try:
		return words[str]
	except KeyError:
		pass
	if str[-1] == "s":
		try:
			return words[str[:-1]]
		except KeyError:
			return words[str[:-2]]
	if str[-2:] == "ed":
		try:
			return words[str[:-1]]
		except KeyError:
			return words[str[:-2]]
	if str[-2:] == "ly":
		return words[str[:-2]]
