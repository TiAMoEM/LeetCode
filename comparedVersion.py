# -*- coding:utf-8 -*-
def compared_version(ver1, ver2):
    """
    传入不带英文的版本号,特殊情况："10.12.2.6.5">"10.12.2.6"
    :param ver1: 版本号1
    :param ver2: 版本号2
    :return: ver1< = >ver2返回-1/0/1
    """
    list1 = ver1.split(".")
    list2 = ver2.split(".")
    print(list1)
    print(list2)
    if len(list1) <= len(list2):
        for i in range(len(list1)):
            if int(list1[i]) > int(list2[i]):
                return 1
            elif int(list1[i]) < int(list2[i]):
                return -1
            else:
                pass
    else:
        for i in range(len(list2)):
            if int(list1[i]) > int(list2[i]):
                return 1
            elif int(list1[i]) < int(list2[i]):
                return -1
            else:
                pass

    if len(list1) == len(list2):
        return 0
    elif len(list1) < len(list2):
        return -1
    else:
        return 1


print(compared_version("10.12.2.6.5", "10.12.2.6"))

"""    
    list1 = str(ver1).split(".")
    list2 = str(ver2).split(".")
    print(list1)
    print(list2)
    # 循环次数为短的列表的len
    for i in range(len(list1)) if len(list1) < len(list2) else range(len(list2)):
        if int(list1[i]) == int(list2[i]):
            pass
        elif int(list1[i]) < int(list2[i]):
            return -1
        else:
            return 1
    # 循环结束，哪个列表长哪个版本号高
    if len(list1) == len(list2):
        return 0
    elif len(list1) < len(list2):
        return -1
    else:
        return 1


result = compared_version("10.12.2.6.5", "10.12.2.6")
print(result)
"""
