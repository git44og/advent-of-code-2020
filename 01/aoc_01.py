

def list_from_file(input_file):
	f = open("input/{}".format(input_file), "r")
	return list(map(lambda x: int(x), f.read().split("\n")))


def add_all(list):
	r = 0
	for a in list:
		r += a
	return r


def mult_all(list):
	r = 1
	for p in list:
		r *= p
	return r



def find_pair(input_list, tuple_size):
	if tuple_size == 2:
		for i1 in range(len(input_list)):
			for i2 in range(i1+1, len(input_list)):
				tuple = (input_list[i1], input_list[i2])
				if add_all(tuple) == 2020:
					return tuple
	elif tuple_size == 3:
		for i1 in range(len(input_list)):
			for i2 in range(i1+1, len(input_list)):
				for i3 in range(i2+1, len(input_list)):
					tuple = (input_list[i1], input_list[i2], input_list[i3])
					if add_all(tuple) == 2020:
						return tuple
	return (0,0)


def product_of_pair(input_file, tuple_size):
	list = list_from_file(input_file)
	pair = find_pair(list, tuple_size)
	return mult_all(pair)
    

if __name__ == "__main__":
	print("result for {}:{}".format(2, product_of_pair("source.txt", 2)))
	print("result for {}:{}".format(3, product_of_pair("source.txt", 3)))