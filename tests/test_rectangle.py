from hw1.Rectangle import Rectangle

def test_rectangle_positive():
    rectangle = Rectangle(4, 8)
    assert rectangle is not None

def test_rectangle_zero():
    rectangle = None
    try:
        rectangle = Rectangle(0, 0)
    except ValueError:
        pass
    assert rectangle is None

def test_rectangle_negative():
    rectangle = None
    try:
        rectangle = Rectangle(-4, -8)
    except ValueError:
        pass
    assert rectangle is None

# Метод площади работает
def test_rectangle_area():
    rectangle = Rectangle(4, 8)
    assert rectangle.area > 0

# Метод периметра работает
def test_rectangle_perimeter():
    rectangle = Rectangle(4, 8)
    assert rectangle.perimeter > 0

# Метод суммы площадей двух одинаковых фигур работает
def test_rectangle_add_area():
    rec_one = Rectangle(4, 8)
    rec_two = Rectangle(5, 6)
    assert rec_one.add_area(rec_two) == rec_one.area + rec_two.area

def test_rectangle_one_side():
    rectangle = None
    try:
        rectangle = Rectangle(4)
    except ValueError:
        pass
    assert rectangle is None

def test_rectangle_zero_sides():
    rectangle = None
    try:
        rectangle = Rectangle()
    except ValueError:
        pass
    assert rectangle is None
