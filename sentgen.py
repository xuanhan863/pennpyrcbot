#!/usr/bin/python
import os,sys, cPickle, random
from Global import nouns, adjs, verbs, advs #import lists of words

#generate random sentences based off of a single structure
#todo, make something that matches against these
def main(args=None):
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
