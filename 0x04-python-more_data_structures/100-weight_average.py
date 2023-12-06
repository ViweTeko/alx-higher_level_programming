#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    sum_score = 0
    sum_weight = 0
    for a in my_list:
        sum_score += a[0] * a[1]
        sum_weight += a[1]
    return sum_score / sum_weight
