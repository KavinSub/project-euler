# Project Euler Problem 500: Problem 500!!!
# Author: Kavin Subramanyam

from math import sqrt
import time

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

# 500500th prime is 7,376,507
prime_sieve = generate_sieve(7500000)

def get_divisors(n):
	divisors = []
	for i in range(1, n + 1):
		if n % i == 0: divisors.append(i)
	return divisors

def is_prime(n):
	return prime_sieve[n]


if __name__ == '__main__':
	begin = time.time()

	i = 1
	count = 1
	max_count = 500500
	n = 1
	factors = set()
	while count <= max_count:
		if count % 1000 == 0: print(count)
		if i in factors:
			factors.add(i**2)
			n *= i
			count += 1
			factors.remove(i)
		elif is_prime(i):
			factors.add(i**2)
			n *= i
			count += 1
		i += 1
		n = n % 500500507

	end = time.time()
	print("Time taken:", end - begin)
	print("Solution:", n)