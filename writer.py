import os, sys, cPickle

#This file exists to do setup which may be common to many different aspects
#of the system.  Currently, it takes all of the word lists and ensures that
#they are pickled.
for fname in os.listdir("."):
        if fname[-4:]==".dat":
            if not os.path.exists(fname[:-3]+"bin"):
                source=open(fname)
                dest=open(fname[:-3]+"bin","wb")
                ls = [line.strip() for line in source]
                cPickle.dump(ls,dest,protocol=2)
		print "Wrote %s"%(fname[:-3]+"bin",)
                
                    
