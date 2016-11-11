# Project Euler Problem 301: Nim
# Author: Kavin Subramanyam

import time

def memoize(func):
	memo = {}
	def inner(*args):
		if args in memo:
			return memo[args]
		else:
			result = func(*args)
			memo[args] = result
			return result
	return inner

def nim_function(n1, n2, n3):
	return n1 ^ n2 ^ n3 == 0

# Counts all bitstrings of length n. Note: is equal to fibonacci sequence
@memoize
def count_bitstrings(n):
	if n == 1: return 1
	if n == 2: return 1
	return count_bitstrings(i - 1) + count_bitstrings(i - 2)

if __name__ == '__main__':
	
	begin = time.time()
	count = 1 # To account for 2^30
	max_value = 30
	for i in range(1, max_value + 1):
		count += count_bitstrings(i)
	end = time.time()
	print("Time taken:", end - begin)
	print("Solution:", count)