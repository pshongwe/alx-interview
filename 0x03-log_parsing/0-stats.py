#!/usr/bin/python3
"""
Log parsing script that reads stdin line by line and computes metrics.

"""
import sys
import signal
import re


class LogParser:
    """Class to parse log entries and compute statistics."""
    def __init__(self):
        """Initialize the LogParser with default values."""
        self.total_size = 0
        self.status_codes = {
            200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0
        }
        self.line_count = 0
        self.log_pattern = re.compile(
            r'(?P<ip>\S+) - \[(?P<date>.*?)\] "GET /projects/260 HTTP/1.1" '
            r'(?P<status>\d{3}) (?P<size>\d+)'
        )

    def print_stats(self):
        """Print the current statistics of the log parsing."""
        print(f"File size: {self.total_size}")
        for code in sorted(self.status_codes.keys()):
            if self.status_codes[code] > 0:
                print(f"{code}: {self.status_codes[code]}")

    def signal_handler(self, sig, frame):
        """Handle SIGINT (Ctrl+C) to print statistics and exit."""
        self.print_stats()
        sys.exit(0)

    def process_line(self, line):
        """
        Process a single line of the log.

        Args:
            line (str): A single log entry.

        Returns:
            None
        """
        match = self.log_pattern.match(line)
        if match:
            try:
                status = int(match.group('status'))
                size = int(match.group('size'))
                self.total_size += size
                if status in self.status_codes:
                    self.status_codes[status] += 1
                self.line_count += 1
                if self.line_count % 10 == 0:
                    self.print_stats()
            except ValueError:
                return

    def run(self):
        """Run the log parser to read from stdin and process lines."""
        signal.signal(signal.SIGINT, self.signal_handler)
        for line in sys.stdin:
            self.process_line(line)
        self.print_stats()


if __name__ == "__main__":
    parser = LogParser()
    parser.run()
