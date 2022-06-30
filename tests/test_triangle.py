from hw1.Triangle import Triangle

def test_triangle_positive_sides():
    triangle = Triangle(4, 5, 6)
    assert triangle is not None

def test_triangle_zero_sides():
    triangle = None
    try:
        triangle = Triangle()
    except ValueError:
        pass
    assert triangle is None

def test_triangle_negative_sides():
    triangle = None
    try:
        triangle = Triangle(-4, -5, -6)
    except ValueError:
        pass
    assert triangle is None

# Метод площади работает
def test_triangle_area():
    triangle = Triangle(4, 5, 6)
    assert triangle.area > 0

# Метод периметра работает
def test_triangle_perimeter():
    triangle = Triangle(4, 5, 6)
    assert triangle.perimeter > 0

# Метод суммы площадей двух одинаковых фигур работает
def test_triangle_add_area():
    tri_one = Triangle(4, 5, 6)
    tri_two = Triangle(7, 8, 9)
    assert tri_one.add_area(tri_two) == tri_one.area + tri_two.area

def test_triangle_two_sides():
    triangle = None
    try:
        triangle = Triangle(4, 5)
    except ValueError:
        pass
    assert triangle is None

def test_triangle_unexisting():
    triangle = None
    try:
        triangle = Triangle(1, 2, 3)
    except ValueError:
        pass
    assert triangle is None
