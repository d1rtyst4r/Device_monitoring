from ping3 import ping


def myping(host):  # return True or False
    """"This function check is device is on-line(has ping) """
    resp = ping(host)
    if resp is None:
        return False
    else:
        return True


def check_ip_list(iplist):
    """"Return two list. First contain ip what are up, second what are down"""
    ip_down = []
    ip_up =[]
    for ip in iplist:
        res = myping(ip)
        if not res:
            ip_down.append(ip)
        else: ip_up.append(ip)
    return ip_up, ip_down
