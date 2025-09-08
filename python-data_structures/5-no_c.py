#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for elm in my_string:
        if elm != 'c' and elm != 'C':
            new_string += "{}".format(elm)
    return new_string
