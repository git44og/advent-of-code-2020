import re


def list_from_file(input_file):
	f = open("input/{}".format(input_file), "r")
	return f.read().split("\n")


def read_rule(input_line):
	# 6-7 g: fgggghgng
	seg = re.match(r"(\d+)-(\d+) (\w): (\w+)", input_line)
	rule = {
		"min": int(seg.group(1)),
		"max": int(seg.group(2)),
		"letter": seg.group(3),
		"password": seg.group(4),
	}
	return rule


def check_line(line, check_method):
	rule = read_rule(line)
	return 1 if check_method(rule) else 0
	

def matches_rule(rule):
	password = rule["password"]
	num_letter = len(password) - len(password.replace(rule["letter"], ""))
	return num_letter >= rule["min"] and num_letter <= rule["max"]
	
	
def matches_new_rule(rule):
	password = rule["password"]
	l1 = password[rule["min"]-1]
	l2 = password[rule["max"]-1]
	return (l1 == rule["letter"] or l2 == rule["letter"]) and l1 != l2
	
	
def answer(input_file):
	line_list = list_from_file(input_file)
	checked = map(lambda x: check_line(x, matches_rule), line_list)
	return sum(checked)
    

def new_answer(input_file):
	line_list = list_from_file(input_file)
	checked = map(lambda x: check_line(x, matches_new_rule), line_list)
	return sum(checked)
    

if __name__ == "__main__":
	print("01 result {}".format(answer("source.txt")))
	print("02 result {}".format(new_answer("source.txt")))
