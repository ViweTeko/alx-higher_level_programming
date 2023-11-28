#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
z = abs(number % 10)

if number < 0:
    z = -z

if z < 6 and z != 0:
    print(f'Last digit of {number} is {z} and is less than 6 and not 0')
elif z == 0:
    print(f'Last digit of {number} is {z} and is 0')
else:
    print(f'Last digit of {number} is {z} and is greater than 5')
