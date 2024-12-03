from day3 import mul_part1, mul_part2


def test_example_input_part1():
    input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    result = mul_part1(input)
    assert result == 161

def test_example_input_part2():
    input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    result = mul_part2(input)
    assert result == 48

def test_example_input_part2_with_newline():
    input = """do()mul(2,4)
    don't()"""
    result = mul_part2(input)
    assert result == 8