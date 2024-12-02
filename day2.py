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
    stack = deque()
    direction = Direction.DOWN if report[0] > report[1] else Direction.UP
    i = 0
    while i < len(report):
        if len(stack) == 0:
            stack.append(report[i])
            i += 1
            continue
        # validate stack and current
        is_valid = validate(stack[-1], report[i], direction)
        if is_valid:
            stack.append(report[i])
            i += 1
            continue
        if not is_valid and dampened:
            return False

        if should_backtrack(report, i):
            stack.clear()
            stack.append(report[1])
            stack.append(report[2])
            i = 3
            continue
        if can_skip(stack, report, i, direction):
            dampened = True
            # if we only have one in our stack, the direction could change
            if len(stack) == 1:
                direction = Direction.DOWN if stack[-1] > report[i+1] else Direction.UP
            i += 1
            continue

        stack.pop()
        dampened = True
        # if popped something off, leaving only one, the direction could change
        if len(stack) == 1:
            direction = Direction.DOWN if stack[-1] > report[i] else Direction.UP
        # don't increment we want to reevaluate with the value popped off

    return True

def should_backtrack(report, i):
    new_direction = Direction.DOWN if report[1] > report[2] else Direction.UP
    return (i == 1 or i ==2) and validate(report[1], report[2], new_direction) and validate(report[2], report[3], new_direction)


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
