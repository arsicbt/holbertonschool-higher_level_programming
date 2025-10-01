#!/usr/bin/python3
"""
Module:
Countain a function that representing the
Pascal s triangle of n
"""


def ligne_suivante(ligne):
    """ Return the next ligne of Pascal's triangle """

    ligne_suiv = [1]
    for i in range(len(ligne) - 1):
        ligne_suiv.append(ligne[i] + ligne[i + 1])

    ligne_suiv.append(1)

    return ligne_suiv


def pascal_triangle(n):
    """ Return the Pascal's triangle of n height """

    if n <= 0:
        return []

    triangle = [[1]]
    for k in range(n - 1):
        ligne_k = ligne_suivante(triangle[k])
        triangle.append(ligne_k)

    return triangle
