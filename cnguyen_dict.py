#!/usr/bin/env python
from __future__ import print_function

net_device = {
            'router1': {'ip_addr': '192.168.1.1'},
            'router2': {'ip_addr': '192.168.1.2'},
            'router3': {'ip_addr': '192.168.1.3'},
            }
for i, j in net_device.items():
    for x, y in j.items():
        print(x, y)
