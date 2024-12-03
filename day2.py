import sys
from collections import deque
from enum import Enum
from typing import Optional


class Direction(Enum):
    UP = 1
    DOWN = 2

def read_reports(path: str) -> int:
    result = 0
    with open(path, "r") as f:
        for line in f:
            report = [int(item) for item in line.split(" ")]
            try:
                res = analyze_report(report)
                color = '\033[31m' if not res else '\033[32m'
                print(f"{color}{report}")
                if res:
                    result += 1
            except Exception as e:
                print(report)
                continue
    return result

def analyze_report(report: list[int]) -> bool:
    dampened = False
    ok = True
    for i in range(len(report) - 1):
        ok = is_valid(report[i], report[i+1])
        if not ok:
            break

    return ok and sorted(report) == report


def is_valid(n1: int, n2: int):
        return 1 <= abs(n1 - n2) >= 3


def main():
    print(read_reports("./input/day2.txt"))


if __name__ == "__main__":
    sys.exit(main())
