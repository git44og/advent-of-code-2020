import pytest
from aoc_07 import *


@pytest.mark.parametrize("test_input, test_input_target, expected", [
	("light red", "bright white", True),
	("light red", "muted yellow", True),
	("light red", "shiny gold", True),
	("light red", "faded blue", True),
	("faded blue", "bright white", False),
	("bright white", "faded blue", False),
	("bright white", "shiny gold", True),
])
def test_bag_contains_bag(test_input, test_input_target, expected):
	rule = {
		"light red": {"bright white": 1, "muted yellow": 2},
		"bright white": {"shiny gold": 1},
		"muted yellow": {"shiny gold": 2, "faded blue": 9},
		"faded blue": {},
		"shiny gold": {},
	}
	assert bag_contains_bag(rule, test_input, test_input_target) == expected


@pytest.mark.parametrize("test_input, expected", [
	("light red", 26),
	("faded blue", 0),
	("shiny gold", 0),
	("muted yellow", 11),
	("bright white", 1),
])
def test_num_bags_inside(test_input, expected):
	rule = {
		"light red": {"bright white": 1, "muted yellow": 2},
		"bright white": {"shiny gold": 1},
		"muted yellow": {"shiny gold": 2, "faded blue": 9},
		"faded blue": {},
		"shiny gold": {},
	}
	assert num_bags_inside(rule, test_input) == expected


@pytest.mark.parametrize("test_input, expected", [
	("light red", 152), # 2+(2*75)
	("faded blue", 5),
	("shiny gold", 0),
	("muted yellow", 24), # 4+(4*5)
	("bright white", 75), # 3+(3*24)
])
def test_num_bags_inside_2(test_input, expected):
	rule = {
		"light red": {"bright white": 2},
		"bright white": {"muted yellow": 3},
		"muted yellow": {"faded blue": 4},
		"faded blue": {"shiny gold": 5},
		"shiny gold": {},
	}
	assert num_bags_inside(rule, test_input) == expected


@pytest.mark.parametrize("test_input, expected", [
	("light red", True),
	("dark orange", True),
	("bright white", True),
	("muted yellow", True),
	("shiny gold", False),
	("dark olive", False),
	("vibrant plum", False),
	("faded blue", False),
	("dotted black", False),
])
def test_bag_contains_bag_2(test_input, expected):
	rules = rules_from_file("source_01.txt")
	assert bag_contains_bag(rules, test_input, "shiny gold") == expected


@pytest.mark.parametrize("test_input, expected", [("source_01.txt", {
	"light red": {"bright white": 1, "muted yellow": 2},
	"dark orange": {"bright white": 3, "muted yellow": 4},
	"bright white": {"shiny gold": 1},
	"muted yellow": {"shiny gold": 2, "faded blue": 9},
	"shiny gold": {"dark olive": 1, "vibrant plum": 2},
	"dark olive": {"faded blue": 3, "dotted black": 4},
	"vibrant plum": {"faded blue": 5, "dotted black": 6},
	"faded blue": {},
	"dotted black": {},
})])
def test_rules_from_file(test_input, expected):
	assert rules_from_file(test_input) == expected


@pytest.mark.parametrize("test_input, expected_key, expected_rule", [
	("light red bags contain 1 bright white bag, 2 muted yellow bags.", "light red", {"bright white": 1, "muted yellow": 2}),
	("bright white bags contain 1 shiny gold bag.", "bright white", {"shiny gold": 1}),
	("faded blue bags contain no other bags.", "faded blue", {}),
])
def test_rule_from_line(test_input, expected_key, expected_rule):
	rule_key, rule = rule_from_line(test_input)
	assert rule_key == expected_key
	assert rule == expected_rule


@pytest.mark.parametrize("test_input, expected", [("source_01.txt", 4)])
def test_answer_1(test_input, expected):
	assert answer_1(test_input) == expected


@pytest.mark.parametrize("test_input, expected", [("source_01.txt", 32)])
def test_answer_2(test_input, expected):
	assert answer_2(test_input) == expected


