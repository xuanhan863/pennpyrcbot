#!/usr/bin/python
import Global
from defs import punc

def pass1(str):
    ls = str.split(" ")
    for i in xrange(len(ls)):
        token = ls[i]
        end=""
        if token[-1] in punc:
            end = token[-1] #chop off and save end puncuation
            token = token[:-1]
        tag = Global.lookup(token).parse_tag
        ls[i] = token+tag+end #writeback
    return " ".join(ls)


if __name__ == "__main__":
    while True:
        str = raw_input("Input words to be tagged:\n")
        if str =="exit":
            break
        print pass1(str)+"\n"
                   
        
        
    
