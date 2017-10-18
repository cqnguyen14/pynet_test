#!/usr/bin/env python
from __future__ import print_function

def my_func(x):
    f = open(x)
    file  = f.read()
    return file

show_version = my_func("show_version.txt")

for line in show_version.splitlines():
    if "Processor board ID" in line:
        line = line.strip()
        fields = line.split()
        print("The router serial number is:  {}".format(fields[3]))
