import re
from itertools import groupby


def seats_from_file(input_file):
	f = open("input/{}".format(input_file), "r")
	return list(map(lambda x: list(x.strip()), f.readlines()))
	

def adjacent_seats(seats, coord):
	limit_cols = seats[max(0,coord[1]-1):coord[1]+2]
	return list(map(lambda x: x[max(0,coord[0]-1):coord[0]+2], limit_cols))


def seat_is_taken(seats, coord):
	return seats[coord[1]][coord[0]] == "#"


def seat_is_empty(seats, coord):
	return seats[coord[1]][coord[0]] == "L"


def seat_will_get_up(adjacent_seats):
	return len(list(filter(lambda x: x=="#", adjacent_seats))) >= 4


def seat_will_sit_down(adjacent_seats):
	return len(list(filter(lambda x: x=="#", adjacent_seats))) == 0


def answer_1(input_file):
	return 0
    

def answer_2(input_file):
	return 0    

if __name__ == "__main__":
	print("01 result {}".format(answer_1("source.txt")))
	print("02 result {}".format(answer_2("source.txt")))
