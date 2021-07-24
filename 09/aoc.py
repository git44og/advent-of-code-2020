import re


def list_from_file(input_file):
	f = open("input/{}".format(input_file), "r")
	lines = list(map(lambda x: x.strip(), f.readlines()))
	return list(map(lambda x: int(x.strip()), lines))
	

def is_valid(input_list, input_prefix, input_index):
	if input_prefix > input_index:
		return True
	number = input_list[input_index]
	prefix = input_list[input_index-input_prefix:input_index]
	for i in range(input_prefix):
		for j in range(input_prefix):
			if i != j and prefix[i]+prefix[j] == number:
				return True
	return False


def sub_sum(test_input, input_offset, target_num):
	current_sum = 0
	i = 0
	while current_sum < target_num and input_offset+i < len(test_input):
		current_sum += test_input[input_offset+i]
		i += 1
	sub_range = test_input[input_offset:input_offset+i]
	return sum(sub_range) == target_num, min(sub_range), max(sub_range)


def answer_1(input_file, prefix):
	num_list = list_from_file(input_file)
	for i in range(len(num_list)):
		if not is_valid(num_list, prefix, i):
			return num_list[i]
	return 0
    

def answer_2(input_file, prefix):
	invalid_number = answer_1(input_file, prefix)
	num_list = list_from_file(input_file)
	for i in range(len(num_list)):
		matches, num_first, num_last = sub_sum(num_list, i, invalid_number)
		if matches:
			return num_first+num_last
	return 0
    

if __name__ == "__main__":
	print("01 result {}".format(answer_1("source.txt", prefix=25)))
	print("02 result {}".format(answer_2("source.txt", prefix=25)))
