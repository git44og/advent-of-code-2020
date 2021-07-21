import pytest
from aoc_05 import *


def test_list_from_file():
	list = list_from_file("source_01.txt")
	assert list == ["BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]


@pytest.mark.parametrize("test_input, expected", [
	("FBFBBFF", 44),
	("BFFFBBF", 70),
	("FFFBBBF", 14),
	("BBFFBBF", 102),
])
def test_row_from_key(test_input, expected):
	row = row_from_key(test_input)
	assert row == expected


@pytest.mark.parametrize("test_input, expected", [
	("RLR", 5),
	("RRR", 7),
	("RLL", 4),
])
def test_col_from_key(test_input, expected):
	col = col_from_key(test_input)
	assert col == expected


@pytest.mark.parametrize("test_input, expected_row, expected_col", [
	("FBFBBFFRLR", "FBFBBFF", "RLR"),
])
def test_split_key(test_input, expected_row, expected_col):
	row, col = split_key(test_input)
	assert row == expected_row
	assert col == expected_col


@pytest.mark.parametrize("test_input, expected", [
	("FBFBBFFRLR", (44, 5)),
	("BFFFBBFRRR", (70, 7)),
	("FFFBBBFRLL", (14, 4)),
])
def test_get_seat_number(test_input, expected):
	assert get_seat_number(test_input) == expected


@pytest.mark.parametrize("test_input, expected", [
	("BFFFBBFRRR", 567),
	("FFFBBBFRRR", 119),
	("BBFFBBFRLL", 820),
	("FBFBBFFRLR", 357),
])
def test_get_seat_id(test_input, expected):
	assert get_seat_id(test_input) == expected


@pytest.mark.parametrize("test_input, test_input_list, expected", [
	(["FBFBBFFRLR", "BFFFBBFRRR", "FFFBBBFRLL"], [357, 567, 116, 179], [179]),
])
def test_get_untaken_seats(test_input, test_input_list, expected):
	full_list = test_input_list
	assert get_untaken_seats(test_input, test_input_list) == expected


@pytest.mark.parametrize("test_input, expected", [("source_01.txt", 820)])
def test_answer_1(test_input, expected):
	assert answer_1(test_input) == expected


# @pytest.mark.parametrize("test_input, expected", [("source_01.txt", 0)])
# def test_answer_2(test_input, expected):
# 	assert answer_2(test_input) == expected


