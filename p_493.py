# Project Euler Problem 493: Under The Rainbow
# Author: Kavin Subramanyam

from functools import reduce
import operator
from decimal import *

getcontext().prec = 50

def memoize(func):
	values = {}
	def inner(*args):
		if args in values:
			return values[args]
		else:
			result = func(*args)
			values[args] = result
			return result
	return inner

@memoize
def factorial(n):
	if n <= 1: return 1
	else: return n * factorial(n - 1)

def multinomial(n, c):
	f = [factorial(x) for x in c]
	return factorial(n)//reduce(operator.mul, f, 1)

# total, colors
def generate_combinations(total, colors):
	if colors <= 0: return [[]]
	elif colors == 1: return [[total]]
	elif total == 0: return [[0] * colors]
	combinations = []
	for i in range(1, min(11, total + 2 - colors)):
		x = generate_combinations(total - i, colors - 1)
		for c in x:
			temp = [i]
			temp.extend(c)
			combinations.append(temp)
	filter_combinations(combinations)
	return combinations

def filter_combinations(combinations):
	indices = []
	for i in range(len(combinations)):
		for v in combinations[i]:
			if v > 10:
				indices.append(i)
	for index in indices[::-1]:
		combinations.pop(index)

def compute(combinations):
	return sum([probability(combination) for combination in combinations])

def probability(combination):
	m = multinomial(20, combination)
	num = reduce(operator.mul, [factorial(10)//factorial(10 - c) for c in combination], 1)
	den = factorial(70)//factorial(50)
	return Decimal(m)*Decimal(num)/Decimal(den)

if __name__ =='__main__':
	expected_value = 0
	total = 0
	for i in range(2, 8):
		combinations = generate_combinations(20, i)
		p = multinomial(7, [i, 7 - i]) * compute(combinations)
		total += p
		expected_value += i * p
	print(expected_value)