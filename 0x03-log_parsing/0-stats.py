#!/usr/bin/python3

"""
Metrics Calculator

This script reads stdin line by line and computes metrics.

Input format:<IP Address>[<date>] <status code><file size>
(if the format is not this one, the line must be skipped)

After every 10 lines,keyboard interrupt print statistics since the beginning
Total file size: File size: <total size>
where <total size>is the sum of all previous<file size>(see input format above)

Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405, and 500
status code doesn’t appear, not an integer, it doesn't print anything.
format: <status code>: <number>
status codes should be printed in ascending order

Warning: In this sample, you will have random values.
"""
import sys


def print_msg(codes, file_size):
    print("File size: {}".format(file_size))
    for key, val in sorted(codes.items()):
        if val != 0:
            print("{}: {}".format(key, val))


file_size = 0
code = 0
count_lines = 0
codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

try:
    for line in sys.stdin:
        parsed_line = line.split()
        parsed_line = parsed_line[::-1]

        if len(parsed_line) > 2:
            count_lines += 1

            if count_lines <= 10:
                file_size += int(parsed_line[0])
                code = parsed_line[1]

                if (code in codes.keys()):
                    codes[code] += 1

            if (count_lines == 10):
                print_msg(codes, file_size)
                count_lines = 0

finally:
    print_msg(codes, file_size)
