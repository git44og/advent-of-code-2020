import pytest
from aoc_01 import *


@pytest.mark.parametrize("test_input, tuple_size, expected", [("source_01.txt", 2, 514579), ("source_01.txt", 3, 241861950)])
def test_answer(test_input, tuple_size, expected):
	assert product_of_tuple(test_input, tuple_size) == expected


@pytest.mark.parametrize("test_input, tuple_size, expected", [("source_01.txt", 2, (1721, 299)), ("source_01.txt", 3, (979, 366, 675))])
def test_answer(test_input, tuple_size, expected):
	number_list = list_from_file(test_input)
	pair = find_tuple(number_list, tuple_size)
	for number in expected:
		assert number in pair
		assert number in pair


def test_list_from_file():
	expected = [1721,979,366,299,675,1456]
	read_list = list_from_file("source_01.txt")
	assert expected == read_list

