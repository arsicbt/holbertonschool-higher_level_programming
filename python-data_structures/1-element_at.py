#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < len(my_list):
        for i in my_list:
            if idx == i:
                return my_list[idx]
    else:
        return None
