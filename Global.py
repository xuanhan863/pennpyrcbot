import os, sys, cPickle, defs

execfile("startup.py") ##make sure all of our bin files are generated.

POS=defs.POS
Category=defs.Category 
Word = defs.Word
Noun = defs.Noun
Adj = defs.Adj
Adv = defs.Adv
Det = defs.Det

words=defs.loadFile("masterwordtable.bin")
cats = defs.loadFile("cat.bin") 
errmsg = "BADSTUFFHAPPENED"
def lookup(str):
	"""Returns a Word object for the given string.  This is the interface that should be used to "lookup" a word in the bot's knowledge base."""
	#note, we lookup with some redundancy/allowance for form variation
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

def get_cat(cat_name):
	"""Returns the category object associated with this tag/word/string."""
	try:
		return cats[cat_name]
	except KeyError:
		return None
