#!/usr/bin/python3
"""Log parsing"""
import sys

def print_stats(status_codes, file_size):
    """Prints the stats"""
    print("File size: {}".format(file_size))
    for code in sorted(status_codes.keys()):
        count = status_codes[code]
        if count > 0:
            print("{}: {}".format(code, count))

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
        for line in sys.stdin:
            if not line.strip():
                continue  # Skip empty lines

            parts = line.split()
            if len(parts) >= 7:
                code = parts[-2]
                if code in status_codes:
                    file_size += int(parts[-1])
                    status_codes[code] += 1
                    counter += 1
                    if counter == 10:
                        print_stats(status_codes, file_size)
                        counter = 0

except KeyboardInterrupt:
    print_stats(status_codes, file_size)
    raise
except EOFError:
    pass
