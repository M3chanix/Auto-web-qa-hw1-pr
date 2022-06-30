from hw1.Square import Square

def test_square_positive():
    square = Square(4)
    assert square is not None

def test_square_zero():
    square = None
    try:
        square = Square(0)
    except ValueError:
        pass
    assert square is None

def test_square_negative():
    square = None
    try:
        square = Square(-4)
    except ValueError:
        pass
    assert square is None

# Метод площади работает
def test_square_area():
    square = Square(4)
    assert square.area > 0

# Метод периметра работает
def test_square_perimeter():
    square = Square(4)
    assert square.perimeter > 0

# Метод суммы площадей двух одинаковых фигур работает
def test_square_add_area():
    sq_one = Square(4)
    sq_two = Square(8)
    assert sq_one.add_area(sq_two) == sq_one.area + sq_two.area

def test_square_two_sides():
    square = None
    try:
        square = Square(4, 4)
    except ValueError:
        pass
    assert square is None

def test_square_zero_sides():
    square = None
    try:
        square = Square()
    except ValueError:
        pass
    assert square is None
