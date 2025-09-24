#!/usr/bin/python3
""" Learn the Duck Typing with abstract class """
from abc import ABC, abstractmethod
import numpy as np


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
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius

    def area(self):
        return np.pi * (self.radius ** 2)

    def perimeter(self):
        return (2 * np.pi) * self.radius


class Rectangle(Shape):
    """ Concrete rectangle base an Shape abstract class """
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2


def shape_info(self):
    """ Print the area and the perimeter of created shape """
    try:
        print(f"Area: {self.area()}")
        print(f"Perimeter: {self.perimeter()}")
    except ZeroDivisionError:
        print("Error: division by zero occured")
