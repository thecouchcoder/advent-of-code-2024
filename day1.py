import sys
from collections import Counter


def calculate_total_distance(list1: list[int], list2: list[int]) -> int:
    list1.sort()
    list2.sort()

    result = sum(abs(i - j) for i, j in zip(list1, list2))
    return result


def calculate_similarity(list1: list[int], list2: list[int]) -> int:
    count = Counter(list2)
    result = sum(i * count[i] for i in list1)
    return result


def main():
    list1 = list()
    list2 = list()
    with open("./input/day1.txt", "r") as f:
        for line in f:
            nums = line.split("   ")
            list1.append(int(nums[0]))
            list2.append(int(nums[1]))

    print(calculate_total_distance(list1, list2))
    print(calculate_similarity(list1, list2))


if __name__ == "__main__":
    sys.exit(main())
