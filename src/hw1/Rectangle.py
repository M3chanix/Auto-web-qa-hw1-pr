from hw1.Figure import Figure
from functools import cache

class Rectangle(Figure):
    """Rectangle figure class"""
    _name = 'Rectangle'

    def __init__(self, *sides):
        if len(sides) != 2:
            raise ValueError('Rectangle should be defined by 2 sides')
        else: 
            super().__init__(*sides)

    @property
    @cache
    def area(self) -> float:
        return self._sides[0] * self._sides[1]
    
    @property
    @cache
    def perimeter(self) -> float:
        return 2 * self._sides[0] + 2* self._sides[1]

