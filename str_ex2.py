#!/usr/bin/env python
from __future__ import print_function

ip_addr = input("Enter the ip address: ")


fourth_oct = ip_addr.split(".")[3]

print(fourth_oct)
print("{:<12}".format(fourth_oct))
print("{:>12}".format(fourth_oct))
