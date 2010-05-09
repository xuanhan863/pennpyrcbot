import os, sys, cPickle, defs
from defs import outOfDate, loadFile, POS, Category

wordListSources = { "noun.dat" : defs.Noun, "adjective.dat" : defs.Adj, 
              "verb.dat" : defs.Verb, "adverb.dat" : defs.Adv, 
              "determiners.dat" : defs.Det}
binWordLists = ["noun.bin", "adjective.bin", "verb.bin", "adverb.bin", 
                "determiners.bin"]
wordtablefname = "masterwordtable.bin"
categorytablefname = "categorytable.bin"
#########build our original word lists#############
for fname in wordListSources: #first, ensure the binaries exist
    if outOfDate(fname[:-3]+"bin", [fname]):
        factory = wordListSources[fname]
        ####parse each line and add to list
        source=open(fname)
        ls = [factory(line.strip(),"") if len(line.strip().split(" ")) == 1 \
                  else factory(*line.strip().split(" ")) for line in source]
        source.close()
        ####add to master list
        ####and now dump the list to hdd
        dest=open(fname[:-3]+"bin","wb")
        cPickle.dump(ls,dest,protocol=2)
        dest.close()
        del ls
        print "Wrote %s"%(fname[:-3]+"bin",)
########word lists are now built##########
allwords = {}
###### now we export our master lookup list######
if outOfDate(wordtablefname,binWordLists):
    for file in binWordLists:
        ls = loadFile(file)
        for word in ls:
            allwords[word.val]=word
        del ls
    dest=open(wordtablefname,"wb")
    cPickle.dump(allwords,dest,protocol=2)
    dest.close()
    print "Just wrote out the master word table."
else:
    allwords = loadFile(wordtablefname)  #we need this loaded for next step
#########dict is built##########
###### now we build the category table#####
if outOfDate("cat.bin", ["cat.dat"]):
    cats={}
    source = open("cat.dat")
    for line in source:
        c = Category.lineToCat(line, cats.__getitem__, allwords.__getitem__)
        cats[c.tag] = c  #built on line above.  now we insert
        dest=open("cat.bin","wb")
        cPickle.dump(cats,dest,protocol=2)
        dest.close()  
    print "Just dumped the category table."
