from math import *

def is_increasing(n):
	digits = int(log(n, 10))
	prev = 0
	for i in range(0, digits + 1):
		d = n // (10 ** (digits - i))
		n = n % (10 ** (digits - i))
		if d < prev:
			return False
		prev = d
	return True

def is_decreasing(n):
	digits = int(log(n, 10))
	prev = 9
	for i in range(0, digits + 1):
		d = n / (10 ** (digits - i))
		n = n % (10 ** (digits - i))
		if d > prev:
			return False
		prev = d
	return True

def is_bouncy(n):
	return not is_increasing(n) and not is_decreasing(n)

if __name__ == '__main__':
	T = 99
	bouncy = 0
	proportion = bouncy/T
	# while proportion < 0.90:
	# 	T += 1
	# 	if is_bouncy(T):
	# 		bouncy += 1
	# 	proportion = bouncy/T
	# 	if T % 10000 == 0:
	# 		print("T: {}, proportion: {}".format(T, proportion))
	# print(proportion)
	# print(T)