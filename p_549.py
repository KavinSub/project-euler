# Project Euler Problem 549: Divsibility of Factorials
# Author: Kavin Subramanyam

from math import sqrt, floor, log
import time

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

max_value = 10 ** 2
prime_sieve = sieve(max_value)
print("Sieve completed.")

def is_prime(n):
	return prime_sieve[n]

def minimum_number(prime, exponent):
	# count = 0
	# current = prime
	# while count < exponent:
	# 	count += integer_divisions(current, prime)
	# 	if count < exponent:
	# 		current += prime
	# return current
	if exponent == 1: return prime
	current = prime * exponent
	x = 2
	a = 1
	while current > prime ** x:
		current -= prime**(x-1)
		if current < prime ** x:
			current = prime**x
		else:
			x += 1
	return current

def integer_divisions(n, k):
	count = 0
	while n % k == 0:
		count += 1
		n = n//k
	return count

def triangle_number(n):
	return (n * (n + 1))//2

if __name__ == '__main__':
	begin = time.time()

	total = 0
	prime = 2
	result = [0 for i in range(max_value + 1)]
	while prime < max_value:
		current = prime
		while current <= max_value:
			if is_prime(current): result[current] = prime
			else: 
				result[current] = max(result[current], minimum_number(prime, integer_divisions(current, prime)))
			current += prime
		prime += 1
		while prime < max_value and not is_prime(prime):
			prime += 1
	end = time.time()
	print("Time elapsed:", end - begin)
	print(sum(result))