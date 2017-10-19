#!/usr/bin/env python 
from getpass import getpass 
from netmiko import ConnectHandler 


import yaml

yaml_file = "my_device.yml"
with open(yaml_file) as f:
    output = yaml.load(f)


for device in output:
    device['password'] = getpass()

net_connect = ConnectHandler(**device)
print(net_connect.send_command("show arp"))
print()
