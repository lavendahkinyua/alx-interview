#!/usr/bin/python3

"""
Metrics Calculator

This script reads stdin line by line and computes metrics.

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size> 
(if the format is not this one, the line must be skipped)

After every 10 lines and/or a keyboard interruption (CTRL + C), it prints these statistics from the beginning:
Total file size: File size: <total size>
where <total size> is the sum of all previous <file size> (see input format above)

Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405, and 500
if a status code doesn’t appear or is not an integer, it doesn't print anything for this status code.
format: <status code>: <number>
status codes should be printed in ascending order

Warning: In this sample, you will have random values - it’s normal to not have the same output as this one.
"""

import sys

def print_metrics(status_code_counts, total_file_size):
    """
    Print the computed metrics.

    Args:
        status_code_counts (dict): A dictionary containing status code counts.
        total_file_size (int): The total file size.

    Returns:
        None
    """
    print("Total file size:", total_file_size)
    for code in sorted(status_code_counts.keys(), key=lambda x: int(x)):
        count = status_code_counts[code]
        if count > 0:
            print(f"{code}: {count}")

def main():
    total_file_size = 0
    status_code_counts = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
    }
    line_counter = 0

    try:
        for line in sys.stdin:
            line_parts = line.split()

            if len(line_parts) == 7:
                file_size = line_parts[-1]
                status_code = line_parts[-2]

                if status_code in status_code_counts:
                    status_code_counts[status_code] += 1

                try:
                    total_file_size += int(file_size)
                except ValueError:
                    pass

                line_counter += 1

                if line_counter == 10:
                    print_metrics(status_code_counts, total_file_size)
                    line_counter = 0

    except KeyboardInterrupt:
        print_metrics(status_code_counts, total_file_size)

if __name__ == "__main__":
    main()


