from hw1.Circle import Circle

# Круг - можно содать с положительным радиусом
def test_positive_radius():
    circle = Circle(10)
    assert circle is not None

# Нельзя создать с нулевым радиусом
def test_zero_radius():
    circle = None
    try:
        circle = Circle(0)
    except ValueError:
        pass
    assert circle is None

# Нельзя создать с отрицательным радиусом
def test_negative_radius():
    circle = None
    try:
        circle = Circle(-10)
    except ValueError:
        pass
    assert circle is None

# Метод площади работает
def test_circle_area():
    circle = Circle(10)
    assert circle.area > 0

# Метод периметра работает
def test_circle_perimeter():
    circle = Circle(10)
    assert circle.perimeter > 0

# Метод суммы площадей двух одинаковых фигур работает
def test_circle_add_area():
    c_one = Circle(10)
    c_two = Circle(12)
    assert c_one.add_area(c_two) == c_one.area + c_two.area

