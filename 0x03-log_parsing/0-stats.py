#!/usr/bin/python3
"""
A script to parse and analyze HTTP request logs.
"""
import sys
import re


def parse_log_line(line):
    """
    Parses a line from the log and extracts useful metrics.
    Args:
        line (str): A single line from the log.
    Returns:
        dict: A dictionary containing the status code and file size.
    """
    log_pattern = (
        r'(?P<ip>\d{1,3}(?:\.\d{1,3}){3}) - \[(?P<date>[^\]]+)\] '
        r'"GET /projects/260 HTTP/1\.1" (?P<status>\d{3}) (?P<size>\d+)'
    )
    match = re.match(log_pattern, line)
    if match:
        return {
            'status_code': int(match.group('status')),
            'file_size': int(match.group('size'))
        }
    return None


def print_metrics(total_file_size, status_code_counts):
    """
    Prints the accumulated metrics.
    """
    print('File size: {:d}'.format(total_file_size), flush=True)
    for status_code in sorted(status_code_counts):
        count = status_code_counts[status_code]
        if count > 0:
            print('{:s}: {:d}'.format(status_code, num), flush=True)


def main():
    """main"""
    total_file_size = 0
    status_code_counts = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0,
    }
    line_count = 0
    try:
        while True:
            line = input()
            if not line:
                break
            metrics = parse_log_line(line)
            if metrics:
                total_file_size += metrics['file_size']
                status_code = metrics['status_code']
                if status_code in status_code_counts:
                    status_code_counts[status_code] += 1
                line_count += 1
                if line_count % 10 == 0:
                    print_metrics(total_file_size, status_code_counts)
    except KeyboardInterrupt:
        print_metrics(total_file_size, status_code_counts)
        sys.exit(0)


if __name__ == '__main__':
    main()
