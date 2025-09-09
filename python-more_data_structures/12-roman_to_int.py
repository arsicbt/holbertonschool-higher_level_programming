#!/usr/bin/python3
roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def roman_to_int(roman_string):
    """ Renvoie l'ecriture decimale du nombre donnee en chiffres
    romains """
    if roman_string == "" or is None:
        return 0
    if len(roman_string) == 1:
        return roman[roman_string]
    elif roman[roman_string[0]] >= roman[roman_string[1]]:
        return roman[roman_string[0]] + roman_to_int(roman_string[1:])
    else:
        return roman_to_int(roman_string[1:]) - roman[roman_string[0]]
