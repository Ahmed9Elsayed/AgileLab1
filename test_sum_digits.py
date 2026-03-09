from sum_digits import sum_of_digits


def test_mixed_string_returns_digit_sum():
    '''
    This test ensures that if we have mixed string with characters and digits the result is correct
    For example: abc123, have the digit 123 cotained and the sum should be 6
    '''
    assert sum_of_digits("abc123") == 6


def test_no_digits_returns_zero():
    '''
    This test ensures that if we have a string that has no digits in it will still work
    For example: hello, have no digits cotained. So, the sum should be 0
    '''
    assert sum_of_digits("hello") == 0


def test_empty_string_returns_zero():
    '''
    This test ensures that if we have an empty string it will still work
    For example: "", is an empty string. So, the sum should be 0
    '''
    assert sum_of_digits("") == 0


def test_digits_only_returns_correct_sum():
    assert sum_of_digits("9876") == 30


def test_special_characters_are_ignored():
    assert sum_of_digits("!@#4$%5") == 9

def test_negative_numbers():
    assert sum_of_digits("10 and -3 and 7") == 14

def test_large_numbers():
    assert sum_of_digits("1d2f3add45678afef9012feMuhammedafa3456faeea789gsSRrg0") == 45

def test_zero_values(): 
    assert sum_of_digits("0a0b0c") == 0

def test_newline_separated(self):
    assert sum_of_digits("4\n8\n15\n16\n23\n42") == 108

def test_tab_separated(self):
    assert sum_of_digits("10\t20\t30") == 60


