#!/usr/bin/env python
from __future__ import print_function

ip_addr = input("Enter the ip address: ")

ip_list = ip_addr.split(".")
print(ip_list)
ip_list[-1] = 0


print("{:<12}{:<12}{:<12}{:<12}".format(*ip_list))


bin_list

#oct1 =  ip_list[0]
#oct2 =  ip_list[1]
#oct3 =  ip_list[2]
#oct4 =  ip_list[3]

#print(oct1)

print("The decimal of the first octet is: ",(ip_list[0]))
print(bin(int(ip_list[0])))
print(bin(int(ip_list[1])))
print(bin(int(ip_list[1])))
print(bin(int(ip_list[2])))
print(bin(int(ip_list[2])))
print(bin(int(ip_list[3])))
print(bin(int(ip_list[3])))
