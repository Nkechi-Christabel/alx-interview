#!/usr/bin/python3
"""This script determines if a given data set represents a valid
UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determine if the given data set represents a valid UTF-8 encoding.

    Parameters:
    - data (list of integers): A list of integers representing bytes of data.

    Returns:
    - bool: True if data is a valid UTF-8 encoding, else False.

    A character in UTF-8 can be 1 to 4 bytes long.
    Each integer represents 1 byte of data, therefore only the 8 least
    significant bits of each integer are considered.
    """

    # Iterate through the list of integers representing the data
    i = 0
    while i < len(data):
        # Check the number of bytes in the current character
        num_bytes = 0
        # Single-byte character (starts with 0)
        if (data[i] & 0b10000000) == 0:
            num_bytes = 1
        elif (data[i] & 0b11100000) == 0b11000000:  # Two-byte character
            num_bytes = 2
        elif (data[i] & 0b11110000) == 0b11100000:  # Three-byte character
            num_bytes = 3
        elif (data[i] & 0b11111000) == 0b11110000:  # Four-byte character
            num_bytes = 4
        else:
            return False  # Invalid byte sequence

        # Check if there are enough bytes left in the data
        if i + num_bytes > len(data):
            return False

        # Verify that the following bytes in the sequence start with '10'
        for j in range(i + 1, i + num_bytes):
            if (data[j] & 0b11000000) != 0b10000000:
                return False

        # Move to the next character
        i += num_bytes

    # All characters are valid UTF-8
    return True
