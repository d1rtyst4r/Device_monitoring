import time

import ping
from device import Device
from read_file import get_all_ip_adreses
from send_mail import send_mail

# List with devices for check
files_for_read = ['Devices\\test_divices.txt']


devices_info_list = get_all_ip_adreses(files_for_read)
devices_list = []
for device_in_one_location in devices_info_list:  # create list with devices
    for device in device_in_one_location:
        devices_list.append(Device(device))

for device in devices_list:
    if not ping.myping(device.ip):
        time.sleep(2)  # wait 2 second
        if not ping.myping(device.ip):# ping device second time for minimize errors
            print(device.get_all_information())
            #send_mail(device)
    #else:  # if you need information of devices that are on-line
        #send_mail(device)
        #print(device.get_all_information())
