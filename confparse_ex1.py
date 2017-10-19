#!/usr/bin/env python
from __future__ import print_function, unicode_literals
from ciscoconfparse import CiscoConfParse

cisco_file = 'cisco_ipsec.txt'

cisco_cfg = CiscoConfParse(cisco_file)
intf_obj = cisco_cfg.find_objects(r"^crypto map")
print()
for intf in intf_obj:
    print(intf.text)
    for child in intf.children:
        print(child.text)
    print()




