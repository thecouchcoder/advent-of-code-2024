from day2 import analyze_report, read_reports, validate


def test_valid():
    result = analyze_report([7, 6, 4, 2, 1])
    assert result is True


def test_equal():
    result = validate(0, 1)
    assert result is False


def test_diff_more_than_3():
    result = validate(4, 1)
    assert result is False
    result = validate(-4, 1)
    assert result is False


def test_direction_change():
    result = validate(-1, -1)
    assert result is False

    result = validate(1, 1)
    assert result is False


def test_sample():
    count = read_reports("./input/day2_sample.txt")
    assert count is 4

def test_failing_test_case():
    assert analyze_report([32, 32, 33, 36, 38, 40]) is True

def test_failing_test_case_2():
    assert analyze_report([44, 47, 48, 49, 48]) is True

def test_correctly_dampens_direction():
    assert analyze_report([9,8,10,11,12,13]) is True

def test_can_dampen_current():
    assert analyze_report([31, 34, 33, 36, 38, 40]) is True

def test_can_dampen_prev():
    assert analyze_report([31, 34, 32, 36, 38, 40]) is True
