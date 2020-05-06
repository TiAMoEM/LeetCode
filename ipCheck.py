# -*- coding:utf-8 -*-
import re

def ipv4Check(ip):
    """
    正则表达式的匹配
    :param ip:
    :return:
    """
    regex = "^((\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])\.){3}(\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])$"
    p = re.compile(regex)
    if p.match(ip):
        return True
    else:
        return False

def ipcheck(ip):
    """
    将ip通过"."来划分，判断每个数字的是不是在0～255之间
    :param ip: string类型的ip地址
    :return:
    """
    iplist = str(ip).split(".")
    if len(iplist) != 4:
        return False
    for i in range(len(iplist)):
        if int(iplist[i]) < 0 or int(iplist[i]) > 255:
            return False
        else:
            pass
    if int(iplist[0]) == 0:
        return False
    return True


print(ipv4Check("192.168.1.1"))
print(ipv4Check("255.255.255.256"))
print(ipv4Check("255.255.255.0"))
print(ipv4Check("23.123.234.11"))
print(ipv4Check("0.0.0.0"))

# print(ipcheck("192.168.1.1"))
# print(ipcheck("255.255.255.256"))
# print(ipcheck("0.255.255.0"))

