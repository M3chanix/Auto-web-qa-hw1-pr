from hw1.Figure import Figure
from math import pi
from functools import cache

class Circle(Figure):
    """ Circle figure class"""
    _name = 'Circle'

    def __init__(self, *sides):
        if len(sides) == 1:
            super().__init__(*sides)
        else: raise ValueError('Circle should be defined only by radius')
    
    @property
    @cache
    def area(self) -> float:
        return pi*(self._sides[0]**2)
    @property
    @cache
    def perimeter(self) -> float:
        return 2*pi*self._sides[0]

