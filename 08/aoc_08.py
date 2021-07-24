import re


def code_from_file(input_file):
	f = open("input/{}".format(input_file), "r")
	lines = list(map(lambda x: x.strip(), f.readlines()))
	code = []
	for line in lines:
		op, index = line_to_code(line.strip())
		code.append({"op": op, "index": index})
	return code
	

def line_to_code(line):
	op, index_str = line.split(" ")
	return op, int(index_str)


def execute_line(code_line, index, accumulator):
	if code_line["op"] == "acc":
		return index+1, accumulator+code_line["index"]
	if code_line["op"] == "jmp":
		return index+code_line["index"], accumulator
	return index+1, accumulator


def execute_code(code):
	used_instructions = []
	index = 0
	accumulator = 0
	while index < len(code) and index not in used_instructions:
		used_instructions.append(index)
		index, accumulator = execute_line(code[index], index, accumulator)
	return index, accumulator


def is_terminating(code):
	index, acc = execute_code(code)
	return index == len(code)


def variation(code, index):
	if code[index]["op"] == "acc":
		return None
	replace = {"jmp": "nop", "nop": "jmp"}
	new_code = code[:]
	new_code[index] = {"op": replace[new_code[index]["op"]], "index": new_code[index]["index"]}
	return new_code


def code_variations(code):
	variations = []
	for i in range(len(code)):
	# for i in range(1):
		code_variation = variation(code, i)
		if code_variation != None:
			variations.append(code_variation)
	return variations


def answer_1(input_file):
	code = code_from_file(input_file)
	index, acc = execute_code(code)
	return acc
    

def answer_2(input_file):
	code = code_from_file(input_file)
	codes = code_variations(code)
	for my_code in codes:
		if is_terminating(my_code):
			index, acc = execute_code(my_code)
			return acc
	return 0
    

if __name__ == "__main__":
	print("01 result {}".format(answer_1("source.txt")))
	print("02 result {}".format(answer_2("source.txt")))
