#!/usr/bin/python
import os,sys,cPickle
import random

#generate random sentences based off of a single structure
#todo, make something that matches against these

def main(args=None):
    execfile("writer.py") #make sure binaries exist
    tmp=open("noun.bin","rb")  #now load the binaries
    nouns=cPickle.load(tmp)
    tmp=open("adjective.bin","rb")
    adjs=cPickle.load(tmp)
    tmp=open("verb.bin","rb")
    verbs=cPickle.load(tmp)
    tmp=open("adverb.bin","rb")
    advs=cPickle.load(tmp)
    print "Hit enter to generate lines.  Type 'exit' to quit."
    while raw_input() != "exit":
        line="The "
        line+=adjs[int(random.random()*len(adjs))]+" "
        line+=nouns[int(random.random()*len(nouns))]+" "
        line+=advs[int(random.random()*len(advs))]+" "
        line+=verbs[int(random.random()*len(verbs))]+"s the "
        line+=adjs[int(random.random()*len(adjs))]+" "
        line+=nouns[int(random.random()*len(nouns))]+"."
        print line
    return 1

if __name__ =="__main__":
    exit(main())
    
