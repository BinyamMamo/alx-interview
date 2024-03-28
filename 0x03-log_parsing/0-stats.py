#!/usr/bin/python3
"""
Task 0. Log parsing
Create a Python script that reads input line by line,
computes metrics, and prints statistics.
"""
import sys


if __name__ == "__main__":
    TOTAL_SIZE = 0
    STATUS_CODES = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0,
    }
    LINE_COUNT = 0

    def print_stats():
        """
        Prints the computed statistics:
        - Total file size
        - Number of lines by status code (in ascending order)
        """
        print(f"File size: {TOTAL_SIZE}")
        for key, value in sorted(STATUS_CODES.items()):
            if value:
                print(f"{key}: {value}")

    try:
        for line in sys.stdin:
            LINE_COUNT += 1
            data = line.split()
            try:
                status_code = data[-2]
                if status_code in STATUS_CODES:
                    STATUS_CODES[status_code] += 1
            except IndexError:
                pass
            try:
                TOTAL_SIZE += int(data[-1])
            except ValueError:
                pass
            if LINE_COUNT % 10 == 0:
                print_stats()

    except KeyboardInterrupt:
        print_stats()
        sys.exit(0)
