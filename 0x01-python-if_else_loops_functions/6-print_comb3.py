#!/usr/bin/python3
for digit in range(0, 10):
    for dig in range(digit + 1, 10):
        if digit == 8 and dig == 9:
            print("{}{}".format(digit, dig))
        else:
            print("{}{}".format(digit, dig), end=", ")
