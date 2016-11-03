# Project Euler Problem 66: Diophantine Equation
# Author: Kavin Subramanyam

from math import sqrt

def compute(D, x, y):
	return x**2 - D * (y**2)

# The broken version
# def continued_fraction(n):
# 	decimal.getcontext().prec = 300
# 	x = Decimal(n).sqrt()
# 	a = int(x)
# 	sequence = [a]
# 	for i in range(100):
# 		x = 1/(x - a)
# 		a = int(x)
# 		sequence.append(a)
# 	return sequence

def continued_fraction(n):
	r = int(sqrt(n))
	sequence = [r]
	a = r
	p = 0
	q = 1
	while True:
		p = a*q - p
		q = (n - p*p)//q
		a = (r + p)//q
		sequence.append(a)
		if q == 1:
			break
	return sequence

def is_perfect_square(n):
	return n == int(sqrt(n)) ** 2

if __name__ == '__main__':
	max_value = 1000
	max_x = 1
	max_d = 2
	for i in range(2, max_value + 1):
		if is_perfect_square(i):
			continue
		sequence = continued_fraction(i)
		numerators = [0, 1]
		denominators = [1, 0]
		k = 0
		while True:
			term = sequence[k]

			n = numerators[1] * term + numerators[0]
			numerators.pop(0)
			numerators.append(n)

			d = denominators[1] * term + denominators[0]	
			denominators.pop(0)
			denominators.append(d)

			v = compute(i, n, d)
			if v == 1:
				if n > max_x:
					max_x = n
					max_d = i
				break

			k += 1
			if k == len(sequence):
				k = 1
	print(max_d)