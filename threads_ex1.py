#!/usr/bin/env python 
from __future__ import print_function, unicode_literals
from getpass import getpass 
import threading
from datetime import datetime
from netmiko import ConnectHandler
from my_devices import device_list as devices
import yaml

def show_arp(a_device):
    '''Execute show version command using Netmiko.'''
    remote_conn = ConnectHandler(**a_device)
    print()
    print('#' * 80)
    print(remote_conn.send_command_expect("show arp"))
    print('#' * 80)
    print()

def main():
    '''
    Use threads and Netmiko to connect to each of the devices. Execute
    'show version' on each device. Record the amount of time required to do this.
    '''
    start_time = datetime.now()

    for a_device in devices:
        my_thread = threading.Thread(target=show_arp, args=(a_device,))
        my_thread.start()

    main_thread = threading.currentThread()
    for some_thread in threading.enumerate():
        if some_thread != main_thread:
            print(some_thread)
            some_thread.join()

    print("\nElapsed time: " + str(datetime.now() - start_time))

if __name__ == "__main__":
    main()



#password = getpass("Enter password: ")
#
#    my_list = [pynet_rtr1, srx]
#
#    for i in my_list:
#        net_connect = ConnectHandler(**i)
##        if i['device_type'] ==  "cisco_ios":
##            print(net_connect.send_command("show version"))
##            cisco = open("cisco_cfg.txt", "wt")
##            cisco.write(net_connect.send_command("show running-config"))
##            cisco.close()
#        if i['device_type'] == "juniper_junos":
#            net_connect.send_config_set("set system syslog file messages any error")
#            net_connect.commit(and_quit = True)
#            juniper = open("juniper_cfg22.txt", "wt")
#            juniper.write(net_connect.send_command("show configuration | display set"))
#            juniper.close()
