# Project Euler Problem 504: Square on the Inside
# Author: Kavin Subramanyam

from itertools import product
from collections import defaultdict
from math import sqrt
import time

def memoize(func):
	memo = {}
	def inner(*args):
		if args in memo: return memo[args]
		else:
			result = func(*args)
			memo[args] = result
			return result
	return inner

def get_area(vertices):
	return ((vertices[0] + vertices[2])*(vertices[1] + vertices[3]))/2

def boundary_points(v):
	count = 0
	for i in range(4):
		count += gcd(v[i], v[(i + 1) % 4])
	return count

@memoize
def gcd(a, b):
	if b == 0: return a
	return gcd(b, a % b)

def lattice_points(vertices):
	area = get_area(vertices)
	boundary_count = boundary_points(vertices)
	return int(area + 1 - boundary_count/2)

def is_square(p):
	s = int(sqrt(p))
	return s**2 == p

if __name__ == '__main__':
	begin = time.time()

	m = 100
	vertices = product(list(range(1, m + 1)), repeat=4)
	square_count = 0
	i = 0
	for v in vertices:
		if i % 100000 == 0: print(i)
		i += 1
		count = lattice_points(v)
		if is_square(count): square_count += 1

	end = time.time()
	print("Time taken:", end - begin)
	print("Solution:", square_count)
