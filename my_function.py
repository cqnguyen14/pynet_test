#!/usr/bin/env python
from __future__ import print_function

def my_func(x, y, z=99):
    print(x + y + z)

my_list=[5, 7, 10]
my_func(*my_list)

#print(x + y + z)

my_dict = {
    'x': 7,
    'y': 3,
    'z': 1
}
my_func(**my_dict)

#print(x - y + z)
