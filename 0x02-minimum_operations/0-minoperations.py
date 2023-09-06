#!/usr/bin/python3
"""Minimum operations module"""


def minOperations(n):
    """Calc fewest num of operations to result in exactly n H characters """
    if n <= 1:
        return 0
    div = 2
    operations = 0
    while n > 1:
        if n % div == 0:
            operations += div
            n /= div
        else:
            div += 1
    return operations
