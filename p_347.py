# Project Euler Problem 347: Largest Integer Divisible By Two Primes
# Author: Kavin Subramanyam

from math import sqrt, floor, log
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

def get_primes(sieve):
	primes = []
	for i in range(len(sieve)):
		if sieve[i]:
			primes.append(i)
	return primes

def prime_combinations(primes, max_v):
	pairs = []
	for i in range(len(primes) - 1):
		for j in range(i + 1, len(primes)):
			if primes[i] * primes[j] > max_v:
				break
			pairs.append((primes[i], primes[j]))
	return pairs

def M(p, q, n):
	log_p = int(log(n, p))
	log_q = int(log(n, q))

	max_v = p*q
	for i in range(1, log_p + 1):
		for j in range(1, log_q + 1):
			v = (p**i)*(q**j)
			if v > max_v and v <= n:
				max_v = v
	return max_v

if __name__ == '__main__':
	begin = time.time()

	max_v = 10 ** 7
	total = 0
	primes = get_primes(generate_sieve(max_v//2))
	pairs = prime_combinations(primes, max_v)
	count = 0
	for pair in pairs:
		count += 1
		q = M(*pair, max_v)
		total += q
	end = time.time()
	print("Time taken:", end - begin)
	print("Solution:", total)