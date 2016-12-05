# Project Euler Problem 87: Prime Power Triples
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

max_value = 7200
prime_sieve = generate_sieve(max_value)

def get_primes():
	return [i for i in range(len(prime_sieve)) if prime_sieve[i] == True]

maximum = 50000000
encountered = set()

def count_triples(primes, e, max_value):
	global encountered
	if e == 4:
		count = 0
		i = 0
		p = primes[i]
		while p**e <= max_value:
			if max_value - p**e not in encountered: 
				encountered.add(max_value - p**e)
				count += 1
			i += 1
			p = primes[i]
		return count
	else:
		count = 0
		i = 0
		p = primes[i]
		while p**e < max_value:
			count += count_triples(primes, e + 1, max_value - p**e)
			i += 1
			p = primes[i]
		return count

if __name__ == '__main__':
	begin = time.time()

	primes = get_primes()
	solution = count_triples(primes, 2, maximum)

	end = time.time()
	print("Time taken:", end - begin)
	print("Solution:", solution)