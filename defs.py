import os, cPickle, Types

POS = Types.POS
Word = Types.Word
Noun = Types.Noun
Adj = Types.Adj
Adv = Types.Adv
Verb = Types.Verb
Det = Types.Det
Category = Types.Category

punc = ".!,?:;" #simple after-word-only punctuation

#helper functions		
def outOfDate(product,deps):
	"""Checks if the modification date of any file in deps is later than the modification date for product."""
        if not os.path.exists(product):
                return True
        for dep in deps:
                if os.stat(product)[8] < os.stat(dep)[8]:
			return True
        return False

def loadFile(fname):
	"""Loads a pickled file with the given name into a python structure."""
        tmp=open(fname, "rb")
        ret=cPickle.load(tmp)
        tmp.close()
        return ret
