# Project Euler Problem 70: Totient Permutation
# Author: Kavin Subramanyam

from math import sqrt
from functools import reduce
from operator import mul
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
	return L

max_prime = 10**7
prime_sieve = generate_sieve(max_prime)

def is_prime(n):
	return prime_sieve[n]

def get_primes(sieve):
	return [i for i in range(len(sieve)) if sieve[i]]

def get_prime_divisors(n):
	primes = []
	for i in range(1, int(sqrt(n)) + 1):
		if n % i == 0:
			if is_prime(i): primes.append(i)
			v = n//i
			if is_prime(v) and v != i: primes.append(v)
	return primes

def phi(n):
	if is_prime(n): return n - 1
	den = get_prime_divisors(n)
	num = [p - 1 for p in den]	
	return (n * reduce(mul, num, 1))//reduce(mul, den, 1)

def is_palindrome(a, b):
	return stringify(a) == stringify(b)

def stringify(n):
	digits = [0] * 10
	while n > 0:
		digits[n % 10] += 1
		n = n//10
	return "".join([str(d) for d in digits])

if __name__ == '__main__':
	begin = time.time()

	memo = {1:1}
	totient_permutations = []
	primes = get_primes(prime_sieve)
	for p in primes:
		if p > int(sqrt(max_prime)): memo[p] = p - 1
		x = p - 1
		power = 1
		while p**power < max_prime:
			t = p**power
			v = x*(p**(power - 1))
			memo[t] = v
			if is_palindrome(t, v): totient_permutations.append((t, v))
			power += 1

	for p in primes:
		k = 1
		if p > int(sqrt(max_prime)): break
		while k*p < max_prime:
			if k*p in memo or k % p == 0 or k not in memo: 
				k += 1
				continue
			v = (p - 1)*memo[k]
			memo[k*p] = v
			if is_palindrome(k*p, v): totient_permutations.append((k*p, v))
			k += 1

	solution = min(totient_permutations, key=lambda x: x[0]/x[1])[0]

	end = time.time()
	print("Time taken:", end - begin)
	print("Solution:", solution)