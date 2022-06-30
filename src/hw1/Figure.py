from functools import cache

class Figure():
    """ A base geometric figure class"""
    _name = 'Figure'

    def __new__(cls, *args, **kwargs):
        if cls is Figure:
            raise TypeError('Instance of Figure class cannot be created')
        else:
            return super().__new__(cls)

    def __init__(self, *sides):
        try:
            for value in sides:
                float(value)
        except ValueError:
            raise ValueError('Sides must be numbers')
        for value in sides:
            if value <= 0:
                raise ValueError('Sides must be positive')
        self._sides = sides

    @property
    def name(self) -> str:
        return self._name

    @property
    @cache
    def area(self) -> float:
        return 0

    @property
    @cache
    def perimeter(self) -> float:
        return sum(x for x in self._sides)

    def add_area(self, other_figure) -> float:
        if isinstance(other_figure, Figure):
            return self.area + other_figure.area
        else:
            raise ValueError('Given value is not a Figure instance')

