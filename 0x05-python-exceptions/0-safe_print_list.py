#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        num = 0
        for a in range(x):
            print(my_list[a], end="")
            num += 1
            for x in range(num):
                print("", end="")
        print()
        return num
    except IndexError:
        print()
        return num
