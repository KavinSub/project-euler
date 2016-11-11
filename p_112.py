# Project Euler Problem 112: Bouncy Numbers
# Author: Kavin Subramanyam

import time

def is_increasing(n):
	c = n % 10
	while n > 0:
		n = n//10
		t = n % 10
		if c < t:
			return False
		c = t
	return True

def is_decreasing(n):
	c = n % 10
	while n > 10:
		n = n//10
		t = n % 10
		if c > t:
			return False
		c = t
	return True

def is_bouncy(n):
	return not is_increasing(n) and not is_decreasing(n)

if __name__ == '__main__':
	begin = time.time()
	target = 0.99
	count = 0
	proportion = 0
	i = 0
	while proportion < target:
		i += 1
		if is_bouncy(i):
			count += 1
		proportion = count/i
	end = time.time()
	print("Time taken:", end - begin)
	print("Solution:", i)