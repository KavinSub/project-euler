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
	L = [i for i in range(len(L)) if L[i] == True]
	return (L, set(L))

if __name__ == '__main__':
	(primes, set_primes) = sieve(1000000)
	max_prime = 0
	prime_chain = 0
	for i in range(len(primes)):
		chain = 0
		total = 0
		j = i
		while total < 1000000:
			if j > len(primes) - 1:
				break
			total += primes[j]
			chain += 1
			j += 1
			if total in set_primes:
				if chain > prime_chain:
					prime_chain = chain
					max_prime = total
		if i % 1000 == 0:
			print(i)
	print("Max chain length: {}\tPrime: {}".format(prime_chain, max_prime))