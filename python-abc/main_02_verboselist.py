#!/usr/bin/env python3
from task_02_verboselist import VerboseList

vl = VerboseList([1, 2, 3])
print(vl)
vl.append(4)
print(vl)
vl.extend([5, 6])
print(vl)
vl.remove(2)
print(vl)
vl.pop()
print(vl)
vl.pop(0)
print(vl)