import pytest
from aoc_04 import *


@pytest.mark.parametrize("test_input, expected", [
	(0, "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm"),
	(2, "hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm"),
])
def test_blocks_from_file(test_input, expected):
	blocks = blocks_from_file("source_01.txt")
	assert blocks[test_input] == expected


def test_pp_from_block():
	input = "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm"
	pp = pp_from_block(input)
	assert pp["ecl"] == "gry"
	assert pp["cid"] == "147"
	assert pp["hgt"] == "183cm"


@pytest.mark.parametrize("test_input, expected", [
	("source_01.txt", 2),
])
def test_answer_1(test_input, expected):
	assert answer_1(test_input) == expected


@pytest.mark.parametrize("test_input, expected", [
	("ecl:gry pid:060033327 eyr:2020 hcl:#fffffd byr:1920 iyr:2017 cid:147 hgt:183cm", True),
	("ecl:gry pid:160033327 eyr:2020 hcl:#fffffd byr:1919 iyr:2017 cid:147 hgt:183cm", False),
	("ecl:gry pid:260033327 eyr:2020 hcl:#fffffd byr:2003 iyr:2009 cid:147 hgt:183cm", False),
	("ecl:gry pid:360033327 eyr:2020 hcl:#fffffd byr:1921 iyr:2021 cid:147 hgt:183cm", False),
	("ecl:gry pid:460033327 eyr:2019 hcl:#fffffd byr:1922 iyr:2017 cid:147 hgt:183cm", False),
	("ecl:gry pid:560033327 eyr:2031 hcl:#fffffd byr:1923 iyr:2017 cid:147 hgt:183cm", False),
	("ecl:gry pid:660033327 eyr:2020 hcl:#fffffd byr:1924 iyr:2017 cid:147 hgt:149cm", False),
	("ecl:gry pid:760033327 eyr:2020 hcl:#fffffd byr:1925 iyr:2017 cid:147 hgt:194cm", False),
	("ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1926 iyr:2017 cid:147 hgt:58in", False),
	("ecl:gry pid:960033327 eyr:2020 hcl:#fffffd byr:1927 iyr:2017 cid:147 hgt:77in", False),
	("ecl:gry pid:860033327 eyr:2020 hcl:#fffff byr:1928 iyr:2017 cid:147 hgt:183cm", False),
	("ecl:gry pid:860033327 eyr:2020 hcl:#fffff4d byr:1929 iyr:2017 cid:147 hgt:183cm", False),
	("ecl:gry pid:860033327 eyr:2020 hcl:#fffftd byr:1930 iyr:2017 cid:147 hgt:183cm", False),
	("ecl:gry pid:860033327 eyr:2020 hcl:fffffd byr:1931 iyr:2017 cid:147 hgt:183cm", False),
	("ecl:fry pid:860033327 eyr:2020 hcl:#fffffd byr:1932 iyr:2017 cid:147 hgt:183cm", False),
	("ecl:gry pid:60033327 eyr:2020 hcl:#fffffd byr:1933 iyr:2017 cid:147 hgt:183cm", False),
	("ecl:gry pid:0000033327 eyr:2020 hcl:#fffffd byr:1934 iyr:2017 cid:147 hgt:183cm", False),
])
def test_is_valid2(test_input, expected):
	pp = pp_from_block(test_input)
	assert is_valid2(pp) == expected


@pytest.mark.parametrize("test_input, expected", [("source_01.txt", 2)])
def test_answer_2(test_input, expected):
	assert answer_2(test_input) == expected


