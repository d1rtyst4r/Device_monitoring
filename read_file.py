import ping as p
from os import path


def get_ip_adreses_from_file(ip_file):
    """"Return list with ip from file """
    with open(ip_file, 'r') as file:
        lines = file.readlines()
        file.close()
        l = []
        for line in lines:
            new_line = line.strip()
            l.append(new_line)
        return (l)


def get_info(file):
    """"Create list with devises information """
    ipaddress_list = get_ip_adreses_from_file(file)
    all_device_info = []

    for ip in ipaddress_list:
        device_info = []  # list with device information
        index1 = ipaddress_list.index(ip)
        device_info.append(ip)  # device ip
        device_info.append(path.splitext(file)[0])  # Use file name as device type and location
        if path.splitext(file)[0] == 'Devices\\Daugavpils_kase':
            device_info.append(index1 + 3)  # Device index for dau cash-boxs
        else:
            device_info.append(index1 + 1)  # Device index for others cash-boxes
        all_device_info.append(device_info)  # add list to list with all devices information
    return all_device_info


def get_all_ip_adreses(list_files_name):
    """"Return list with full information of all devices"""
    all_files_info = []
    for file in list_files_name:
        all_files_info.append(get_info(file))
    return all_files_info
