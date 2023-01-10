#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of ", number, "is ", number[-1])
if number[-1] > 5:
    print("and is greater than 5")
if number[-1] == 0:
    print("and is 0")
if number[-1] < 6 && number[-1] != 0:
    print("and is less than 6 and not 0")
