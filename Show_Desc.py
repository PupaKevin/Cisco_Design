#!/usr/bin/env python

iosv_l2 = {
    'device_type': 'cisco_ios',
    'ip': '10.255.115.8',
    'username': 'kmaynard',
    'password': '1LoveviNGN',
}


net_connect = ConnectHandler(**iosv_l2)
# net_connect.find_prompt()
output = net_connect.send_command('show ip int brief')
print(output)
output = net_connect.send_command('show int des')
print(output)