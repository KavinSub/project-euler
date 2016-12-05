# Project Euler Problem 145: How Many Reversible Numbers Are There Below One-Billion
# Author: Kavin Subramanyam

from math import log
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

# def reverse(n):
# 	power = int(log(n, 10))
# 	c = power
# 	num = 0
# 	while c >= 0:
# 		num += (n % 10)*(10**c)
# 		n = n//10
# 		c -= 1
# 	return num

@memoize
def reverse(n):
	if n == 0: return 0
	return (n % 10)*(10**int(log(n, 10))) + reverse(n//10)

def is_reversible(n):
	return all_odd(n + reverse(n))

odd_digits = set([1, 3, 5, 7, 9])
def all_odd(n):
	while n > 0:
		if n % 10 not in odd_digits:
			return False
		n = n//10
	return True

if __name__ == '__main__':

	begin = time.time()

	count = 0
	max_v = 10**4
	items = []
	for i in range(10, max_v):
		if i % 10 == 0: continue
		if is_reversible(i):
			# print(i, reverse(i), i + reverse(i))
			items.append(i + reverse(i))
			count += 1

	end = time.time()
	print("Time taken:", end - begin)
	print("Solution:", count)
	print(sorted(list(set(items))))