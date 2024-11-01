#!/ussr/bin/python3
"""
Utf8 that valid a dataset
"""


def validUTF8(data):
    """ Convert integer to binary string, padded to 8 bits"""

    for byte in data:
        byt_num = format(byte, '08b')

        if byt_num.startswith('0'):
            continue
        elif byt_num.startswith('110'):
            continue
        elif byt_num.startswith('1110'):
            continue
        elif byt_num.startswith('11110'):
            continue
        else:
            return False
    return True
