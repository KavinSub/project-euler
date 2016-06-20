from math import factorial
from itertools import *
factorials = {0:1, 1: 1, 2: 2, 3: factorial(3), 4:factorial(4), 5:factorial(5), 6:factorial(6),
			  7:factorial(7), 8:factorial(8), 9:factorial(9)}

def factorial_sum(n):
	total = 0
	while n > 0:
		total += factorials[n % 10]
		n = n // 10
	return total
if __name__ == '__main__':
	total = 0
	for i in range(3, 10000000):
		if factorial_sum(i) == i:
			total += i
		if i % 10000 == 0:
			print(i)
	print(total)