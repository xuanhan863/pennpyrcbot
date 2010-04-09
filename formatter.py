#!/usr/bin/python

"""Usage: 
First Argument: Input File
Second Argument: Output File

Command:
./formatter input output
"""

import sys

file = open(sys.argv[1], "r")
outfile = open(sys.argv[2], "w")

for line in file:
    print line
    outfile.write(line[0:line.index("-")]+ "\n")
