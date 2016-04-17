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
	C = [i for i in range(len(L)) if L[i] == False and i % 2 == 1]
	L = [i for i in range(len(L)) if L[i] == True]
	return (L, C[1:])

# Generates first n squares
def squares(n):
	s = set()
	for i in range(1, n + 1):
		s.add(i * i)
	return s

if __name__ == '__main__':
	primes, odd_composite = sieve(1000000)
	square_numbers = squares(10000)

	i = 0
	while True:
		j = 0
		goldbach = False
		while primes[j] < odd_composite[i]:
			if abs(primes[j] - odd_composite[i])//2 in square_numbers:
				goldbach = True
				break
			j += 1
		if not goldbach:
			print(odd_composite[i])
			break
		if i % 100 == 0:
			print(i)
		i += 1