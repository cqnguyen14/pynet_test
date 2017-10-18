#!/usr/bin/env python
from __future__ import print_function

f = open("writefile", "wt")
f.write("hello 1\n")
f.write("hello 2\n")
f.write("hello 3\n")

f.close()

f = open("writefile")
output = f.read()

print(output)

f = open("writefile", "at")
