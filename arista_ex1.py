#!/usr/bin/env python
from __future__ import print_function
from pprint import pprint
import pyeapi

pynet_sw = pyeapi.connect_to("pynet-sw2")
output= pynet_sw.enable("show ip route")
output = output[0]
output = output['result']['vrfs']['default']
print(output['routes'])
routes = output['routes']
print()
print()
print()

print("\n{:>15} {:>15} {:>15}".format("prefix", "interface", "next_hop"))
filler = "-" * 15
print()
print("{:>15} {:>15} {:>15}".format(filler, filler, filler))
print()
for prefix, attr in routes.items():
    intf_nexthop = attr['vias'][0]
    interface = intf_nexthop.get('interface', 'N/A')
    next_hop = intf_nexthop.get('nexthopAddr', 'N/A')
    print("{:>15} {:>15} {:>15}".format(prefix, interface, next_hop))
print()
#pprint(output[0]['result']['vrfs']['default']['routes'])
#my_dict = (output[0]['result']['vrfs']['default']['routes'])
#print(my_dict)
#print()
#my_dict = (output[0]['result']['vrfs']['default']['routes']['0.0.0.0/0']['vias'])
#print(my_dict)
#print()
#for key, value in my_dict.items():
#    print(key, value)
#    print()
