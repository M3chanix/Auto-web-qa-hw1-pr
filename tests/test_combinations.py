from hw1.Circle import Circle
from hw1.Triangle import Triangle
from hw1.Rectangle import Rectangle
from hw1.Square import Square

def test_circle_other():
    circle = Circle(10)
    test_list = [1, 2, 3]
    try:
        circle.add_area(test_list)
    except ValueError:
        pass

def test_triangle_other():
    triangle = Triangle(4, 5, 6)
    test_list = [1, 2, 3]
    try:
        triangle.add_area(test_list)
    except ValueError:
        pass

def test_rectangle_other():
    rectangle = Rectangle(4, 8)
    test_list = [1, 2, 3]
    try:
        rectangle.add_area(test_list)
    except ValueError:
        pass

def test_square_other():
    square = Square(4)
    test_list = [1, 2, 3]
    try:
        square.add_area(test_list)
    except ValueError:
        pass

def test_circle_rectangle():
    circle = Circle(10)
    rec = Rectangle(4, 8)
    assert rec.add_area(circle) == rec.area + circle.area

def test_triangle_square():
    tri = Triangle(4, 5, 6)
    sq = Square(4)
    assert tri.add_area(sq) == sq.area + tri.area

