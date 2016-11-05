# Project Euler Problem 76: Counting Summations
# Author: Kavin Subramanyam

def memoize(func):
	v = {}
	def inner(*args):
		if args in v:
			return v[args]
		else:
			result = func(*args)
			v[args] = result
			return result
	return inner

@memoize
def count(n, v):
	if v <= 1: return 1
	c = 0
	while n >= 0:
		c += count(n, v - 1)
		n = n - v
	return c

if __name__ == '__main__':
	print(count(100, 100) - 1)