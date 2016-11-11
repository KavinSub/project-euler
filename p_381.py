# Project Euler Problem 381: (prime-k) factorial
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
	return L

def get_primes(sieve):
	return [i for i, b in enumerate(sieve) if b == True]

def extended_euclidean(a, b):
	if a % b == 0: return (0, 1)
	x, y = extended_euclidean(b, a % b)
	x, y = y, x - y*(a//b)
	return x, y

def modinv(a, m):
	x, y = extended_euclidean(a, m)
	if x < 0: x += m
	return x

def factorial_mod(n, p):
	s = 1
	for i in range(n + 1, p):
		s = (s * i) % p
	s = modinv(s, p)
	s = -s + p
	return s % p 

if __name__ == '__main__':
	begin = time.time()

	max_v = 10**2
	primes = get_primes(generate_sieve(max_v))[2:] # Removes 2, 3
	total = 0 
	current = 0
	for i, p in enumerate(primes):
		current = factorial_mod(p - 5, p)
		t = current
		k = current
		for i in range(3, 5)[::-1]:
			t *= (p - i)
			t = t % p
			k += t
		total += (k % p)
	end = time.time()
	print("Time taken:", end - begin)
	print("Solution:", total)