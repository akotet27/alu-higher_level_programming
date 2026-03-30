#!/usr/bin/python3
"""Defines a Rectangle subclass Square"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Inherits from Rectangle."""

    def __init__(self, size):
        """set the values"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
