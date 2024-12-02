from day2 import analyze_report, read_reports


def test_day2_valid():
    result = analyze_report([7, 6, 4, 2, 1])
    assert result is True


def test_day2_diff():
    result = analyze_report([7, 7, 4, 2, 1])
    assert result is False


def test_day2_diff_more_than_3():
    result = analyze_report([7, 3, 2, 1])
    assert result is False


def test_day2_direction_change():
    result = analyze_report([7, 8, 4, 2, 1])
    assert result is False

    result = analyze_report([1, 2, 3, 4, 3, 5])
    assert result is False


def test_day2_sample():
    count = read_reports("./input/day2_sample.txt")
    assert count is 2
