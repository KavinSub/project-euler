# Project Euler Problem 500: Problem 500!!!
# Author: Kavin Subramanyam

def get_divisors(n):
	divisors = []
	for i in range(1, n + 1):
		if n % i == 0: divisors.append(i)
	return divisors

if __name__ == '__main__':
	max_divisors = 0
	max_v = 1000
	for i in range(max_v):
		count = len(get_divisors(i))
		if count > max_divisors:
			print(i, count)
			max_divisors = count