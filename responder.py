#!/usr/bin/python

import sys, re, categorizer

def main(args=None):
    #makes map word:POS
    taggedString = "happy@adj book@noun horse@noun say@vrb"
    map = {}
    taggedList = taggedString.split(" ")
    for element in taggedList:
        pair = element.split("@")
        map[pair[1]] = pair[0]
    for k in map:
        print k,map[k]

#generates response from word:POS using category
def genResponse(map):
    #find common word in each POS map

    #change sentence structure

    #construct sentence using 1 or 2 of common words


if __name__=="__main__":
    exit(main())
