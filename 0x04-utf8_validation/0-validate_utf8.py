#!/usr/bin/python3
"""
UTF-8 Validation for a dataset
"""


def validUTF8(data):
    """Check if a dataset represents a valid UTF-8 encoding."""
    num_bytes = 0

    for byte in data:
        byt_num = format(byte, '08b')

        if num_bytes == 0:
            if byt_num.startswith('0'):
                continue
            elif byt_num.startswith('110'):
                num_bytes = 1
            elif byt_num.startswith('1110'):
                num_bytes = 2
            elif byt_num.startswith('11110'):
                num_bytes = 3
            else:
                return False
        else:
            if not byt_num.startswith('10'):
                return False
            num_bytes -= 1

    return num_bytes == 0
