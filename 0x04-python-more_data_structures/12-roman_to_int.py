#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C':100, 'D': 500, 'M': 1000}
    number = 0
    if  not isinstance(roman_string, str) or not roman_string:
        return (0)
    for i, char in enumerate(roman_string):
        temp = roman[char]
        try:
            if temp < roman[roman_string[i + 1]]:
                temp = -temp
        except IndexError:
            pass
        number += temp
    return number
