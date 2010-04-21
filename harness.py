#!/usr/bin/python
import naive_parser as parser
import readline

endpunc='.?!'

do = parser.parse

feed = None
print "I am still in the process of learning English."
print "Please test my knowledge with sentences."
print "I'll read them in and tell you what I understand."
while feed != "exit":
    if feed is not None:
        try:
            res=do(feed)
            for part in res:
                print "***"+part+"***"
                print res[part]
                print "-------------------------------"
        except Exception:
            print "Sorry, my English knowledge was too limited to understand that."
    feed = raw_input("\n> ")
#laziness hacks
    if feed[-1] in endpunc:
        feed = feed[:-1] + " " + feed[-1]  #add in space before last punctuation
    else:
        feed = feed+" ."
    if feed[0].isupper():
        feed = feed[0].lower() + feed[1:] #make sure first word lower case
    
