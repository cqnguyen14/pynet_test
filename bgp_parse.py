#!/usr/bin/env python
from __future__ import print_function

filename = "show_ip_bgp.txt"
f = open(filename)
show_bgp = f.read()


fields = show_bgp.split("Weight Path")

print(fields)


bgp_table = fields[1]
bgp_table = bgp_table.strip()
#print(bgp_table)

for line in bgp_table.splitlines():
    line = line.strip()
    fields = line.split()
    #print(fields)
    prefix = fields[1]
    as_path = fields[5:-1]
    #print(as_path)
#    print("Prefix: {}, AS_Path: {}".format(prefix, as_path))
