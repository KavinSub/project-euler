from math import *
from itertools import *

primes = []

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
	L = [i for i in range(len(L)) if L[i] == True]
	return L

prime_factorization = {}

# Returns prime factorization of a number
def factorize(n):
	if n in prime_factorization:
		return prime_factorization[n]
	else:
		if n == 1:
			return []
		L = []
		for prime in primes:
			if n % prime == 0:
				L.extend([prime])
				L.extend(factorize(n//prime))
				prime_factorization[n] = L
				return L

if __name__ == '__main__':
	primes = sieve(1000000)
	count = 0
	i = 2
	while i < 1000000:
		prime_count = len(set(factorize(i)))
		if prime_count == 4:
			count += 1
		else:
			count = 0
		if count == 4:
			print(i - 3)
			break
		if i % 1000 == 0:
			print(i)
		i += 1