#!/usr/bin/python3
"""a method that determines if a given data set represents a valid UTF-8 encoding"""


def validUTF8(data):
    """a method that determines if a given data set represents a valid UTF-8 encoding"""
    num_bytes = 0
    for num in data:
        bin_rep = format(num, '#010b')[-8:]
        if num_bytes == 0:
            for bit in bin_rep:
                if bit == '0':
                    break
                num_bytes += 1
            if num_bytes == 0:
                continue
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if not (bin_rep[0] == '1' and bin_rep[1] == '0'):
                return False
        num_bytes -= 1
    return num_bytes == 0