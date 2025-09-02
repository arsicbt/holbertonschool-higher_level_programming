#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = number % 10 if number > 0 else number %-10
msg = "greater than 5" if ld > 5 else "0" if ld == 0 else "less than 6 and not 0"

print(f"Last digit of {number} id {ld} and is {msg}")
