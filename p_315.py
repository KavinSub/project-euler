# Project Euler Problem 315: Digital Root Clocks
# Author: Kavin Subramanyam

from math import sqrt
import time

def memoize(func):
	memo = {}
	def inner(*args):
		if args in memo: return memo[args]
		else:
			result = func(*args)
			memo[args] = result
			return result
	return inner

def generate_sieve(n):
	L = [True] * (n + 1)
	L[0] = False
	L[1] = False
	prime = 2
	k = prime
	while prime < int(sqrt(n)) + 1:
		while k <= n - prime:
			k += prime
			L[k] = False
		prime += 1
		while L[prime] == False:
			prime += 1
		k = prime
		print(k)
	return L

min_value = 10**7
max_value = 2*(10**7)
prime_sieve = generate_sieve(max_value)
print("Sieve complete.")

def is_prime(n):
	return prime_sieve[n]

digits = {
	0: 0b1110111,
	1: 0b0100100,
	2: 0b1011101,
	3: 0b1101101,
	4: 0b0101110,
	5: 0b1101011,
	6: 0b1111011,
	7: 0b0100111,
	8: 0b1111111,
	9: 0b1101111
}

def sam_transitions(num):
	cost = 0
	while num > 0:
		cost += 2*count_ones(digits[num % 10])
		num = num//10
	return cost

def total_sam_transitions(num):
	count = 0
	while num >= 10:
		count += sam_transitions(num)
		num = digital_sum(num)
	count += sam_transitions(num)
	return count

# p = previous num, c = current num
def max_transitions(p, c):
	return count_ones(segrep(p) ^ segrep(c))

def total_max_transitions(num):
	c = 0
	count = 0
	while num >= 10:
		count += max_transitions(c, num)
		c = num
		num = digital_sum(num)
	count += max_transitions(c, num) + max_transitions(digital_sum(num), 0)
	return count

def segrep(n):
	constant = 2**7
	rep = 0
	exp = 0
	while n > 0:
		rep += (constant**exp)*(digits[n % 10])
		exp += 1
		n = n//10
	return rep

# Counts 1s in bit string of n
@memoize
def count_ones(n):
	count = 0
	while n > 0:
		if n & 1 == 1: count += 1
		n = n >> 1
	return count

def digital_sum(n):
	digits = 0
	while n > 0:
		digits += n % 10
		n = n//10
	return digits

if __name__ == '__main__':
	begin = time.time()
	sam_count = 0
	max_count = 0
	for i in range(min_value, max_value + 1):
		if i % (10**5) == 0: print(i)
		if not is_prime(i): continue
		sam_count += total_sam_transitions(i)
		max_count += total_max_transitions(i)
	end = time.time()
	print("Time taken:", end - begin)
	print("Solution:", sam_count - max_count)