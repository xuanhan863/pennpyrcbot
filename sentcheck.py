#!/usr/bin/python

import sys, cPickle
from Global import nouns, adjs, advs, verbs, POS, getPOS

validFormats=[POS.null,POS.adj, POS.noun, POS.adv, POS.verb, POS.null, POS.adj, POS.noun]

def main(args=None):    
    print "Type in sentences to be analyzed. Type 'exit_now' to quit."
    inLine = raw_input()
    while inLine != "exit_now":
        posDict = {} #maps word to set of integers(possible POS)
        inList = inLine.lower()[:-1].split(" ")
        for word in inList:
            posDict[word] = getPOS(word)
    #        print "Added '%s' with set: %s"%(word,posDict[word])
        for i in range(len(inList)):
     #       print "Working on word: '%s' with index %s"%(inList[i],i)
            if validFormats[i] not in posDict[inList[i]]:
                print "Did not match structure on",inLine
                return 1
       #     if i == len(inList)-1:
      #          print "Good structure on", inLine
        try:
            inLine = raw_input()
        except EOFError:
            print "All tests passed!"
            return 0

if __name__ == "__main__":
    exit(main())
