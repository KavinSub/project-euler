# Project Euler Problem 206: Concealed Square
# Author: Kavin Subramanyam

import re

def match_pattern(x):
	number = str(x)
	regex = re.compile(r"^1\d2\d3\d4\d5\d6\d7\d8\d9\d0$")
	result = regex.match(number)
	if result != None:
		return True
	return False

if __name__ == '__main__':
	begin = 1010101010
	while not match_pattern(begin ** 2):
		begin += 10
		if begin % 100000 == 0:
			print(begin ** 2)
	print(begin)