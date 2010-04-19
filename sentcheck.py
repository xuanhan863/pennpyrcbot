#!/usr/bin/python

import sys, cPickle
from Global import nouns, adjs, advs, verbs, POS

validFormats=[POS.null,POS.adj, POS.noun, POS.adv, POS.verb, POS.null, POS.adj, POS.noun]

def main(args=None):    
    print "Type in sentences to be analyzed. Type 'exit_now' to quit."
    inLine = raw_input()
    while inLine != "exit_now":
        posDict = {} #maps word to set of integers(possible POS)
        inList = inLine.lower()[:-1].split(" ")
        for word in inList:
            posDict[word] = getPOS(word)
#            print "Added '%s' with set: %s"%(word,posDict[word])
    
        for i in range(len(inList)):
 #           print "Working on word: '%s' with index %s"%(inList[i],i)
            if validFormats[i] not in posDict[inList[i]]:
                print "Did not match structure on",inLine
                break
 #           if i == len(inList)-1:
#                print "Good structure on", inLine
        
        inLine = raw_input()

def getPOS(word):
    ret = set()
    if word in nouns or (word[-1]=="s" and word[:-1] in nouns):
        ret.add(POS.noun)
    if word in verbs or (word[-1]=="s" and word[:-1] in verbs):
        ret.add(POS.verb)
    if word in adjs:
        ret.add(POS.adj)
    if word in advs:
        ret.add(POS.adv)
    if len(ret) == 0:
        ret.add(POS.null)
    return ret

if __name__ == "__main__":
    exit(main())
