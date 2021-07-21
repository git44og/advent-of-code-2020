import pytest
from aoc_03 import *


@pytest.mark.parametrize("test_input, coordinate, expected", [
	([".#.#..#", "#.#.#.."], [0,1], True),
	([".#.#..#", "#.#.#.."], [8,0], True),
	([".#.#..#", "#.#.#.."], [3,1], False)])
def test_hit_tree(test_input, coordinate, expected):
	assert hit_tree(test_input, coordinate) == expected


@pytest.mark.parametrize("test_input, slope, expected", [
	("source_01.txt", [1,1], 2),
	("source_01.txt", [3,1], 7),
	("source_01.txt", [5,1], 3),
	("source_01.txt", [7,1], 4),
	("source_01.txt", [1,2], 2),
])
def test_answer_1(test_input, slope, expected):
	assert answer_1(test_input, slope) == expected


@pytest.mark.parametrize("test_input, expected", [("source_01.txt", 336)])
def test_answer_2(test_input, expected):
	assert answer_2(test_input) == expected


