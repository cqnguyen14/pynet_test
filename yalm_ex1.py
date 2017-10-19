#!/usr/bin/env python 
from getpass import getpass 
from netmiko import ConnectHandler 


import yaml

yaml_file = "my_yalm1.yml"
with open(yaml_file) as f:
    output = yaml.load(f)

print()
print()
print(output)
print()
print(len(output))
print()
print()

for i in output:
    print(i)
print()
print()
