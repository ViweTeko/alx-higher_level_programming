#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    for a in my_list:
        if a not in new_list:
            new_list.append(a)
    return sum(new_list)
