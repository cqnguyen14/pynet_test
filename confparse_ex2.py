#!/usr/bin/env python
from __future__ import print_function, unicode_literals
from ciscoconfparse import CiscoConfParse

cisco_file = 'cisco_ipsec.txt'

cisco_cfg = CiscoConfParse(cisco_file)
intf_obj = cisco_cfg.find_objects(r"^crypto map")
print("the crypto maps that are using pfs group2:")
print()
for intf in intf_obj:
    for child in intf.children:
        if "group2" in child.text:
            print(child.parent.text)
print()
