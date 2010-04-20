#!/usr/bin/python

import sys, random, os, cPickle
from defs import outOfDate, loadFile
"""
PRE:
CSV file: CAT, word, word, ..., word

Purpose:
Input a word, and a list of related words will be returned.
This script will do that by finding the category of that word and mapping that to a set of common words from that category. It will randomly choose one and return. 

Usage:
Designed to adapt to a sentence where the word is tagged.
./categorizer.py csv_map_file

"""

#TAKEN FROM startup.py to generate bin#
for fname in os.listdir("."): #first, create the binaries/verify presence       
    if fname[-4:]==".dat" and outOfDate(fname[:-3]+"bin", [fname]):
                source=open(fname)
                dest=open(fname[:-3]+"bin","wb")
                ls = [line.strip() for line in source]
                cPickle.dump(ls,dest,protocol=2)
                print "Wrote %s"%(fname[:-3]+"bin",)
                source.close()
                dest.close()
#end of generate bin#

def main(args=None):
    line = raw_input()
    while line != "exit_now":
        li = line.split(" ")
        for word in li:
            cat = findCat(word)
            if cat is not None:
                print getCommonWord(cat)
            else:
                print "This word doesn't belong in a category."
        line = raw_input()

def findCat(word):
    for meat in loadFile('meat.bin'):
        if word == meat: return "meat"
    for veg in loadFile('veg.bin'):
        if word == veg: return "veg"
    for fruit in loadFile('fruit.bin'):
        if word == fruit: return "fruit"
    for dairy in loadFile('dairy.bin'):
        if word == dairy: return "dairy"
    return None

def getCommonWord(cat):
    mapping = makeMap(sys.argv[1])
    if mapping[cat] is not None:
        return mapping[cat][random.randint(0,2)].strip()

def makeMap(filename):
    map = {}
    file = open(filename)
    for line in file:
        tempList = line.split(",")
        map[tempList[0]] = tempList[1:]
    return map

if __name__ == "__main__":
    exit(main())
