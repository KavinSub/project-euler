from math import *
from itertools import *

def prop_div(n):
	L = [1]
	for i in range(2, floor(sqrt(n)) + 1):
		if n % i == 0 and i ** 2 != n:
			L.append(i)
			L.append(n // i)
		elif i ** 2 == n:
			L.append(i)
	return L

def abundant(n):
	return sum(prop_div(n)) > n

if __name__ == '__main__':
	# Generate all abundant numbers
	abundant_numbers = set([i for i in range(1, 28124) if abundant(i)])

	# Get all numbers that can be written as a pair of abundant numbers
	pairs = product(abundant_numbers, abundant_numbers)
	abundant_pairs = set([sum(pair) for pair in pairs if sum(pair) <= 28123])
	nums = set(range(1, 28124))

	print(sum(nums - abundant_pairs))