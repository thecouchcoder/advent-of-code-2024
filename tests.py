from day1 import calculate_total_distance


def test_day1_sample():
    list1 = [3, 4, 2, 1, 3, 3]
    list2 = [4, 3, 5, 3, 9, 3]

    result = calculate_total_distance(list1, list2)
    assert result == 11
