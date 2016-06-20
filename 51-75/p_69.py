from math import *

prime_factorizations = {}
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

# Returns the set of prime factors that makes up n
def factorize(n):
	if n in prime_factorizations:
		return prime_factorizations[n]
	else:
		factors = set()
		for prime in primes:
			if n % prime == 0:
				factors.add(prime)
				factors = factors | factorize(n//prime)
				break
		prime_factorizations[n] = factors
		return factors

# Computes n/phi(n)
def phi(n):
	product = 1
	for p in factorize(n):
		product *= (1 - 1/p)
	return 1/product

if __name__ == '__main__':
	primes = sieve(1000000)
	max_totient = 0
	v = 0
	for i in range(2, 1000000):
		if phi(i) > max_totient:
			max_totient = phi(i)
			v = i
		if i % 1000 == 0:
			print(i)
	print(max_totient)
	print(v)