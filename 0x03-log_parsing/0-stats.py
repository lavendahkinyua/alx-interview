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
counter = 0
status_codes = {
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
    while True:
        try:
            line = input()  # Read a line from standard input
            parsed_line = line.split()
            if len(parsed_line) >= 7:  # Check for the correct format
                file_size += int(parsed_line[-1])
                code = parsed_line[-2]
                if code in status_codes:
                    status_codes[code] += 1
                counter += 1
                if counter == 10:
                    print_stats(status_codes, file_size)
                    counter = 0
        except KeyboardInterrupt:
            print_stats(status_codes, file_size)
            raise
        except Exception as e:
            pass

except EOFError:
    pass
except KeyboardInterrupt:
    print_stats(status_codes, file_size)
