#!/usr/bin/python

"""
About:
This script takes apart the output of the harness program specified in a specific format as specified below. The following data structures are used:

theme(tMap): part -> word (ie. core -> radish)
agent(aMap): part -> word (ie. core -> boy)

It then takes the map and retreives common topics associated with that agent/theme.

Finally, through a probabilistic approach, it returns a response.

Input Format:
type:word theme:word@thm:word@det:word@des:word@cor agent:word@agt:word@det:word@des:word@cor
"""
import sys, re, categorizer, random

def main(args=None):
    #makes maps
    theme = {}
    agent = {}
    type = ""

    #to be adjusted to read from output of another class/script
    #sample input is currently rotten carrots
    input = "type:statement theme:veg@thm:the@det:cut@des:carrot@cor agent:carrot@agt:the@det:awesome@des:boy@cor"

    #sectionList breakdown
    #type[]
    #theme[]
    #agent[]
    sectionList = input.split(" ")
    
    for group in sectionList:
        currentDict = {}
        groupList=group.split(":")
        if groupList[0] == "type":
            type = groupList[1]
        elif groupList[0] == "theme" or groupList[0] == "agent":
            for element in groupList[1:]:
                pair = element.split("@")
                currentDict[pair[1]] = pair[0]
        else:
            print "Input format not recognized"

        if groupList[0] == "theme":
            theme = currentDict
        elif groupList[0] == "agent":
            agent = currentDict

    #generate response
    print genResponse(type, theme, agent)

#generates response from word:POS using category
def genResponse(type, tMap, aMap):
    #type has yet to be used

    #find alternate common topic for each through rgen
    #reminder: commons is a list [action, agent, descriptor]
    commons = getCommons(tMap["thm"])
#    original =  [tMap["des"],tMap["cor"],
    #construct sentence
    #yet to implement probabilistic approach to choosing answers
    #goodbye func can be called at a low probability
    choice = random.randint(0, 100)
    
    if choice == 0:
        return goodbye()
    elif choice < 11:
        return generalize(commons)
    elif choice < 21:
        return comment(commons)
    elif choice < 31:
        return question(commons)
    elif choice < 41:
        return imperative(commons)
    else:
        return "\"There are 10 kinds of people in this world, those who understand binary, and those who don't\""

#returns a list of length 3 @action,@agent,@desc
def getCommons(theme):
    catFile = open("cat.dat", "r")
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

def question(commons):
    print "How about " + commons[2] + " " + commons[1] + "?"

def comment(commons):
    print "I like " + commons[2] + " " + commons[1] " more."

def imperative(commons):
    pass

def generalize():
    pass

def goodbye():
    pass

if __name__=="__main__":
    exit(main())
