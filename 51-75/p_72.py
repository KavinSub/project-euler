# Project Euler Problem 72: Counting Fractions
# Author: Kavin Subramanyam

from math import sqrt
import time
from functools import reduce
from operator import mul

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
	return L

max_value = 1000000
prime_sieve = generate_sieve(max_value)

def is_prime(n):
	return prime_sieve[n]

def get_primes(sieve):
	return [i for i in range(len(sieve)) if sieve[i] == True]

def prime_divisors(n):
	pd = []
	for i in range(1, int(sqrt(n)) + 1):
		if is_prime(i):
			if n % i == 0:
				pd.append(i)
				v = n//i
				if is_prime(v) and v != i:
					pd.append(v)
	return pd

def phi(n):
	if is_prime(n): return n - 1
	den = prime_divisors(n)
	num = [p - 1 for p in den]
	return (n * reduce(mul, num, 1))//reduce(mul, den, 1)


if __name__ == '__main__':
	begin = time.time()

	count = 1 # {1/2}
	memo = {}
	primes = get_primes(prime_sieve)
	for p in primes:
		if p > int(sqrt(max_value)): memo[p] = p -1
		x = p - 1
		power = 1
		while p**power < max_value:
			t = p**power
			v = x*(p**(power - 1))
			memo[t] = v
			power += 1

	for p in primes:
		k = 1
		while k*p <= max_value:
			if k not in memo:
				k += 1
				continue
			if k % p == 0:
				memo[k*p] = phi(k*p) 
				k += 1
				continue
			v = (p - 1)*memo[k]
			memo[k*p] = v
			power = 2
			while (k*p)**power <= max_value:
				t = (k*p)**power
				r = v*((k*p)**(power - 1))
				memo[t] = r
				power += 1
			k += 1


	for i in range(3, max_value + 1):
		count += memo[i]

	end = time.time()
	print("Time taken:", end - begin)
	print("Solution:", count)