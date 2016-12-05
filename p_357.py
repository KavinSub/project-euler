# Project Euler Problem 357: Prime Generating Integers
# Author: Kavin Subramanyam

from math import sqrt, floor
import time

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

def sieve(n):
	L = [True] * (n + 1)
	L[0] = False
	L[1] = False
	prime = 2
	k = prime
	while prime < int(floor(sqrt(n))) + 1:
		while k <= n - prime:
			k += prime
			L[k] = False
		prime += 1
		while L[prime] == False:
			prime += 1
		k = prime
		print(k)
	return L

max_value = 10 ** 8
prime_sieve = sieve(max_value)
print("sieve complete.")

def is_prime(n):
	return prime_sieve[n]

def is_prime_generating(n):
	# if not is_prime(n + 1): return False
	# if not is_prime(2 + n//2): return False
	if is_prime(n//2):
		if not is_prime(2 + n//2) or not is_prime(n + 1):
			return False
		return True
	for i in range(1, int(sqrt(n)) + 1):
		if n % i == 0:
			if not is_prime(i + n//i):
				return False
	return True

if __name__ == '__main__':
	# max_value = 10 ** 8

	count = 3
	i = 6
	x = 1
	while i <= max_value:
		if is_prime_generating(i):
			count += i
		i += 4
		x += 1
		if x % 10000 == 0:
			print(i)
	print(count)