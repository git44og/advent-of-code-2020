import re


def rules_from_file(input_file):
	f = open("input/{}".format(input_file), "r")
	lines = list(map(lambda x: x.strip(), f.readlines()))
	rules = {}
	for line in lines:
		rule_key, rule = rule_from_line(line)
		rules[rule_key] = rule
	return rules
	

def rule_from_line(rule_line):
	rule_key_text, rules_text = rule_line.strip()[:-1].split(" contain ")
	rule_key = rule_key_text[:-5]
	if rules_text == "no other bags":
		return rule_key, {}
	rules = {}
	for rule_text in rules_text.split(", "):
		matching = re.match(r"([0-9]+) (.+) bag", rule_text)
		num = int(matching.group(1))
		color = matching.group(2)
		rules[color] = num
	return rule_key, rules


def bag_contains_bag(rule, bag, target_bag):
	if target_bag in rule[bag].keys():
		return True
	for sub_bag in rule[bag].keys():
		if bag_contains_bag(rule, sub_bag, target_bag):
			return True
	return False


def num_bags_inside(rule, bag):
	count = 0
	for inner_bag in rule[bag].keys():
		count += rule[bag][inner_bag] * (1 + num_bags_inside(rule, inner_bag))
	return count


def answer_1(input_file):
	rules = rules_from_file(input_file)
	colors = rules.keys()
	target_color = "shiny gold"
	count = 0
	for color in colors:
		count += 1 if bag_contains_bag(rules, color, target_color) else 0
	return count
    

def answer_2(input_file):
	rules = rules_from_file(input_file)
	return num_bags_inside(rules, "shiny gold")
    

if __name__ == "__main__":
	print("01 result {}".format(answer_1("source.txt")))
	print("02 result {}".format(answer_2("source.txt")))
