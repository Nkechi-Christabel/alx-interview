#!/usr/bin/python3

import sys
import signal
import re


def parse_line(line):
    """
    Parse a line of input to extract the status code and file size.
    If the line does not match the specified format, return None.
    """
    pattern = r'^\S+ - \[.*\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)'
    match = re.match(pattern, line)
    if match:
        status_code, file_size = map(int, match.groups())
        return status_code, file_size
    else:
        return None


def print_statistics(total_size, status_counts):
    """
    Print the total file size and the number of lines by status code.
    """
    print(f"File size: {total_size}")
    for status_code in sorted(status_counts.keys()):
        print(f"{status_code}: {status_counts[status_code]}")


def signal_handler(sig, frame):
    """
    Handle keyboard interruption (CTRL + C) by printing statistics.
    """
    print_statistics(total_size, status_counts)
    sys.exit(0)

if __name__ == "__main__":
    total_size = 0
    status_counts = {}
    line_count = 0

    signal.signal(signal.SIGINT, signal_handler)

    for line in sys.stdin:
        line = line.strip()
        parsed_line = parse_line(line)
        if parsed_line:
            status_code, file_size = parsed_line
            total_size += file_size
            status_counts[status_code] = status_counts.get(status_code, 0) + 1
            line_count += 1

            if line_count % 10 == 0:
                print_statistics(total_size, status_counts)
    # Print statistics for remaining lines
    if line_count % 10 != 0:
        print_statistics(total_size, status_counts)
