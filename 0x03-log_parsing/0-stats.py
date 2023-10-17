#!/usr/bin/python3
"""Log parsing module"""
import sys

# Initialize variables to store metrics
total_size = 0
status_code_counts = {}

def process_log_lines():
    """
    Read log lines from standard input, process them, and print metrics.

    This function reads log lines line by line from standard input and computes
    two types of metrics:
    1. Total file size (sum of all file sizes encountered).
    2. Counts of status codes (200, 301, 400, 401, 403, 404, 405, and 500).

    It prints these metrics every 10 lines or when interrupted by CTRL+C.

    The input format for log lines should be as follows:
    <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
    If a line does not match this format, it will be skipped.

    The function doesn't return anything and runs indefinitely until interrupted.

    Args:
        None

    Returns:
        None
    """
    try:
        line_number = 0
        while True:
            line = sys.stdin.readline()
            if not line:
                break  # End of input

            line = line.strip()

            # Parse the line to extract the relevant information
            parts = line.split()
            if len(parts) != 7:
                continue  # Skip lines that don't match the expected format

            ip_address, date, request, status_code, file_size = parts

            try:
                file_size = int(file_size)
            except ValueError:
                continue  # Skip lines with non-integer file size

            # Update total file size
            total_size += file_size

            # Update status code counts
            if status_code in {"200", "301", "400", "401", "403", "404", "405", "500"}:
                if status_code not in status_code_counts:
                    status_code_counts[status_code] = 0
                status_code_counts[status_code] += 1

            line_number += 1

            # Print statistics every 10 lines or on keyboard interruption (CTRL+C)
            if line_number % 10 == 0:
                print("Total file size: File size:", total_size)
                for code in sorted(status_code_counts.keys(), key=lambda x: int(x)):
                    print(f"{code}: {status_code_counts[code]}")

    except KeyboardInterrupt:
        # Handle keyboard interruption (CTRL+C)
        print("Total file size: File size:", total_size)
        for code in sorted(status_code_counts.keys(), key=lambda x: int(x)):
            print(f"{code}: {status_code_counts[code}")

if __name__ == "__main__":
    process_log_lines()
