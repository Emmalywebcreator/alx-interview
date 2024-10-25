#!/usr/bin/python3
"""
Log Parsing Script

This script reads log data from standard input line by line, parses each line
to extract IP addresses, status codes, and file sizes, and then aggregates
statistics on the total file size and the count of each status code. The script
outputs statistics every 10 lines and upon a keyboard interrupt (CTRL + C).
"""

import sys
import re


def initialize_log():
    """Initialize log statistics."""
    return {
        'total_file_size': 0,
        'status_codes_count': {
            '200': 0,
            '301': 0,
            '400': 0,
            '401': 0,
            '403': 0,
            '404': 0,
            '405': 0,
            '500': 0
        },
        'line_count': 0
    }


def parse_log_line(line, log_stats):
    """
    Parse a log line using regex and update the log statistics.
    """
    log_pattern = re.compile(
        r'(?P<ip>\d{1,3}(\.\d{1,3}){3}) - \['
        r'.*\] "GET /projects/260 HTTP/1\.1" '
        r'(?P<status_code>\d{3}) (?P<file_size>\d+)'
    )

    match = log_pattern.match(line)
    if match:
        status_code = match.group('status_code')
        file_size = int(match.group('file_size'))

        '''Update total file size'''
        log_stats['total_file_size'] += file_size

        '''Update status code count if it's one of the expected ones'''
        if status_code in log_stats['status_codes_count']:
            log_stats['status_codes_count'][status_code] += 1


def print_stats(log_stats):
    """
    Print the current log statistics.
    """
    print(f"File size: {log_stats['total_file_size']}")
    for code in sorted(log_stats['status_codes_count'].keys()):
        if log_stats['status_codes_count'][code] > 0:
            print(f"{code}: {log_stats['status_codes_count'][code]}")


def main():
    """Main function to read stdin and compute statistics."""
    log_stats = initialize_log()

    try:
        for line in sys.stdin:
            log_stats['line_count'] += 1
            parse_log_line(line, log_stats)

            # Print stats every 10 lines
            if log_stats['line_count'] % 10 == 0:
                print_stats(log_stats)

    except KeyboardInterrupt:
        print_stats(log_stats)
        sys.exit(0)


if __name__ == "__main__":
    main()
