from sum_digits import sum_of_digits


def test_mixed_string_returns_digit_sum():
    assert sum_of_digits("abc123") == 6


def test_no_digits_returns_zero():
    assert sum_of_digits("hello") == 0


def test_empty_string_returns_zero():
    assert sum_of_digits("") == 0


def test_digits_only_returns_correct_sum():
    assert sum_of_digits("9876") == 30


def test_special_characters_are_ignored():
    assert sum_of_digits("!@#4$%5") == 9
