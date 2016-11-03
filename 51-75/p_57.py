# Project Euler Problem 57: Square root convergents
# Author: Kavin Subramanyam

from fractions import Fraction

def numerator_more_digits(fraction):
	return len(str(fraction.numerator)) > len(str(fraction.denominator))

if __name__ == '__main__':
	count = 0
	current = Fraction(0, 1)
	for i in range(1000):
		current = 1/(2 + current)
		if numerator_more_digits(1 + current):
			count += 1
	print(count)