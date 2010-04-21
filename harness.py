#!/usr/bin/python
import naive_parser as parser

endpunc='.?!'

do = parser.parse

feed = None
while feed != "exit":
    if feed is not None:
        print do(feed)
    feed = raw_input("> ")
#laziness hacks
    if feed[-1] in endpunc:
        feed = feed[:-1] + " " + feed[-1]  #add in space before last punctuation
    else:
        feed = feed+" ."
    if feed[0].isupper():
        feed = feed[0].lower() + feed[1:] #make sure first word lower case
    
