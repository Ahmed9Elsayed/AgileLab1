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
    '''
    This test ensures that a string containing only digits returns the correct sum.
    For example: "9876" should return 9+8+7+6 = 30
    '''
    assert sum_of_digits("9876") == 30


def test_special_characters_are_ignored():
    '''
    This test ensures that special characters are ignored and only digits are summed.
    For example: "!@#4$%5" contains digits 4 and 5, so the sum should be 9
    '''
    assert sum_of_digits("!@#4$%5") == 9

def test_negative_numbers():
    '''
    This test ensures that the minus sign is ignored and only individual digits are summed.
    For example: "10 and -3 and 7" has digits 1, 0, 3, 7, so the sum should be 11
    '''
    assert sum_of_digits("10 and -3 and 7") == 11

def test_large_numbers():
    '''
    This test ensures that the function handles long strings with many mixed characters correctly.
    The string contains digits 1-9, 0, repeated twice, so the sum should be 90
    '''
    assert sum_of_digits("1d2f3add45678afef9012feMuhammedafa3456faeea789gsSRrg0") == (1+2+3+4+5+6+7+8+9+0+1+2+3+4+5+6+7+8+9+0)

def test_zero_values():
    '''
    This test ensures that a string containing only zero digits returns 0.
    For example: "0a0b0c" has digits 0, 0, 0, so the sum should be 0
    '''
    assert sum_of_digits("0a0b0c") == 0

def test_newline_separated():
    '''
    This test ensures that newline characters are treated as separators and only digits are summed.
    For example: "4\\n8\\n15\\n16\\n23\\n42" sums individual digits 4+8+1+5+1+6+2+3+4+2 = 36
    '''
    assert sum_of_digits("4\n8\n15\n16\n23\n42") == (4+8+1+5+1+6+2+3+4+2)

def test_tab_separated():
    '''
    This test ensures that tab characters are treated as separators and only digits are summed.
    For example: "10\\t20\\t30" sums individual digits 1+0+2+0+3+0 = 6
    '''
    assert sum_of_digits("10\t20\t30") == (1+0+2+0+3+0)

