from math import sqrt

def is_prime(n):
	for i in range(2, int(sqrt(n)) + 1):
		if n % i == 0:
			return False
	return True

def divide_by_one(n):
	pass

if __name__ == '__main__':
	pass