#!/usr/bin/env python
from __future__ import print_function

import re

filename = "show_int_fa4.txt"
f = open(filename)
show_int = f.read()

for line in show_int.splitlines():
    if "packets input" in line or "packets output" in line:
        print(line)
        m = re.search(r"^\s+(\d+)*(\d+)", line)
        print(m.group(0))
        print(m.group(1))
        print(m.group(2))
#print(show_int)


#import re

#m = re.search(r"(.*) packets (.*),", show_int, flags=re.DOTALL)

#for line in m.group(0).splitlines():
#    if "packets input" in line or "packets output" in line:
#        print(line)








#    elif "packets output" in line:
#        print(line)



#fields = show_bgp.split("Weight Path")

#print(fields)


#bgp_table = fields[1]
#bgp_table = bgp_table.strip()
#print(bgp_table)

#for line in bgp_table.splitlines():
#    line = line.strip()
#    fields = line.split()
#    #print(fields)
#    prefix = fields[1]
#    as_path = fields[5:-1]
    #print(as_path)
#    print("Prefix: {}, AS_Path: {}".format(prefix, as_path))
