from math import *

def sum_prop_div(n):
	if n <= 1:
		return 0
	s = 1
	for i in range(2, floor(sqrt(n)) + 1):
		if n % i == 0 and i ** 2 != n:
			s += i
			s += n // i
		elif i ** 2 == n:
			s += i
	return s

if __name__ == '__main__':
	amicable_numbers = set()

	for i in range(1, 10000):
		a = sum_prop_div(i)
		b = sum_prop_div(a)
		if i == b and i != a:
			amicable_numbers.add(a)
			amicable_numbers.add(b)

	print(sum(amicable_numbers))