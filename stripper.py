#!/usr/bin/python

import sys

"""
Usage: strip each line in file to remove whitespace

Command:
./stripper.py input output
"""

try:
    infile = open(sys.argv[1], "r")
    outfile = open(sys.argv[2], "w")
    for line in infile:
        outfile.write(line.strip()+"\n")
finally:
    infile.close()
    outfile.close()
