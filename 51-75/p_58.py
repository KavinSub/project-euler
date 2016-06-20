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
		print(k)
	P = set()
	for i in range(len(L)):
		if L[i] == True:
			P.add(i)
	return P

# Generates a range for prime spiral level k
def generate_range(k):
	if k <= 1:
		return range(1, 2)
	else:
		return range((2 * (k - 1) - 1) ** 2 + 1, (2 * k - 1) ** 2 + 1)

def is_prime(n):
	if n < 2:
		return False
	for i in range(2, int(sqrt(n)) + 1):
		if n % i == 0:
			return False
	return True

if __name__ == '__main__':
	# T = 1000000000
	# primes = sieve(T)
	# ratio = 1
	# diagonal = 1
	# side = 1
	# k = 1
	# count = 0
	# while ratio >= 0.1 or k < 5:
	# 	for i in generate_range(k):
	# 		if i in primes and (((2 * k - 1) ** 2) - i) % (side - 1) == 0:
	# 			count += 1
	# 	ratio = count/diagonal
	# 	print("count: {}, diagonal: {}, side:{}, ratio: {}".format(count, diagonal, side, ratio))
	# 	k += 1
	# 	side += 2
	# 	diagonal = 2 * (2 * k - 1) - 1

	ratio = 1
	diagonal = 5
	side = 3
	k = 2
	p = 1
	count = 0
	while ratio >= 0.1 or k < 5:
		for i in range(1, 5):
			if is_prime(p + (side - 1) * i):
				count += 1
		p = p + (side - 1) * 4
		ratio = count/diagonal
		print("count: {}, diagonal: {}, side:{}, ratio: {}".format(count, diagonal, side, ratio))
		k += 1
		side += 2
		diagonal += 4