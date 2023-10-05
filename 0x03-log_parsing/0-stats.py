#!/usr/bin/python3
"""Log parsing"""

import sys

def print_stats(status_codes, file_size):
    """Prints the stats"""
    print("File size: {}".format(file_size))
    for key, value in sorted(status_codes.items()):
        if value != 0:
            print("{}: {}".format(key, value))

file_size = 0
code = 0
counter = 0
status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}

try:
    for line in sys.stdin:
        counter += 1
        data = line.split()
        if len(data) >= 8:  # Check for at least 8 elements in the data list
            file_size += int(data[-1])
            code = data[-2]
            if code in status_codes:
                status_codes[code] += 1
        if counter % 10 == 0:
            print_stats(status_codes, file_size)
except KeyboardInterrupt:
    print_stats(status_codes, file_size)
    raise
print_stats(status_codes, file_size)
