#!/usr/bin/python
import Global

def pass1(str):
    ls = str.split(" ")
    for i in xrange(len(ls)):
        token = ls[i]
        print "Token:",token
        tag = Global.lookup(token).parse_tag
        ls[i] = tag + token #writeback
    return " ".join(ls)


if __name__ == "__main__":
    while True:
        str = raw_input("Input words to be tagged:\n")
        if str =="exit":
            break
        print pass1(str)+"\n"
                   
        
        
    
