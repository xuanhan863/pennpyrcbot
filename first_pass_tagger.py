#!/usr/bin/python
import Global

def pass1(str):
    """This takes in a line of plaintext and tags each word with part of speech.  This is necessary so that the parser can use regex's on the word structure for its grammar."""
    ls = str.split(" ")
    for i in xrange(len(ls)):
        token = ls[i]
        tag = Global.lookup(token).parse_tag
        ls[i] = tag + token #writeback
    return " ".join(ls)


if __name__ == "__main__":
    while True:
        str = raw_input("Input words to be tagged:\n")
        if str =="exit":
            break
        print pass1(str)+"\n"
                   
        
        
    
