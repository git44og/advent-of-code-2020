import re


def blocks_from_file(input_file):
	f = open("input/{}".format(input_file), "r")
	lines = f.readlines()
	blocks = []
	block = ""
	for line in lines:
		line = line.strip()
		if line == "" and block != "":
			blocks.append(block.strip())
			block = ""
			continue
		block = "{} {}".format(block, line)
	if block != "":
		blocks.append(block.strip())
	return blocks
	

def pp_from_block(block):
	pp = {}
	for kv in block.split(" "):
		key, value = kv.split(":")
		pp[key.strip()] = value.strip()
	return pp


def is_valid(pp):
	required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
	for key in required:
		if key not in pp.keys():
			return False
	return True

	
def is_valid2(pp):
	#byr
	try:
		if int(pp["byr"]) < 1920 or int(pp["byr"]) > 2002:
# 			print("byr {}".format(pp["byr"]))
			return False
	except:
# 		print("byr {}".format(pp["byr"]))
		return False

	#iyr
	try:
		if int(pp["iyr"]) < 2010 or int(pp["iyr"]) > 2020:
# 			print("iyr {}".format(pp["iyr"]))
			return False
	except:
# 		print("iyr {}".format(pp["iyr"]))
		return False

	#eyr
	try:
		if int(pp["eyr"]) < 2020 or int(pp["eyr"]) > 2030:
# 			print("eyr {}".format(pp["eyr"]))
			return False
	except:
# 		print("eyr {}".format(pp["eyr"]))
		return False
	
	#hgt
	matching = re.match(r"([0-9]+)(in|cm)", pp["hgt"])
	if matching:
		num = int(matching.group(1))
		unit = matching.group(2)
		if unit == "cm" and (num < 150 or num > 193):
# 			print("hgt {}".format(pp["hgt"]))
			return False
		if unit == "in" and (num < 59 or num > 76):
# 			print("hgt {}".format(pp["hgt"]))
			return False
	else:
# 		print("hgt {}".format(pp["hgt"]))
		return False
		
	#hcl
	matching = re.match(r"^#[0-9a-f]{6}$", pp["hcl"])
	if not matching:
# 		print("hcl {}".format(pp["hcl"]))
		return False
	
	#ecl
	if pp["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
# 		print("ecl {}".format(pp["ecl"]))
		return False

	#pid
	matching = re.match(r"^[0-9]{9}$", pp["pid"])
	if not matching:
# 		print("pid {}".format(pp["pid"]))
		return False
	
	return True


def answer_1(input_file):
	blocks = blocks_from_file(input_file)
	counter = 0
	for block in blocks:
		pp = pp_from_block(block)
		if is_valid(pp):
			counter += 1
	return counter
    

def answer_2(input_file):
	blocks = blocks_from_file(input_file)
	counter = 0
	for block in blocks:
		pp = pp_from_block(block)
		if is_valid(pp) and is_valid2(pp):
			counter += 1
	return counter
    

if __name__ == "__main__":
	print("01 result {}".format(answer_1("source.txt")))
	print("02 result {}".format(answer_2("source.txt")))
