#!/usr/bin/python

"""
Input Format:
for word = var

type:word theme:word@thm:word@det:word@des:word@cor agent:word@agt:word@det:word@des:word@cor
"""
import sys, re, categorizer, random

def main(args=None):
    #makes maps
    theme = {}
    agent = {}
    type = ""
    input = "type:word theme:word@thm:word@det:word@des:word@cor agent:word@agt:word@det:word@des:word@cor"

    #sectionList breakdown
    #type[]
    #theme[]
    #agent[]
    sectionList = input.split(" ")
    
    for group in sectionList:
        currentDict = {}
        groupList=group.split(":")
        if groupList[0] == type:
            type = groupList[1]
        elif groupList[0] == "theme" or groupList[0] = "agent":
            for element in groupList:
                pair = element.split("@")
                currentDict[pair[1]] = pair[0]
        else:
            print "Input format not recognized"

        if groupList[0] == "theme":
            theme = currentDict
        elif groupList[0] == "agent":
            agent = currentDict

    #generate response
    genResponse(type, theme, agent)

#generates response from word:POS using category
def genResponse(type, tMap, aMap):
    #find common topic for each
    commons = getCommons(tMap[thm])

    #change sentence structure

    #construct sentence using 1 or 2 of common words

def getCommons(theme):
    catFile = open(cat.dat, "r")
    ret = ["@action", "@agent", "@desc"]
    for line in catFile:
        lineList = line.split(" ")
        if theme == lineList[0]:
            acList = lineList[2].split(":")
            ret[0] = acList[random.randint(1,len(acList)-1)]
            agList = lineList[3].split(":")
            ret[1] = agList[random.randint(1,len(agList)-1)]
            deList = lineList[4].split(":")
            ret[2] = deList[random.randint(1,len(deList)-1)]
            return ret
    return None

if __name__=="__main__":
    exit(main())
