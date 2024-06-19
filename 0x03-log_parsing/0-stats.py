#!/usr/bin/python3
"""
A script to parse and analyze HTTP request logs.
"""
import sys
import re
import signal


total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0,
                      403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


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
            'status': int(match.group('status')),
            'size': int(match.group('size'))
        }
    return None


def print_metrics():
    """
    Prints the accumulated metrics.
    """
    print(f"File size: {total_file_size}")
    for status_code in sorted(status_code_counts):
        count = status_code_counts[status_code]
        if count > 0:
            print(f"{status_code}: {count}")


def signal_handler(sig, frame):
    """
    Handles interrupt signals to print metrics before exiting.
    """
    print_metrics()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


try:
    while True:
        line = sys.stdin.readline().strip()
        if not line:
            break
        metrics = parse_log_line(line)
        if metrics:
            total_file_size += metrics['size']
            status_code = metrics['status']
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1
            line_count += 1
            if line_count % 10 == 0:
                print_metrics()
except KeyboardInterrupt:
    print_metrics()
    sys.exit(0)
