# Project Euler Problem 60: Prime Pair Sets
# Author: Kavin Subramanyam

from math import sqrt
import time
from itertools import combinations

def memoize(func):
	memo = {}
	def inner(*args):
		if args in memo: return memo[args]
		else:
			result = func(*args)
			memo[args] = result
			return result
	return inner

def generate_sieve(n):
	L = [True] * (n + 1)
	L[0] = False
	L[1] = False
	prime = 2
	k = prime
	while prime < int(sqrt(n)) + 1:
		while k <= n - prime:
			k += prime
			L[k] = False
		prime += 1
		while L[prime] == False:
			prime += 1
		k = prime
		print(k)
	return L

max_prime = 10 ** 6
prime_sieve = generate_sieve(max_prime)
print("Sieve complete.")


def is_prime_sqrt(n):
	for i in range(2, int(sqrt(n)) + 1):
		if n % i == 0:
			return False
	return True

def is_prime(n):
	if n > max_prime: return is_prime_sqrt(n)
	return prime_sieve[n]

def get_primes(sieve, max_value):
	return [i for i in range(max_value + 1) if sieve[i] == True]

@memoize
def decompose_prime(n):
	if n < 10: return [n]
	primes = []
	prime_set = set()
	i = 1
	while 10**i < n:
		pre = n//10**i
		suff = n % (10**i)
		if suff <= 10**(i-1):
			i += 1
			continue
		for x in pre, suff:
			if is_prime(x) and x not in prime_set:
				primes.append(x)
				prime_set.add(x)
		# if is_prime(pre): primes.append(pre)
		# if is_prime(suff): primes.append(suff)
		i += 1
	for p in primes:
		if p < 10: continue
		new_primes = decompose_prime(p)
		for np in new_primes:
			if np not in prime_set:
				primes.append(np)
				prime_set.add(np)
	return primes

@memoize
def is_prime_pair(a, b):
	return is_prime(int(str(a) + str(b))) and is_prime(int(str(b) + str(a)))

def check_all_pairs(primes):
	for i in range(len(primes) - 1):
		for j in range(i + 1, len(primes)):
			if not is_prime_pair(primes[i], primes[j]):
				return False
	return True

if __name__ == '__main__':
	begin = time.time()
	max_v = max_prime
	target = 4
	solution = None
	complete = False
	for i in range(2, max_v + 1):
		if i % 100000 == 0: print(i)
		if is_prime(i):
			primes = decompose_prime(i)
			if len(primes) >= target:
				primes.sort()
				combs = combinations(primes, target)
				for c in combs:
					if check_all_pairs(c) and len(c) == target:
						solution = c
						complete = True
		if complete: break
	end = time.time()
	print("Time taken:", end - begin)
	print("Solution", solution, sum(solution))

	# begin = time.time()
	# max_value = 1000
	# primes = get_primes(prime_sieve, max_value)
	# target = 4
	# solution = []
	# combs = combinations(primes, target)
	# valid_pairs = []
	# for i, c in enumerate(combs):
	# 	if i % 100000 == 0: print(i)
	# 	if check_all_pairs(c):
	# 		solution = c
	# 		break
	# 		# valid_pair.append(c)
	# end = time.time()
	# print("Time taken:", end - begin)
	# print(len(valid_pair))
	# print("Solution:", solution, sum(solution))