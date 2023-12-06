#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    Convert a roman numeral to an integer
    You can assume the number will be between 1 to 3999.
    If the roman_string is not a string or None, return 0
    """
    if type(roman_string) != str or roman_string is None:
        return 0
    numer = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list = 0
    for a in range(len(roman_string)):
        if a > 0 and numer[roman_string[a]] > numer[roman_string[a - 1]]:
            list += numer[roman_string[a]] - 2 * numer[roman_string[a - 1]]
        else:
            list += numer[roman_string[a]]
    return list
