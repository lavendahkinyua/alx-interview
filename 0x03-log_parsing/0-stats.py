#!/usr/

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
    print("Total file size: File size:", total_file_size)
    for code, count in sorted(status_code_counts.items(), key=lambda x: int(x[0])):
        if count != 0:
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
                file_size = int(line_parts[-1])
                status_code = line_parts[-2]

                total_file_size += file_size

                if status_code in status_code_counts:
                    status_code_counts[status_code] += 1

                line_counter += 1

                if line_counter == 10:
                    print_metrics(status_code_counts, total_file_size)
                    line_counter = 0

    except KeyboardInterrupt:
        print_metrics(status_code_counts, total_file_size)

if __name__ == "__main__":
    main()
