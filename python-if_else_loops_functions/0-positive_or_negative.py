#!/usr/bin/python3
import random
number = random.randint(-10, 10)
print(f"{number} is {'negative' if number < 0 else 'zero' if number == 0 else 'positive'}")
