#!/usr/bin/env python
from __future__ import print_function

net_device = {'username': 'admin', 'password': 'whatever', 'ip_addr': '192.168.1.1', 'vendor': 'Juniper', 'Model': 'MX960'}

for x,y in net_device.items():
    print(x, y)


new_pass = input("Please enter new password: ")
net_device['password'] = new_pass

print("The new password is:  {}".format(net_device['password']))


net_device['secret'] = []
#print(net_device['secret'])


print(net_device.get('device_type', 'cisco ios'))
