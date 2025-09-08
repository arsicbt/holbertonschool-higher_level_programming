#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    for i in range(len(my_list)):
        new_list.append(True) if i % 2 == 0 else new_list.append(False)
    return new_list
