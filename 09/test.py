import pytest
from aoc import *


@pytest.mark.parametrize("input_list, input_prefix, input_index, expected", [
	([35, 20, 15, 25, 47, 40], 5, 5, True),
	([35, 20, 15, 25, 47, 40], 5, 4, True),
	([35, 20, 15, 25, 47, 40], 3, 4, False),
	([49, 1, 11, 24, 15, 16, 4, 20, 5, 25, 31, 10, 40, 9, 13, 36, 17, 6, 58, 19, 32, 81], 20, 20, True),
	([21, 32, 30, 37, 26, 34, 18, 3, 49, 1, 11, 24, 15, 16, 4, 20, 5, 25, 31, 10, 40, 9, 13, 36, 17, 6, 58, 19, 32, 81], 25, 29, True),
])
def test_is_valid(input_list, input_prefix, input_index, expected):
	assert is_valid(input_list, input_prefix, input_index) == expected


@pytest.mark.parametrize("test_input, expected", [
	("source_01.txt", [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576])
])
def test_list_from_file(test_input, expected):
	assert list_from_file(test_input) == expected


@pytest.mark.parametrize("test_input, input_offset, target_num, expected, expected_min, expected_max", [
	([35, 20, 15, 25, 47, 40, 62, 55], 0, 40, False, 20, 35),
	([35, 20, 15, 25, 47, 40, 62, 55], 1, 60, True, 15, 25),
	([35, 20, 15, 25, 47, 40, 62, 55], 1, 61, False, 15, 47),
	([35, 20, 15, 25, 47, 40, 62, 55], 1, 1000, False, 15, 62),
	([35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576], 2, 127, True, 15, 47),
])
def test_sub_sum(test_input, input_offset, target_num, expected, expected_min, expected_max):
	matches, num_min, num_max = sub_sum(test_input, input_offset, target_num)
	assert num_min == expected_min
	assert num_max == expected_max
	assert matches == expected


@pytest.mark.parametrize("test_input, expected", [("source_01.txt", 127)])
def test_answer_1(test_input, expected):
	assert answer_1(test_input, prefix=5) == expected


@pytest.mark.parametrize("test_input, expected", [("source_01.txt", 62)])
def test_answer_2(test_input, expected):
	assert answer_2(test_input, prefix=5) == expected


