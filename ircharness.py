#!/usr/bin/python
import parser
from first_pass_tagger import pass1
import readline
from thematic_roles import *
import Global, res
import os

endpunc='.?!'
default_resp="I don't know enough English to answer that yet."
parse = parser.parser.parse
respond = res.main

def getResponse(feed):
    try:
        if feed[0] == ">":
            return mapleResponse(feed[1:])
        if feed[-1] in endpunc and feed[-2] != " ":
            feed = feed[:-1] + " " + feed[-1]  #add in space before last punc
        elif feed[-1] not in endpunc:
            feed = feed+" ."
        if feed[0].isupper():
            feed = feed[0].lower() + feed[1:] #make sure first word lower case
        res=parse(pass1(feed[:-2])+feed[-2:])
        return respond(res)
    except Exception:
        return default_resp

def mapleResponse(str):
    """Used to pipe lines beginning with '>' to Maple.  Mainly just for fun.  Will not work if host machine does not have cli Maple available."""
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
#    print ls
    ret = ["I asked Mr. Maple, he says:"]
    ret.extend(ls,)
    return ret

if __name__ == "__main__":
    print "Hello."
    while True:
        line = raw_input()
        if "Goodbye" in line:
            exit(0)
        print getResponse(line)
