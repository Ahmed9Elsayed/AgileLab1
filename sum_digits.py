def sum_of_digits(s):
    """Calculate the sum of all digit characters in a given string.

    Iterates through each character in the string, identifies numeric
    digits (0-9), and returns their sum. Non-digit characters are ignored.

    Args:
        s (str): The input string to process.

    Returns:
        int: The sum of all digit characters found in the string.
             Returns 0 if no digits are present.

    Examples:
        >>> sum_of_digits("abc123")
        6
        >>> sum_of_digits("hello")
        0
        >>> sum_of_digits("")
        0
    """
    return sum(int(ch) for ch in s if ch.isdigit())