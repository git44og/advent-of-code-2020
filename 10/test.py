import pytest
from aoc import *


@pytest.mark.parametrize("test_input_base, test_input_extension, expected", [
	([], [1], [[1]]),
	([], [1, 1], [[1, 1], [2]]),
	([], [1, 2, 1], [[1, 2, 1], [1, 3], [3, 1]]),
	([], [1, 1, 1], [[1, 1, 1], [1, 2], [2, 1], [3]]),
	([1, 1], [1, 1], [[1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [1, 3]]),
	([1, 2], [1, 1], [[1, 2, 1, 1], [1, 2, 2], [1, 3, 1]]),
])
def test_generate_pattern_options(test_input_base, test_input_extension, expected):
	assert generate_pattern_options(test_input_base, test_input_extension) == expected


@pytest.mark.parametrize("test_input, test_extension, expected", [
	([1], 1, [[1, 1], [2]]),
	([1, 1], 1, [[1, 1, 1], [1, 2]]),
	([1], 2, [[1, 2], [3]]),
	([], 3, [[3]]),
	([1], 3, [[1, 3]]),
	([1, 2], 1, [[1, 2, 1], [1, 3]]),
	([1, 3], 1, [[1, 3, 1]]),
])
def test_extend_pattern(test_input, test_extension, expected):
	assert extend_pattern(test_input, test_extension) == expected


@pytest.mark.parametrize("test_input, expected", [
	([1, 3, 1, 1, 1, 3, 1, 1, 3, 3, 1, 3], [[1], [1,1,1], [1,1], [1]])
])
def test_split_jumps(test_input, expected):
	assert split_jumps(test_input) == expected


@pytest.mark.parametrize("test_input, expected", [
	({1: 7, 3: 4}, 28)
])
def test_get_output(test_input, expected):
	assert get_output(test_input) == expected


@pytest.mark.parametrize("test_input, expected", [
	([1, 3, 1, 1, 1, 3, 1, 1, 3, 1, 3], {1: 7, 3: 4})
])
def test_group_jolt_jumps(test_input, expected):
	assert group_jolt_jumps(test_input) == expected


@pytest.mark.parametrize("test_input, expected", [
	([1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19], [1, 3, 1, 1, 1, 3, 1, 1, 3, 1, 3])
])
def test_jolt_jumps(test_input, expected):
	assert jolt_jumps(test_input) == expected


@pytest.mark.parametrize("test_input, expected", [
	([16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4], [1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19])
])
def test_adapter_sort(test_input, expected):
	assert adapter_sort(test_input) == expected


@pytest.mark.parametrize("test_input, expected", [
	([16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4], [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4, 22])
])
def test_add_outlet(test_input, expected):
	assert add_outlet(test_input) == expected


@pytest.mark.parametrize("test_input, expected", [
	("source_01.txt", [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4])
])
def test_list_from_file(test_input, expected):
	assert list_from_file(test_input) == expected


@pytest.mark.parametrize("test_input, expected", [
	("source_01.txt", 35),
	("source_02.txt", 220),
	])
def test_answer_1(test_input, expected):
	assert answer_1(test_input) == expected


@pytest.mark.parametrize("test_input, expected", [
	("source_01.txt", 8),
	("source_02.txt", 19208),
	])
def test_answer_2(test_input, expected):
	assert answer_2(test_input) == expected


