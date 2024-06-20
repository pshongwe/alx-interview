#!/usr/bin/python3
"""0-stats"""
import sys
import signal


class LogParser:
    """0-stats"""
    def __init__(self):
        """0-stats"""
        self.total_size = 0
        self.status_codes = {
                 '200': 0,
                 '301': 0,
                 '400': 0,
                 '401': 0,
                 '403': 0,
                 '404': 0,
                 '405': 0,
                 '500': 0,
        }
        self.line_count = 0

    def print_stats(self):
        """0-stats"""
        print(f"File size: {self.total_size}")
        for code in sorted(self.status_codes.keys()):
            if self.status_codes[code] > 0:
                print(f"{code}: {self.status_codes[code]}")

    def signal_handler(self, sig, frame):
        """0-stats"""
        self.print_stats()
        sys.exit(0)

    def process_line(self, line):
        """0-stats"""
        try:
            parts = line.split()
            if len(parts) != 7:
                return
            ip, dash, date, get, url, status, size = parts
            if get != '"GET':
                return
            status = int(status)
            size = int(size)

            self.total_size += size
            if status in self.status_codes:
                self.status_codes[status] += 1

            self.line_count += 1
            if self.line_count % 10 == 0:
                self.print_stats()
        except ValueError:
            return

    def run(self):
        """0-stats"""
        signal.signal(signal.SIGINT, self.signal_handler)
        for line in sys.stdin:
            self.process_line(line)
        self.print_stats()


if __name__ == "__main__":
    parser = LogParser()
    parser.run()
