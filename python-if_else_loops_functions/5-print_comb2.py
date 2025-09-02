#!/usr/bin/python3
for n in range(99):
    print("{:02d}".format(n), end=", " if n != 98 else ", 99\n")
