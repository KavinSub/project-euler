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

def rotate_num(n):
	k = str(n)
	if n < 2:
		return n
	else:
		return int(k[-1] + k[:len(k) - 1])

def all_rotations(n):
	k = str(n)
	if n < 2:
		return [n]
	else:
		L = []
		for i in range(len(k)):
			k = rotate_num(int(k))
			L.append(int(k))
	return L

def all_prime(rotations, sieve):
	for num in rotations:
		if sieve[num] == False:
			return False
	return True

if __name__ == '__main__':
	prime_sieve = sieve(1000000)
	
	circular_primes = set()

	for i in range(len(prime_sieve)):
		if prime_sieve[i] == True:
			rotations = all_rotations(i)
			if all_prime(rotations, prime_sieve):
				circular_primes.add(i)
		if i % 10000 == 0:
			print(i)
	print(len(circular_primes))