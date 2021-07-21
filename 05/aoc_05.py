import re


def list_from_file(input_file):
	f = open("input/{}".format(input_file), "r")
	lines = list(map(lambda x: x.strip(), f.readlines()))
	return lines
	

def row_from_key(row_key):
	return index_from_key(row_key, 0, 127, "F", "B")


def col_from_key(col_key):
	return index_from_key(col_key, 0, 7, "L", "R")


def index_from_key(gen_key, l_bound, u_bound, l_key, u_key):
	for partition_key in gen_key:
		if partition_key == l_key:
			u_bound -= int((u_bound - l_bound + 1) / 2)
		elif partition_key == u_key:
			l_bound += int((u_bound - l_bound + 1) / 2)
	return u_bound


def split_key(key):
	return key[:7], key[-3:]
	

def get_seat_number(key):
	row_key, col_key = split_key(key)
	return (row_from_key(row_key), col_from_key(col_key))


def get_seat_id(key):
	seat_number = get_seat_number(key)
	return seat_id_from_number(seat_number)


def seat_id_from_number(seat_number):
	return seat_number[0] * 8 + seat_number[1]


def gen_all_seats():
	all_seats = []
	for row in range(1, 127):
		for col in range(0, 8):
			all_seats.append(seat_id_from_number((row, col)))
	return all_seats			


def get_untaken_seats(keys, all_seats):
	for key in keys:
		seat_id = get_seat_id(key)
		if seat_id in all_seats:
			del all_seats[all_seats.index(seat_id)]
	return all_seats


def answer_1(input_file):
	key_list = list_from_file(input_file)
	seat_ids = []
	for key in key_list:
		seat_id = get_seat_id(key)
		seat_ids.append(seat_id)
	return max(seat_ids)
    

def answer_2(input_file):
	key_list = list_from_file(input_file)
	all_seats = gen_all_seats()
	untaken_seats = get_untaken_seats(key_list, all_seats)
	filtered_seats = list(filter(lambda x: not (x-1 in untaken_seats or x+1 in untaken_seats), untaken_seats))
	return filtered_seats
    

if __name__ == "__main__":
	print("01 result {}".format(answer_1("source.txt")))
	print("02 result {}".format(answer_2("source.txt")))
