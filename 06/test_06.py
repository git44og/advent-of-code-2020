import pytest
from aoc_06 import *


@pytest.mark.parametrize("test_input, expected", [
	({"a", "b", "c"}, 3),
	({"a"}, 1),
	({"b", "c"}, 2),
])
def test_sum_answers(test_input, expected):
	assert sum_answers(test_input) == expected


@pytest.mark.parametrize("test_input, expected", [
	(["abc"], {"a", "b", "c"}),
	(["a", "b", "c"], {"a", "b", "c"}),
	(["ab", "ac"], {"a", "b", "c"}),
	(["a", "a", "a", "a"], {"a"}),
	(["b"], {"b"}),
])
def test_answers_of_group(test_input, expected):
	assert answers_of_group(test_input) == expected


@pytest.mark.parametrize("test_input, expected", [
	(["abc"], {"a", "b", "c"}),
	(["a", "b", "c"], set()),
	(["ab", "ac"], {"a"}),
	(["a", "a", "a", "a"], {"a"}),
	(["b"], {"b"}),
])
def test_everyones_answers_of_group(test_input, expected):
	assert everyones_answers_of_group(test_input) == expected


@pytest.mark.parametrize("test_input, expected", [
	("source_01.txt", [["abc"], ["a", "b", "c"], ["ab", "ac"], ["a", "a", "a", "a"], ["b"]]),
])
def test_groups_from_file(test_input, expected):
	groups = groups_from_file(test_input)
	assert groups == expected


@pytest.mark.parametrize("test_input, expected", [("source_01.txt", 11)])
def test_answer_1(test_input, expected):
	assert answer_1(test_input) == expected


@pytest.mark.parametrize("test_input, expected", [("source_01.txt", 6)])
def test_answer_2(test_input, expected):
	assert answer_2(test_input) == expected


