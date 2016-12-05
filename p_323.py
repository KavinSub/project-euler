# Project Euler Problem 323: Bitwise-OR operations on random integers
# Author: Kavin Subramanyam

from itertools import permutations
from collections import Counter
from operator import mul
from functools import reduce

def factorial(n):
	return reduce(mul, range(1, n + 1), 1)

def index(p, k):
	c = 0
	i = 1
	for v in p:
		c = c | v
		if c == 2**k - 1: return i
		i += 1
	return i

def expected_value(count, k):
	v = 0
	total = factorial(2**k)
	for key in count.keys():
		v += key*(count[key]/total)
	return v

if __name__ == '__main__':
	k = 2
	count = Counter()
	perms = permutations(range(2**k))
	for i, p in enumerate(perms):
		result = index(p, k)
		count[result] += 1
	print(expected_value(count, k))