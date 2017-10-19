#!/usr/bin/env python
from __future__ import print_function
from pprint import pprint

f = open("show_ip_int_brief.txt")
show_ip_int = f.read()

show_ip_int = show_ip_int.split("Protocol")[1]
show_ip_int = show_ip_int.strip()

my_dict = {}

for line in show_ip_int.splitlines():
    fields = line.split()
    intf_name = fields[0]
    ip_addr = fields[1]
    status = fields[-2]
    protocol = fields[-1]
    my_dict[intf_name] = {
        'ip_addr': ip_addr,
        'status': status,
        'protocol': protocol
    }
print(my_dict)



for line in output:
    line = line.strip()
    if 'Interface' in line:
        continue
    interface, ip_address, _, _, status, protocol = line.split()
    fields = {
        'ip_address': ip_address,
        'line_status': status,
        'line_protocol': protocol,
    }
    ip_dict[interface] = fields


pprint(ip_dict)



#for line in show_ip_int.splitlines():
#    fields = line.split()
#    intf_name = fields[0]
#    ip_addr = fields[1]
#    status = fields[-2]
#    protocol = fields[-1]
#    my_dict[intf_name] = {
#        'ip_addr': ip_addr,
#        'status': status,
#        'protocol': protocol
#    }
#print(my_dict)
