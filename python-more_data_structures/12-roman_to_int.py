#!/usr/bin/python3

def roman_to_int(roman_string):
    if type(roman_string) is not str:
        return (0)

    if type(roman_string) is str:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        total = 0
    previous = 0

    for letter in reversed(roman_string.upper()):
        value = values.get(letter, 0)

        if value < previous:
            total -= value
        else:
            total += value

        previous = value

    return total
