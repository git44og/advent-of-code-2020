import pytest
from aoc_02 import *


@pytest.mark.parametrize("test_input, expected", [("source_01.txt", 2)])
def test_answer(test_input, expected):
	assert answer(test_input) == expected


@pytest.mark.parametrize("test_input, expected", [("source_01.txt", 1)])
def test_new_answer(test_input, expected):
	assert new_answer(test_input) == expected


@pytest.mark.parametrize("test_input, expected", [
	({"min": 4,"max": 13,"letter": "c","password": "ccccvcgwbhwrcqf"},True),
	({"min": 4,"max": 13,"letter": "c","password": "ccvcgwbhwrcqf"},True),
	({"min": 4,"max": 13,"letter": "c","password": "ccvcgwbhwrqf"},False),
	({"min": 4,"max": 5,"letter": "c","password": "ccvcccgwbhwrqf"},True),
	({"min": 4,"max": 5,"letter": "c","password": "ccvccccgwbhwrqf"},False)
])
def test_matches_rule(test_input, expected):
	assert matches_rule(test_input) == expected


@pytest.mark.parametrize("test_input, expected", [
	({"min": 2,"max": 3,"letter": "c","password": "aca"},True),
	({"min": 2,"max": 3,"letter": "c","password": "aac"},True),
	({"min": 2,"max": 3,"letter": "c","password": "acc"},False),
	({"min": 2,"max": 3,"letter": "c","password": "aaa"},False),
])
def test_matches_new_rule(test_input, expected):
	assert matches_new_rule(test_input) == expected


@pytest.mark.parametrize("test_input, expected_min, expected_max, expected_letter, expected_password", [("4-13 c: ccccvcgwbhwrcqf", 4, 13, "c", "ccccvcgwbhwrcqf")])
def test_rule_reader(test_input, expected_min, expected_max, expected_letter, expected_password):
	rule = read_rule(test_input)
	assert rule["min"] == expected_min
	assert rule["max"] == expected_max
	assert rule["letter"] == expected_letter
	assert rule["password"] == expected_password


	



