#!/usr/bin/python3
""" Learn the Duck Typing with abstract class """
from abc import ABC, abstractmethod
#import numpy as np

class Shape(ABC):
    """ Abstract class for a future shape """
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """ Concrete circle base an Shape abstract class """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return np.pi * (abs(self.radius) ** 2)

    def perimeter(self):
        return (2 * np.pi) * abs(self.radius)


class Rectangle(Shape):
    """ Concrete rectangle base an Shape abstract class """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """ Print the area and the perimeter of created shape """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

l = [1, 1, 2]
print(l)
l.remove['1']
print(l)