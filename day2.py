import sys


def read_reports(path: str) -> int:
    result = 0
    with open(path, "r") as f:
        for line in f:
            report = [int(item) for item in line.split(" ")]
            if analyze_report(report):
                result += 1
    return result


def analyze_report(report: list[int]) -> bool:
    direction = -1 if report[0] - report[1] < 0 else 1  # -1 for down, 1 for up
    for i, j in zip(report, report[1:]):
        diff = i - j
        is_valid = validate(diff, direction)
        if not is_valid:
            return False
    return True


def validate(diff: int, direction: int):
    return not (
        diff == 0 or abs(diff) > 3 or (diff > 0 > direction) or (diff < 0 < direction)
    )


def main():
    print(read_reports("./input/day2.txt"))


if __name__ == "__main__":
    sys.exit(main())
