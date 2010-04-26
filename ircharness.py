#!/usr/bin/python
import naive_parser as parser
import readline
from thematic_roles import *
import Global, responder
import os

endpunc='.?!'

do = parser.parse

blank='_none'
def getResponse(feed):
    if feed[0] == ">":
        return mapleResponse(feed[1:])
    if feed[-1] in endpunc:
        feed = feed[:-1] + " " + feed[-1]  #add in space before last punctuation
    else:
        feed = feed+" ."
    if feed[0].isupper():
        feed = feed[0].lower() + feed[1:] #make sure first word lower case

    if feed is not None:
        try:
            res=do(feed)
        except Exception:
            return "I don't know enough English to answer that yet."
        cat = "null"
        theme_cor=blank
        try:
            verbInd=feed.index(res['action'].core.val)
            end = feed[len(res['action'].core.val):]
            for word in end.split(" "):
                try:
                    cattry=Global.lookup(word)
                    cat=cattry.cat
                    theme_cor = word
                    if cat !="null" and cat != "": #if we found one
                        break
                except Exception:
                    pass
        except KeyError:
            pass#print "No Action"
        toRes = "type:"+res['type']
        theme =res['theme']
        toRes+=" theme:%s@thm"%(cat,)
        if theme.det != blank:
            toRes+=":%s@det"%(theme.det,)
        for desc in theme.descriptors:
            toRes+=":%s@des"%(desc.val,)
            toRes+=":%s@cor"%(theme_cor,)
            toRes+=" agent"
        agent=res['agent']
        if agent.det != blank:
            try:
                toRes+=":%s@det"%(agent.det.val,)
            except Exception:
                toRes+=":%s@det"%(agent.det,)
        for desc in agent.descriptors:
            toRes+=":%s@des"%(desc.val,)
        if agent.core != blank:
            toRes+=":%s@cor"%(agent.core.val,)
        try:
            toRes+=" action"            
            action = res['action']
            for desc in action.descriptors:
                toRes+=":%s@des"%(desc.val)
            if action.core != blank:
                toRes+=":%s@cor"%(action.core.val,)
        except KeyError:
                pass
        return responder.main(toRes,feed)

def mapleResponse(str):
    tmp=open("mapleinputswap","w")
    tmp.write(str)
    tmp.close()
    os.system("maple mapleinputswap > mapleoutputswap")
    os.remove("mapleinputswap")
    tmp=open("mapleoutputswap")
    ls = [line[:-1] for line in tmp]
    ls = ls[6:] # strip header and footer
    ls = ls[:-3]
    tmp.close()
    os.remove("mapleoutputswap")
    print ls
    ret = ["I asked Mr. Maple, he says:"]
    ret.extend(ls,)
    return ret
