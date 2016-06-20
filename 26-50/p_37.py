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

# Checks if p is truncatable or not
def is_truncatable(p, prime_sieve):
	s = str(p)
	L = []
	for i in range(len(s)):
		a = int(s[i:])
		b = int(s[:len(s) - i])
		if not prime_sieve[a] or not prime_sieve[b]:
			return False
	return True

if __name__ == '__main__':
	prime_sieve = sieve(1000000)
	primes = set()
	count = 0
	total = 0
	for i in range(10, 1000000):
		if prime_sieve[i] == True:
			if is_truncatable(i, prime_sieve) == True:
				count += 1
				total += i
		if i % 1000 == 0:
			print("{}: {}", i, count)
	print(count)
	print(total)