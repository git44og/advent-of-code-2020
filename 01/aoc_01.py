from functools import reduce


def list_from_file(input_file):
	f = open("input/{}".format(input_file), "r")
	return list(map(lambda x: int(x), f.read().split("\n")))


def mult_all(list1):
	return reduce((lambda x, y: x * y), list1)


def sub_sum(max_tuple, input_list, index_list=[], current_sum=0):
	if len(index_list) == max_tuple:
		return (current_sum, index_list)
	for i in range(len(input_list)):
		if i in index_list:
			continue
		sub_result = sub_sum(max_tuple, input_list, index_list+[i], current_sum+input_list[i])
		if sub_result == None:
			continue
		if sub_result[0] != 2020:
			continue
		return sub_result
		


def find_tuple(input_list, tuple_size):
	result = sub_sum(tuple_size, input_list)
	return list(map(lambda x: input_list[x], result[1]))
		

def product_of_tuple(input_file, tuple_size):
	list = list_from_file(input_file)
	pair = find_tuple(list, tuple_size)
	
	return mult_all(pair)
    

if __name__ == "__main__":
	print("result for {}:{}".format(2, product_of_tuple("source.txt", 2)))
	print("result for {}:{}".format(3, product_of_tuple("source.txt", 3)))