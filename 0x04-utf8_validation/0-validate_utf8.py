#!/ussr/bin/python3
"""
Utf8 that valid a dataset
"""


def validUTF8(data):
    """ Convert integer to binary string, padded to 8 bits"""
    num_bytes = 0

    for num in data:
        byt_num = format(num_bytes, '08B')

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
    return num_bytes == 0
