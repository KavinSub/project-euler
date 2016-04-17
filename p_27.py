from math import *

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
	return L

def compute_quadratic(a, b, n):
	return (n ** 2) + (a * n) + b

prime_sieve = sieve(1000000)

m = -1
product = 0
for a in range(-1000, 1001):
	for b in range(-1000, 1001):
		n = -1
		while True:
			prime = compute_quadratic(a, b, n + 1)
			if prime_sieve[prime] == True:
				n += 1
			else:
				break
			if n > m:
				m = n
				product = a * b
print(m + 1)
print(product)