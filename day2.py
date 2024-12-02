import sys
from collections import deque
from inspect import stack


def read_reports(path: str) -> int:
    result = 0
    with open(path, "r") as f:
        for line in f:
            report = [int(item) for item in line.split(" ")]
            try:
                analyze_report(report)
                if analyze_report(report):
                    result += 1
            except Exception as e:
                print(report)
                continue
    return result

def analyze_report(report: list[int]) -> bool:
    dampened = False
    stack = deque([report[0]])
    direction = 1 if report[0] - report[1] < 0 else -1
    for i in range(len(report)):
        if i == 0:
            continue
        diff = stack[len(stack)-1] - report[i]
        is_valid = validate(diff, direction)
        if is_valid:
            stack.append(report[i])
        if not is_valid and not dampened:
            dampened = True
            # keep previous, discard current
            if i == len(report)-1 or validate(stack[len(stack)-1]-report[i+1], direction):
                continue
            # discard previous, validate if current fixes it
            else:
                stack.pop()
                if len(stack) != 0:
                    diff = stack[len(stack)-1] - report[i]
                    if len(stack) == 1:
                        direction = 1 if report[i] - report[i+1] < 0 else -1
                    is_valid = validate(diff, direction)
                else:
                    is_valid = True
                    direction = 1 if report[i] - report[i+1] < 0 else -1
                stack.append(report[i])
        if not is_valid and dampened:
            return False
    return True


def validate(diff: int, direction: int):
    return not (
        diff == 0 or abs(diff) > 3 or (diff > 0 and direction == 1) or (diff < 0 and direction == -1)
    )


def main():
    print(read_reports("./input/day2.txt"))


if __name__ == "__main__":
    sys.exit(main())
