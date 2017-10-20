#!/usr/bin/env python 
from getpass import getpass 
from netmiko import ConnectHandler 

password = getpass("Enter password: ")
if __name__ == "__main__":
    pynet_rtr1 = {
        'device_type': 'cisco_ios',
        'ip':   '184.105.247.70',
        'username': 'pyclass',
        'password': password,
    }

    srx = {
        'device_type': 'juniper_junos',
        'ip':   '54.156.236.43',
        'username': 'pyclass',
        'password': password,
    }
    
    my_list = [pynet_rtr1, srx]
    
    for i in my_list:
        net_connect = ConnectHandler(**i) 
        if i['device_type'] ==  "cisco_ios":
            continue
        elif i['device_type'] == "juniper_junos":
            print(net_connect.send_command("show version"))
            juniper = open("cnguyen_cfg.txt", "wt")
            juniper.write(net_connect.send_command("show configuration | display set"))
            juniper.close()
