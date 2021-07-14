

def list_from_file(input_file):
	f = open("input/{}".format(input_file), "r")
	return f.read().split("\n")


def hit_tree(forest_map, coordinate):
	forest_width = len(forest_map[0])
	return forest_map[coordinate[1]][coordinate[0] % forest_width] == "#"


def answer_1(input_file, slope):
	forest_map = list_from_file(input_file)
	coordinate = [0,0]
	tree_counter = 0
	while coordinate[1] < len(forest_map):
		tree_counter += 1 if hit_tree(forest_map, coordinate) else 0
		for i in range(2):
			coordinate[i] += slope[i]
	return tree_counter
    

def answer_2(input_file):
	slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]
	result = 1
	for slope in slopes:
		result *= answer_1(input_file, slope)
	return result
    

if __name__ == "__main__":
	print("01 result {}".format(answer_1("source.txt", [3,1])))
	print("02 result {}".format(answer_2("source.txt")))
