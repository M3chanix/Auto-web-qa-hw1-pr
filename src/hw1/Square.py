from hw1.Rectangle import Rectangle

class Square(Rectangle):
    """Square figure class"""
    _name = 'Square'

    def __init__(self, *sides):
        if len(sides) == 1:
            sides = [sides[0], sides[0]]
            super().__init__(*sides)
        else: 
            raise ValueError('Square should be defiend by 1 side')

