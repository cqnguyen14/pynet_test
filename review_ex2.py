#!/usr/bin/env python
from __future__ import print_function
from pprint import pprint

f = open("show_arp.txt")
show_arp= f.read()

show_arp = show_arp.split("Interface")[1]
show_arp = show_arp.strip()

my_dict1 = {}
my_dict2 = {}

for line in show_arp.splitlines():
    fields = line.split()
    j1 = fields[0]
    ip_addr = fields[1]
    j2 = fields[2]
    mac = fields[3]
    my_dict1[ip_addr] = mac
    my_dict2[mac] = ip_addr
print()
print("IP Address       Mac Address")
pprint(my_dict1)
print()
print()
print("Mac Address        IP Address")
pprint(my_dict2)
