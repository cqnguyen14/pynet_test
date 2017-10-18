#!/usr/bin/env python
from __future__ import print_function

my_list = list(range(49))

for x in my_list:
    if x == 13:
        continue
    elif x > 39:
        break
    print(x)
