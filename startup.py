import os, sys, cPickle, defs
from defs import outOfDate, loadFile, POS

#########build our original word lists#############
for fname in os.listdir("."): #first, create the binaries/verify presence
    if fname[-4:]==".dat" and outOfDate(fname[:-3]+"bin", [fname]):
                source=open(fname)
                dest=open(fname[:-3]+"bin","wb")
                ls = [line.strip() for line in source]
                cPickle.dump(ls,dest,protocol=2)
                print "Wrote %s"%(fname[:-3]+"bin",)
                source.close()
                dest.close()
########word lists are now built##########

###########build our map of words -> POS######
deps=[]
for dep in os.listdir("."):
	if dep[-4:] == ".dat":
		deps.append(dep)
if outOfDate("posmap.bin",deps):
	POSMap = {}
	for word in loadFile("noun.bin"):
		POSMap[word] =  POS.noun
	for word in loadFile("adjective.bin"):
		POSMap[word] = POS.adj
	for word in loadFile("verb.bin"):
		POSMap[word] = POS.verb
	for word in loadFile("adverb.bin"):
		POSMap[word] = POS.verb
	for word in loadFile("determiners.bin"):
		POSMap[word] = POS.det
	dest=open("posmap.bin","wb")
	cPickle.dump(POSMap,dest,protocol=2)
	dest.close()
	print "Wrote dictionary."
#########dict is built##########
