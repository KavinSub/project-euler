# Project Euler Problem 64: Odd period square roots
# Author: Kavin Subramanyam


from math import sqrt

def continued_fraction(n):
	r = int(sqrt(n))
	sequence = [r]
	if r**2 == n: # If n is a perfect square
		return sequence
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

if __name__ == '__main__':
	count = 0
	max_value = 10000
	for i in range(1, max_value + 1):
		sequence = continued_fraction(i)
		if len(sequence) % 2 == 0:
			count += 1
	print(count)