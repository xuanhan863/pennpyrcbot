#!/usr/bin/python

"""
About:
This script takes apart the output of the harness program specified in a specific format as specified below. The following data structures are used:

theme(tMap): part -> word (ie. core -> radish)
agent(aMap): part -> word (ie. core -> boy)

It then takes the map and retreives common topics associated with that agent/theme.

Finally, through a probabilistic approach, it returns a response.

Input Format:
type:word theme:word@thm:word@det:word@des:word@cor agent:word@agt:word@det:word@des:word@cor action:word@act:word@des:word@cor
"""
import sys, re, categorizer, random, epi
random.seed(2)

def main(line, src):
    #makes maps
    theme = {}
    agent = {}
    action = {}
    type = ""

    #to be adjusted to read from output of another class/script
    #sample input is currently rotten carrots
    #file = open("input", 'r')
    #for line in file:
    input = line

    sectionList = input.split(" ")
    for group in sectionList:
        currentDict = {}
        groupList=group.split(":")
        if groupList[0] == "type":
            type = groupList[1]
        elif groupList[0] == "theme" or groupList[0] == "agent" or groupList[0] == "action":
            for element in groupList[1:]:
                pair = element.split("@")
                currentDict[pair[1].strip()] = pair[0].strip()
        else:
            print "Input format not recognized"
        if groupList[0] == "theme":
            theme = currentDict
        elif groupList[0] == "agent":
            agent = currentDict
        elif groupList[0] == "action":
            action = currentDict
    #generate response
    #print "GOT HERE"
    return genResponse(src, type, theme, agent, action)

#generates response from word:POS using category
def genResponse(src, type, tMap, aMap, actMap):
    #type has yet to be used

    #find alternate common topic for each through rgen
    #reminder: commons is a list [action, agent, descriptor]
    commons = getCommons(tMap["thm"])

    #original eg.cut, carrot, man, salty, very, like
    original =  [None,tMap["cor"], actMap["cor"], None, None]
    #choose type of sentence to construct
    choice = random.randint(0, 40)
    var = random.randint(0,5)
    
    if "like" in src.split(" ") or "likes" in src.split(" "):
        choice = 30

    if choice == 0:
        return goodbye()
    elif choice < 11:
        return generalize(commons,original,var)
    elif choice < 21:
        return comment(commons,original,var)
    elif choice < 31:
        if type == "statement":
            return question(commons,original,var)
        else:
            return generalize(commons,original,var)
    elif choice < 41:
        if type == "statement":
            return imperative(commons,original,var)
        else:
            return comment(commons,original,var)
   # elif choice < 51:
    #    return change(commons, original, var)
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

def question(commons,original,var):
    if var == 0:
        if original[2][-1] == "e":
            return "Why do you like " + original[2][:-1] + "ing " + original[1]
        elif original[2][-2:] == "es":
            return "Why do you like " + original[2][:-2] + "ing " + original[1]
        else:
            return "Why do you like " + original[2] + "ing " + original[1]
    elif var == 2:
        return "I know you like " + original[1] + ", but what else can you " + original[2] +v"?"
    elif var == 3:
        return "Can't you say something else about the " + original[1] + "?"
    else:
        return "I like " + original[1] + " too. Have you checked out " + epi.getFoodLink(original[1]) + "? They have some cool recipes."

def comment(commons,original,var):
    if var == 0:
        return "I really don't understand why you like the " + original[1] + " so much."
    elif var == 1:
        return "I knew that already, tell me more about the " + original[1] + "."
    elif var == 2:
        return "I really don't know what to say about that."
    elif var == 3:
        return "I've never knew that. Really?"
    else:
        return "I don't do that very often."

def imperative(commons,original,var):
    if var == 0:
        return "There's no reason to say that"
    elif var == 1:
        return "There is nothing cooler than that."
    elif var == 2:
        return "I don't know about that..."
    elif var == 3:
        return "Tell me more."
    elif var == 4:
        return "You're losing my attention. Be more interesting."
    else:
        return "That sounds interesting. Tell me more about the " + original[1] + "."

def generalize(commons,original,var):
    if var == 0:
        return "What type of thing is " + original[1] + "?"
    elif var == 1:
        return "What else is related to the " + original[1] + "?"
    elif var == 2:
        return "Where is this conversation going if we keep talking about " + original[1] + "?"
    elif var == 3:
        return "How is the " + original[1] + " relevant at all?"
    elif var == 4:
        return "That's too specific. What else?"
    else:
        return "Can't it be something else?"

#def change(commons,original,var):
#    return "How about " + commons[2] + " " + commons[1] + "?"

def goodbye():
    return "Anyway, I gotta go, cya."
    #quit here

if __name__=="__main__":
    exit(main())
