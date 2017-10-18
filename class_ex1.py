#!/usr/bin/env python
from __future__ import print_function



class NetDevice(object):
  def __init__(self,iip_addr, username, password, serial_number, model, vendor, uptime, os_version):
    self.ip_addr = ip_addr
    self.username = username 
    self.password = password
    self.serial_number = serial_number
    self.model = model
    self.vendor = vendor
    self.uptime = uptime
    self.os_version = os_version

  def test_method(self):
    print "Device IP is: {}".format(self.ip_addr) 
    print "Username is: {}".format(self.username) 
 
rtr1 = NetDevice('10.22.1.1', 'admin', 'passw') 
rtr1.test_method()
