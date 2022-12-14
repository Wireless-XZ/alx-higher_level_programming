#!/usr/bin/python3
def roman_to_int(roman_string):
    result = prev = 0
    if type(roman_string) != str or roman_string is None:
        return 0
    roman_int = {'I': 1, 'V': 5, 'X': 10,
                 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for roman_num in roman_string:
        for roman_, int_ in roman_int.items():
            if roman_num is roman_:
                result += int_
                if prev < int_ and prev != 0:
                    result -= 2 * prev
                prev = int_
                break
    return result
