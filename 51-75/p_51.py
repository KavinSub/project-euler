from math import sqrt
import itertools
import ctypes

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
def is_prime(n):
	for i in range(2, int(sqrt(n)) + 1):
		if n % i == 0:
			return False
	return True

# Generates all possible combinations of [0, 1, ..., n - 1]
def generate_combinations(n):
	length = len(str(n))
	items = list(range(0, length))
	replacements = []

	for i in range(1, length):
		replacements.append(itertools.combinations(items, i))
	return replacements

def generate(combination, n):
	primes = []
	x = 0
	if combination[0] == 0:
		x = 1
	else:
		x = 0

	for i in range(x, 10):
		s = ctypes.create_string_buffer(bytes(str(n), 'utf-8'))
		for value in combination:
			s[value] = bytes(str(i), 'utf-8')
		number = int(s.value)
		if is_prime(number):
			primes.append(number)
	return primes

if __name__ == '__main__':
	max_value = 1000000
	done = False
	for i in range(10, max_value):
		if i % 10000 == 0:
			print(i)
		if not is_prime(i):
			continue
		group = generate_combinations(i)
		for combinations in group:
			for combination in combinations:
				family = generate(combination, i)
				if len(family) == 8:
					print(family[0])
					done = True
		if done:
			break