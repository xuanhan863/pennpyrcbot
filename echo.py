#!/usr/bin/python
import sys, re, random, readline

test="hELLLO WORLD"
punc=",.?'\";:()-!"

def qa(msg, dest=sys.stdout):
    """Write a message and get the response."""
    dest.write(msg+"\n")
    return raw_input()
    
def niceSub(orig, repl):
    """Performs a string substitution maintaining case on first letter."""
    if orig[0].islower():
        return repl[0].lower() +repl[1:]
    return repl[0].upper()+repl[1:]

def rpl(msg, needle, sub):
    """Cleanly replaces all words of 'needle' in msg with 'sub'"""
    return " ".join([niceSub(x,sub) if x.lower()==needle.lower() else x for x in msg.split(" ")])

def commonsubs(orig):
    """Perform common word substitutions for responding."""
    orig=rpl(orig,"my","your")
    orig=rpl(orig,"i","you")
    orig=rpl(orig,"me","you")    #ppl like to talk about themselves
    return orig

def makeResponse(statement):
    """Takes a statement from the user and forms a prompt out of it.
To add another response, hard increment num_choices and add an if statement at
the bottom in the same manner as the others."""
    num_choices=5
    select=random.random()
    interval = 1.0/num_choices
    if select <= interval:
        if statement[-1] in punc:
            statement=statement[:-1]
        return statement+"?  How does that make you feel?"
    if select <= 2*interval:
        if statement[-1] in punc:
            statement = statement[:-1]
        return statement+"? Go on."
    if select < 3*interval:
        return "This subject getting too depressing.  Is there anything else"+\
            " we can talk about?"
    if select <=4*interval:
        return "You bore me, but continue if you must."
    if select <=5*interval:
        return "The same was once true for me."


def main(args=None):
    if args is None:
        args=sys.argv[1:]
    s=None
    while s!="quit":
        if s is None:
            msg="Hello."
            s=qa(msg)
            continue
        msg=commonsubs(s)
        s=qa(makeResponse(msg))

if __name__=="__main__":
    exit(main())
