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
                if analyze_report(report):
                    result += 1
            except Exception as e:
                print(report)
                continue
    return result

def analyze_report(report: list[int]) -> bool:
    dampened = False
    stack = deque()
    direction = Direction.DOWN if report[0] > report[1] else Direction.UP
    for i in range(len(report)):
        if len(stack) == 0:
            stack.append(report[i])
            continue
        # validate stack and current
        is_valid = validate(stack[-1], report[i], direction)
        if is_valid:
            stack.append(report[i])
            continue
        if not is_valid and dampened:
            return False

        if can_skip(stack, report, i, direction):
            dampened = True
            if len(stack) == 1:
                direction = Direction.DOWN if stack[-1] > report[i+1] else Direction.UP
            continue

        stack.pop()
        dampened = True
        if len(stack) == 1:
            direction = Direction.DOWN if stack[-1] > report[i+1] else Direction.UP
        i = i-1
        # stack empty? fix direction
        # validate stack and current
        # if valid append and continue
        # else return false

    return True

def can_skip(stack, report, index, direction):
    if index == len(report) - 1 or validate(stack[-1], report[index + 1], direction):
        return True
    return False

def validate(n1: int, n2: int, direction: Direction):
    diff = n1 - n2
    return not (
        diff == 0 or abs(diff) > 3 or (diff > 0 and direction == Direction.UP) or (diff < 0 and direction == Direction.DOWN)
    )


def main():
    print(read_reports("./input/day2.txt"))


if __name__ == "__main__":
    sys.exit(main())
