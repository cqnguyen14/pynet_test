#!/usr/bin/env python
from __future__ import print_function

net_device = {'username': 'admin', 'bgp_peers': ['10.10.10.10', '20.20.20.20', '30.1.1.1'], 'ip_addr': '192.168.1.1', 'password': 'whatever'}

for x in net_device:
    print(x)



for x,y in net_device.items():
    print(x, y)
