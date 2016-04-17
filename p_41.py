from math import *

digits = "123456789"

def is_pandigital(n):
	s = str(n)
	return set(digits[:len(s)]) == set(s)

def sieve(n):
	L = [True] * (n + 1)
	L[0] = False
	L[1] = False
	prime = 2
	k = prime
	print("Begin sieve.")
	while prime < int(floor(sqrt(n))) + 1:
		while k <= n - prime:
			k += prime
			L[k] = False
		prime += 1
		while L[prime] == False:
			prime += 1
		k = prime
		print(k)
	S = []
	for i in range(len(L)):
		if L[i] == True:
			S.append(i)
	return S

if __name__ == '__main__':
	primes = sieve(100000000)
	print("Sieve completed.")
	pandigital = 0
	for prime in primes:
		if is_pandigital(prime):
			pandigital = prime
	print(pandigital)