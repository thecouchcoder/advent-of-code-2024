import sys
from collections import deque
from copy import deepcopy
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
    for i in range(len(report)):
        copy = deepcopy(report)
        copy = copy[:i] + copy[i+1:]


        always_inc = True
        always_dec = True
        is_ok = True
        for j in range(len(copy)-1):
            if copy[j] <= copy[j+1]:
                always_inc = False
            if copy[j] >= copy[j+1]:
                always_dec = False
            if not is_valid(copy[j], copy[j+1]) or (always_dec is False and always_inc is False):
                is_ok = False
                break
        if is_ok:
            return True
    return False


def is_valid(n1: int, n2: int):
        return not (1 < abs(n1 - n2) > 3)


def main():
    print(read_reports("./input/day2.txt"))


if __name__ == "__main__":
    sys.exit(main())
