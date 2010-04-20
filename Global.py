import os, sys, cPickle

def lookup(str):
	"""Returns a Word object for the given string.  This is the interface
that should be used to "lookup" a word in the bot's knowledge base."""
	return Word(str)

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

for fname in os.listdir("."): #first, create the binaries/verify presence
        if fname[-4:]==".dat":
            if not os.path.exists(fname[:-3]+"bin"):
                source=open(fname)
                dest=open(fname[:-3]+"bin","wb")
                ls = [line.strip() for line in source]
                cPickle.dump(ls,dest,protocol=2)
                print "Wrote %s"%(fname[:-3]+"bin",)
                source.close()
                dest.close()
tmp=open("noun.bin","rb")  #now load the binaries
nouns=cPickle.load(tmp)
tmp=open("adjective.bin","rb")
adjs=cPickle.load(tmp)
tmp=open("verb.bin","rb")
verbs=cPickle.load(tmp)
tmp=open("adverb.bin","rb")
advs=cPickle.load(tmp)
tmp=open("determiners.bin","rb")
dets=cPickle.load(tmp)

class POS:
	noun, verb, adj, adv, det, null = range(6)
	@staticmethod
	def getPOSFromFiles(word):#shouldn't be needed outside of this code
		if word in nouns:
			return POS.noun
		if word in verbs:
			return POS.verb
		if word in adjs:
			
		if word in advs:
			ret.add(POS.adv)
		if word in dets:
			ret.add(POS.det)
		if len(ret) == 0:
			ret.add(POS.null)
		return tuple(ret)
	@staticmethod
	def getPOS(word):
		global POSMap
		try:
			return POSMap[word]
		except KeyError:
			pass
		if word[-1]=="s":
			try:
				return POSMap[word[:-1]]
			except KeyError:
				pass
		return (POS.null,)


###########build our map of words -> set of POS
if not os.path.exists("posmap.bin"):
	POSMap = {}
	for word in nouns:
		POSMap[word] =  POS.getPOSFromFiles(word)
	for word in adjs:
		POSMap[word] = POS.getPOSFromFiles(word)
	for word in verbs:
		POSMap[word] = POS.getPOSFromFiles(word)
	for word in advs:
		POSMap[word] = POS.getPOSFromFiles(word)
	for word in dets:
		POSMap[word] = POS.getPOSFromFiles(word)
	dest=open("posmap.bin","wb")
	cPickle.dump(POSMap,dest,protocol=2)
	dest.close()
else:
	source=open("posmap.bin","rw")
	POSMap=cPickle.load(source)
	source.close()
#####dict is built
