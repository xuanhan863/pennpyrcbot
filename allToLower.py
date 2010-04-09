#!/usr/bin/python

"""Usage:
First Argument: Input File
Second Argument: Output File

Command:
./allToLower input output
"""

import sys

file = open(sys.argv[1], "r")
out = open(sys.argv[2], "w")

for line in file:
    out.write(line.lower())
