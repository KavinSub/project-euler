# Project Euler Problem 61: Cyclical Figurate Numbers
# Author: Kavin Subramanyam

from collections import deque
import time

def triangle(n):
	return (n*(n+1))//2

def square(n):
	return n**2

def pentagon(n):
	return (n*(3*n - 1))//2

def hexagon(n):
	return n*(2*n - 1)

def heptagon(n):
	return n*(5*n-3)//2

def octagon(n):
	return n*(3*n - 2)

def print_nested_list(lists):
	for l in lists:
		print(l)

# 0 = Square, 1 = Pentagon, 2 = Hexagon, 3 = Heptagon, 4 = Octagon
numbers = [{}, {}, {}, {}, {}]

# encountered is bitstring
def determine_next(num, encountered, original):
	if encountered == 31: 
		if num % 100 == original//100: return [original]
		else: return []
	key = num % 100
	chain = []
	longest_chain = 0
	for i, table in enumerate(numbers):
		values = []
		if (2**i) & encountered == 0:
			if key in table: values = table[key]
		for v in values:
			next_chain = determine_next(v, encountered | 2**i, original)
			if len(next_chain) >= longest_chain:
				longest_chain = len(next_chain)
				chain = [v]
				chain.extend(next_chain)
	return chain

if __name__ == '__main__':

	begin = time.time()

	numfunctions = [square, pentagon, hexagon, heptagon, octagon]

	# Generate all numbers
	for index, function in enumerate(numfunctions):
		i = 1
		num = function(i)
		table = numbers[index]
		while num < 10000:
			if num >= 1000:
				key = num//100
				if key not in table: table[key] = [num]
				else: table[key].append(num)
			i += 1
			num = function(i)

	# Now find the cycle
	i = 1
	num = triangle(i)
	solution = []
	while num < 10000:
		if num >= 1000:
			chain = determine_next(num, 0, num)
			if len(chain) == 6:
				solution = chain
				break
		i += 1
		num = triangle(i)

	end = time.time()
	print("Time taken:", end - begin)
	print("Solution:", solution, sum(solution))