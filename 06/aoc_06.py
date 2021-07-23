import re


def groups_from_file(input_file):
	groups = []
	current_group = []
	f = open("input/{}".format(input_file), "r")
	lines = list(map(lambda x: x.strip(), f.readlines()))
	for line in lines:
		if line.strip() == "":
			groups.append(current_group)
			current_group = []
		else:
			current_group.append(line.strip())
	groups.append(current_group)
	return groups
	

def answers_of_group(group):
	answers = set()
	for person in group:
		for answer in person:
			answers.add(answer)
	return answers


def everyones_answers_of_group(group):
	answers = set(group[0])
	for person in group:
		answers = answers.intersection(set(person))
	return answers


def sum_answers(answers):
	return len(answers)


def answer_1(input_file):
	groups = groups_from_file(input_file)
	count = 0
	for group in groups:
		answers = answers_of_group(group)
		count += sum_answers(answers)
	return count
    

def answer_2(input_file):
	groups = groups_from_file(input_file)
	count = 0
	for group in groups:
		answers = everyones_answers_of_group(group)
		count += sum_answers(answers)
	return count
    

if __name__ == "__main__":
	print("01 result {}".format(answer_1("source.txt")))
	print("02 result {}".format(answer_2("source.txt")))
