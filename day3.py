import re
import sys


def mul_part1(memory: str) -> int:
    regex = r"mul\(([0-9]+),([0-9]+)\)"
    matches = re.findall(regex, memory)
    return sum(int(i)*int(j) for i,j in matches)

def mul_part2(memory: str) -> int:
    memory = "do()" + memory.replace("\n","") + "don't()"
    enabled = r"do\(\).*?mul\(\d+,[0-9]+\).*?don't\(\)"
    mul = r"mul\(([0-9]+),([0-9]+)\)"
    inputs = re.findall(enabled, memory)
    print(inputs)
    matches = [re.findall(mul, i) for i in inputs]
    matches = [x for xs in matches for x in xs]
    print(matches)
    return sum(int(i)*int(j) for i,j in matches)

def main():
    with open("./input/day3.txt", "r") as f:
        contents = f.read()
        print(mul_part1(contents))
        print(mul_part2(contents))

if __name__ == "__main__":
    sys.exit(main())