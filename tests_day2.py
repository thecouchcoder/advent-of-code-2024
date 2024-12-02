from day2 import analyze_report, read_reports, validate, Direction


def test_given_diff_greater_than_3_when_validate():
    result = validate(10, 4, Direction.UP)
    assert result is False
    result = validate(4, 10, Direction.UP)
    assert result is False

def test_given_diff_is_equal_when_validate():
    result = validate(1,1, Direction.UP)
    assert result is False

def test_given_direction_change_when_validate():
    result = validate(6,7, Direction.DOWN)
    assert result is False

    result = validate(7,6, Direction.UP)
    assert result is False

def test_given_valid_when_validate():
    result = validate(7,6, Direction.DOWN)
    assert result is True
    result = validate(6,7, Direction.UP)
    assert result is True
    result = validate(7,4, Direction.DOWN)
    assert result is True
    result = validate(4,7, Direction.UP)
    assert result is True

def test_sample():
    count = read_reports("./input/day2_sample.txt")
    assert count is 4

def test_valid():
    result = analyze_report([7, 6, 4, 2, 1])
    assert result is True

def test_can_skip():
    assert analyze_report([31, 34, 33, 37, 38, 40]) is True

def test_can_pop():
    assert analyze_report([32, 35, 38, 36, 37, 40]) is True

def test_can_skip_equal():
    assert analyze_report([31, 32, 33, 33, 35, 36]) is True

def test_can_fix_first_element():
    assert analyze_report([40, 32, 31, 30, 29]) is True

def test_can_fix_last_element():
    assert analyze_report([29, 30, 31, 32, 40]) is True

def test_can_change_direction():
    assert analyze_report([29, 30, 28, 27, 26]) is True

# def test_failing_test_case():
#     assert analyze_report([32, 32, 33, 36, 38, 40]) is True
#
# def test_failing_test_case_2():
#     assert analyze_report([44, 47, 48, 49, 48]) is True
#
# def test_correctly_dampens_direction():
#     assert analyze_report([9,8,10,11,12,13]) is True
#

