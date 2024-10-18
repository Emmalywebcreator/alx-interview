#!/usr/bin/env python3
"""
Module that calculate the minimum number of operation
"""


def minOperations(n):
    """
    Calculate the fewest number of operations to result in
    exactly n 'H' characters.
    """
    if n <= 1:
        return 0
    operations = 0
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
    return operations

