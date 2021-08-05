import pytest
from aoc import *


@pytest.mark.parametrize("test_input, expected", [
	(['.', 'L', 'L', 'L'], True),
	(['L', '.', 'L', 'L', 'L', 'L', '.', 'L'], True),
	(['L', '.', 'L', 'L', '.'], True),
	(['#', '#', '#', 'L', 'L'], False),
	(['#', '#', '#', '#', 'L'], False),
	(['#', '#', '#', '#', '#'], False),
])
def test_will_sit_down(test_input, expected):
	assert seat_will_sit_down(test_input) == expected


@pytest.mark.parametrize("test_input, expected", [
	(['.', 'L', 'L', 'L'], False),
	(['L', '.', 'L', 'L', 'L', 'L', '.', 'L'], False),
	(['L', '.', 'L', 'L', '.'], False),
	(['#', '#', '#', 'L', 'L'], False),
	(['#', '#', '#', '#', 'L'], True),
	(['#', '#', '#', '#', '#'], True),
])
def test_will_get_up(test_input, expected):
	assert seat_will_get_up(test_input) == expected


@pytest.mark.parametrize("test_input, expected", [
	([0,0], False),
	([1,1], True),
	([0,1], False),
])
def test_seat_is_taken(test_input, expected):
	seats = [
		['L', '.', 'L'],
		['.', '#', 'L'],
		['L', '.', 'L'],
	]
	assert seat_is_taken(seats, test_input) == expected


@pytest.mark.parametrize("test_input, expected", [
	([0,0], True),
	([1,1], False),
	([0,1], False),
])
def test_seat_is_empty(test_input, expected):
	seats = [
		['L', '.', 'L'],
		['.', '#', 'L'],
		['L', '.', 'L'],
	]
	assert seat_is_empty(seats, test_input) == expected


@pytest.mark.parametrize("test_input, expected", [
	([0,0], ['.', 'L', 'L', 'L']),
	([1,1], ['L', '.', 'L', 'L', 'L', 'L', '.', 'L']),
	([0,1], ['L', '.', 'L', 'L', '.']),
	([2,0], ['L', 'L', 'L', 'L', 'L']),
])
def test_adjacent_seats(test_input, expected):
	seats = [
		['L', '.', 'L'],
		['L', 'L', 'L'],
		['L', '.', 'L'],
	]
	a_seats = adjacent_seats(seats, test_input)
	assert a_seats.sort() == expected.sort()


@pytest.mark.parametrize("test_input, expected", [
	("source_01.txt", [
		['L', '.', 'L', 'L', '.', 'L', 'L', '.', 'L', 'L',],
		['L', 'L', 'L', 'L', 'L', 'L', 'L', '.', 'L', 'L',],
		['L', '.', 'L', '.', 'L', '.', '.', 'L', '.', '.',],
		['L', 'L', 'L', 'L', '.', 'L', 'L', '.', 'L', 'L',],
		['L', '.', 'L', 'L', '.', 'L', 'L', '.', 'L', 'L',],
		['L', '.', 'L', 'L', 'L', 'L', 'L', '.', 'L', 'L',],
		['.', '.', 'L', '.', 'L', '.', '.', '.', '.', '.',],
		['L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L',],
		['L', '.', 'L', 'L', 'L', 'L', 'L', 'L', '.', 'L',],
		['L', '.', 'L', 'L', 'L', 'L', 'L', '.', 'L', 'L',],
	])
])
def test_list_from_file(test_input, expected):
	assert seats_from_file(test_input) == expected


@pytest.mark.parametrize("test_input, expected", [
	("source_01.txt", 35),
	])
def test_answer_1(test_input, expected):
	assert answer_1(test_input) == expected


@pytest.mark.parametrize("test_input, expected", [
	("source_01.txt", 0),
	])
def test_answer_2(test_input, expected):
	assert answer_2(test_input) == expected


