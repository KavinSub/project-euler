# Project Euler Problem 73: Counting Fractions in a Range
# Author: Kavin Subramanyam

from fractions import Fraction
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

def gcd(a, b):
	while b != 0:
		temp = b
		b = a % b
		a = temp
	return a

def within_range(num, den):
	return 3*num > den and 2*num < den


if __name__ == '__main__':
	begin = time.time()

	max_d = 12000
	count = 0
	for i in range(2, max_d + 1):
		for j in range(i//3 + 1, i//2 + 1):
			if gcd(j, i) == 1:
				if within_range(j, i):
					count += 1
	end = time.time()
	print("Time elapsed:", end - begin)
	print("Solution:", count)