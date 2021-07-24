import pytest
from aoc_08 import *


@pytest.mark.parametrize("test_input, expected", [
	([{"op": "nop", "index": 0}], True),
	([{"op": "jmp", "index": 0}], False),
	([
		{"op": "nop", "index": 0},
		{"op": "acc", "index": 1},
		{"op": "jmp", "index": 4},
		{"op": "acc", "index": 3},
		{"op": "jmp", "index": -3},
		{"op": "acc", "index": -99},
		{"op": "acc", "index": 1},
		{"op": "jmp", "index": -4},
		{"op": "acc", "index": 6},
	], False)
])
def test_is_terminating(test_input, expected):
	assert  is_terminating(test_input) == expected


@pytest.mark.parametrize("test_input, test_index, expected", [
	([
		{"op": "nop", "index": 0},
		{"op": "acc", "index": 1},
		{"op": "jmp", "index": 4},
	], 0, [
		{"op": "jmp", "index": 0},
		{"op": "acc", "index": 1},
		{"op": "jmp", "index": 4},
	]),
	([
		{"op": "nop", "index": 0},
		{"op": "acc", "index": 1},
		{"op": "jmp", "index": 4},
	], 1, None),
	([
		{"op": "nop", "index": 0},
		{"op": "acc", "index": 1},
		{"op": "jmp", "index": 4},
	], 2, [
		{"op": "nop", "index": 0},
		{"op": "acc", "index": 1},
		{"op": "nop", "index": 4},
	]),
])
def test_variation(test_input, test_index, expected):
	assert variation(test_input, test_index) == expected


@pytest.mark.parametrize("test_input, expected", [
	# ([{"op": "nop", "index": 0}], [[{"op": "jmp", "index": 0}]]),
	# ([{"op": "jmp", "index": 0}], [[{"op": "nop", "index": 0}]]),
	# ([{"op": "acc", "index": 0}], []),
	([
		{"op": "nop", "index": 0},
		{"op": "acc", "index": 1},
		{"op": "jmp", "index": 4},
	], [
		[
			{"op": "jmp", "index": 0},
			{"op": "acc", "index": 1},
			{"op": "jmp", "index": 4},
		],[
			{"op": "nop", "index": 0},
			{"op": "acc", "index": 1},
			{"op": "nop", "index": 4},
		]
	])
])
def test_code_variations(test_input, expected):
	assert code_variations(test_input) == expected


@pytest.mark.parametrize("test_input, expected_index, expected_acc", [
	({"op": "nop", "index": 3}, 1, 0),
	({"op": "acc", "index": -2}, 1, -2),
	({"op": "jmp", "index": 4}, 4, 0),
])
def test_execute_line(test_input, expected_index, expected_acc):
	index, accumulator = execute_line(test_input, 0, 0)
	assert index == expected_index
	assert accumulator == expected_acc


@pytest.mark.parametrize("test_input, expected", [("source_01.txt", [
	{"op": "nop", "index": 0},
	{"op": "acc", "index": 1},
	{"op": "jmp", "index": 4},
	{"op": "acc", "index": 3},
	{"op": "jmp", "index": -3},
	{"op": "acc", "index": -99},
	{"op": "acc", "index": 1},
	{"op": "jmp", "index": -4},
	{"op": "acc", "index": 6},
])])
def test_code_from_file(test_input, expected):
	assert code_from_file(test_input) == expected


@pytest.mark.parametrize("test_input, expected_op, expected_index", [
	("nop +0", "nop", 0),
	("acc +1", "acc", 1),
	("jmp +4", "jmp", 4),
])
def test_line_to_code(test_input, expected_op, expected_index):
	op, index = line_to_code(test_input)
	assert op == expected_op
	assert index == expected_index


@pytest.mark.parametrize("test_input, expected", [("source_01.txt", 5)])
def test_answer_1(test_input, expected):
	assert answer_1(test_input) == expected


@pytest.mark.parametrize("test_input, expected", [("source_01.txt", 8)])
def test_answer_2(test_input, expected):
	assert answer_2(test_input) == expected


