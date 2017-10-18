#!/usr/bin/env python
from __future__ import print_function

filename = "show_version.txt"
f = open(filename)
show_version = f.read()

#print(show_version)



#fields = show_version.split("License UDI:")
#fields = show_version.split("*0        CISCO881-SEC-K9:")

#print(fields)


#router_sn = fields[1]
#router_sn = router_sn.strip()
#print(router_sn)

pid = "Processor board ID"

for line in show_version.splitlines():
    if "Processor board ID" in line:
        line = line.strip()
        fields = line.split()
        print("The router serial number is:  {}".format(fields[3]))
#    prefix = fields[1]
#    as_path = fields[5:-1]
    #print(as_path)
    #print("Prefix: {}, AS_Path: {}".format(prefix, as_path))
