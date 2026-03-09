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

def test_negative_numbers():
    assert sum_of_digits("10 and -3 and 7") == 11

def test_large_numbers():
    assert sum_of_digits("1d2f3add45678afef9012feMuhammedafa3456faeea789gsSRrg0") == (1+2+3+4+5+6+7+8+9+0+1+2+3+4+5+6+7+8+9+0)

def test_zero_values(): 
    assert sum_of_digits("0a0b0c") == 0

def test_newline_separated():
    assert sum_of_digits("4\n8\n15\n16\n23\n42") == (4+8+1+5+1+6+2+3+4+2)

def test_tab_separated():
    assert sum_of_digits("10\t20\t30") == (1+0+2+0+3+0)

