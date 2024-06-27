#!/usr/bin/python3
"""validUTF8"""


def validUTF8(data):
    """
    Determine if a given data set represents
    a valid UTF-8 encoding.
    Parameters:
    data (list of int): The data set to check,
    each integer represents 1 byte of data.
    Returns:
    bool: True if data is a valid UTF-8 encoding, else False.
    """
    num_bytes = 0

    for num in data:
        byte = num & 0xFF  # Get the 8 least significant bits
        if num_bytes == 0:
            if byte >> 7 == 0:  # 1-byte character
                continue
            elif byte >> 5 == 0b110:  # 2-byte character
                num_bytes = 1
            elif byte >> 4 == 0b1110:  # 3-byte character
                num_bytes = 2
            elif byte >> 3 == 0b11110:  # 4-byte character
                num_bytes = 3
            else:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0


if __name__ == "__main__":
    validUTF8 = __import__('0-validate_utf8').validUTF8

    data = [65]
    print(validUTF8(data))  # True

    data = [80, 121, 116, 104, 111, 110,
            32, 105, 115, 32, 99, 111, 111, 108, 33]
    print(validUTF8(data))  # True

    data = [229, 65, 127, 256]
    print(validUTF8(data))  # False
