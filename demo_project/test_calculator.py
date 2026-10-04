from calculator import divide, is_even


def test_divide():
    assert divide(10, 2) == 5


def test_even_number():
    assert is_even(4) is True


def test_odd_number():
    assert is_even(5) is False