import os, sys, cPickle

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

class POS:
	noun, verb, adj, adv, null = range(5)
