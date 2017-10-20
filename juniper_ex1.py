#!/usr/bin/env python
#!/usr/bin/env python
from __future__ import print_function
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from getpass import getpass
from pprint import pprint


juniper_srx = {
        "host": "juniper1.twb-tech.com",
        "user": "pyclass",
        "password": getpass(),
    }

a_device = Device(**juniper_srx)
a_device.open()
#pprint(a_device.facts)
a_device.timeout = 90
cfg = Config(a_device)

print()
print()
print()
print()
print()

cfg.load(path="configure_ip.conf", format="text", merge=False)


print("Merge diff: ")
print(cfg.diff())

print("Performing rollback")
cfg.rollback(0)

print()
print()
print()
print()
print()

cfg.load(path="configure_ip.conf", format="text", replace=False)


print("Replace diff: ")
print(cfg.diff())

print("Performing rollback")
cfg.rollback(0)
