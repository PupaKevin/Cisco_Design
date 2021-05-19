#!/usr/bin/env python
from netmiko import ConnectHandler

iosv_l2 = {
    'device_type': 'cisco_ios',
    'ip': 'deCrib.witech.vi',
    'username': 'pupa',
    'password': '#L0v3Alone!',
}


net_connect = ConnectHandler(**iosv_l2)
# net_connect.find_prompt()
output = net_connect.send_command('show int des')
print(output)
output = net_connect.send_command('show inv')
print(output)
