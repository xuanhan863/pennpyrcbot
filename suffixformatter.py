#!/usr/bin/python

"""Usage: 
First Argument: Input File
Second Argument: Output File

Command:
./suffixformatter input output
"""

import sys

file = open(sys.argv[1], "r")
outfile = open(sys.argv[2], "w")

for line in file:
    print line
    if (line.find("-") == 0):
        outfile.write(line[1:])
    
