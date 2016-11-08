# Project Euler Problem 387: Harshad Numbers
# Author: Kavin Subramanyam

from math import sqrt, floor
import time

def memoize(func):
	values = {}
	def inner(*args):
		if args in values:
			return values[args]
		else:
			result = func(*args)
			values[args] = result
			return result
	return inner


@memoize
def is_prime(n):
	for i in range(2, int(sqrt(n)) + 1):
		if n % i == 0:
			return False
	return True

def digit_sum(n):
	return sum([int(c) for c in str(n)])

@memoize
def right_truncatable(n):
	if n < 10: return True
	return n % digit_sum(n) == 0 and right_truncatable(n//10) 

def strong(n):
	result = digit_sum(n)
	if n % result == 0:
		if is_prime(n//result):
			return True
	return False

def is_strong_right(n):
	return strong(n) and right_truncatable(n)

def is_super(n):
	return is_prime(n) and right_truncatable(n//10) and strong(n//10)

def generate_candidates(n):
	return [n * 10 + 2 * i + 1 for i in range(0, 5)]

def generate_harshad_numbers(n):
	candidates = [10 * n + i for i in range(0, 10) if right_truncatable(10 * n + i)]
	return candidates

if __name__ == '__main__':
	# begin = time.time()
	# max_value = 10 ** 4
	# super_sum = 0
	# x = 101
	# i = 0
	# while x < max_value:
	# 	if is_super(x):
	# 		super_sum += x
	# 	x += 2  
	# 	i += 1
	# 	if i % 10000 == 0:
	# 		print(i)
	# elapsed = time.time() - begin
	# print("Time elapsed:", elapsed)
	# print(super_sum)

	# begin = time.time()
	# max_value = 10 ** 3
	# super_sum = 0
	# x = 10
	# while x < max_value:
	# 	if is_strong_right(x):
	# 		for c in generate_candidates(x):
	# 			if is_prime(c):
	# 				super_sum += c
	# 	if x % 10000 == 0:
	# 		print(x, super_sum)
	# 	x += 1
	# elapsed = time.time() - begin
	# print("Time elapsed:", elapsed)
	# print(super_sum)


	# new approach, generate right truncatable primes, check if prime or not
	 # max_value = 10 ** 4
	 # x = 10
	 # while x < max_value:
	 # 	if right_truncatable(x):
	 # 		print(x)
	 # 	x += 1

	 begin = time.time()

	 prime_sum = 0
	 current = []
	 x = 10
	 while x < 100:
	 	if right_truncatable(x):
	 		current.append(x)
	 	x += 1
	 
	 i = 2
	 while i <= 13:
	 	x = 10 ** i
	 	temp = []
	 	for number in current:
	 		candidates = generate_candidates(number)
	 		for candidate in candidates:
	 			if strong(candidate//10) and is_prime(candidate):
	 				prime_sum += candidate
	 	for number in current:
	 		temp.extend(generate_harshad_numbers(number))
	 	current = temp
	 	print(i)
	 	i += 1
	 print("Time elapsed:", time.time() - begin)
	 print(prime_sum)


