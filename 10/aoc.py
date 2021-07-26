import re
from itertools import groupby


def list_from_file(input_file):
	f = open("input/{}".format(input_file), "r")
	lines = list(map(lambda x: x.strip(), f.readlines()))
	return list(map(lambda x: int(x.strip()), lines))
	

def add_outlet(jolt_list):
	jolt_list.append(max(jolt_list)+3)
	return jolt_list


def adapter_sort(jolt_list):
	jolt_list.sort()
	return jolt_list


def jolt_jumps(sorted_jolt_list):
	list_1 = [0]+sorted_jolt_list[:-1]
	list_2 = sorted_jolt_list
	jolt_jump_list = list(map(lambda x1, x2: x2-x1, list_1, list_2))
	return jolt_jump_list


def group_jolt_jumps(jolt_jumps_list):
	return {
		1: len(list(filter(lambda x: x==1, jolt_jumps_list))),
		3: len(list(filter(lambda x: x==3, jolt_jumps_list)))
	}


def get_output(group_jolt_jumps):
	return group_jolt_jumps[1]*group_jolt_jumps[3]


def answer_1(input_file):
	jolt_list = list_from_file(input_file)
	full_jolt_list = add_outlet(jolt_list)
	sorted_list = adapter_sort(full_jolt_list)
	jumps = jolt_jumps(sorted_list)
	grouped_jumps = group_jolt_jumps(jumps)
	result = get_output(grouped_jumps)
	return result
    

def split_jumps(jump_list):
	return [list(group) for k, group in groupby(jump_list, lambda x: x == 3) if not k]


def generate_pattern_options(base_pattern, extension_pattern):
	if len(extension_pattern) == 0:
		return [base_pattern]
	sub_patterns = extend_pattern(base_pattern, extension_pattern[0])
	result_patterns = []
	for sub_pattern in sub_patterns:
		result_patterns += generate_pattern_options(sub_pattern, extension_pattern[1:])
	return result_patterns


def extend_pattern(source_pattern, extension):
	if len(source_pattern) == 0:
		return [[extension]]
	result_patterns = [source_pattern.copy()+[extension]]
	if source_pattern[-1] + extension <= 3:
		new_pattern = source_pattern.copy()
		new_pattern[-1] = source_pattern[-1] + extension
		result_patterns.append(new_pattern)
	return result_patterns


def answer_2(input_file):
	jolt_list = list_from_file(input_file)
	full_jolt_list = add_outlet(jolt_list)
	sorted_list = adapter_sort(full_jolt_list)
	jumps = jolt_jumps(sorted_list)

	splitted = split_jumps(jumps)
	adapter_options = 1

	for sub_section in splitted:
		options = generate_pattern_options([], sub_section)
		adapter_options *= len(options)

	return adapter_options
    

if __name__ == "__main__":
	print("01 result {}".format(answer_1("source.txt")))
	print("02 result {}".format(answer_2("source.txt")))
