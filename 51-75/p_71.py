# Project Euler Problem 71: Ordered Fractions
# Author: Kavin Subramanyam

def gcd(a, b):
	while b != 0:
		a, b = b, a % b
	return a


if __name__ == '__main__':
	d = 100
	denominator = d - d % 7
	numerator = (denominator//7) * 3

	divisor = gcd(numerator - 1, denominator)
	fraction = [numerator - 1//divisor, denominator//divisor]
	while fraction[1] > d:
		denominator -= 1
		divisor = gcd(numerator, denominator)
		fraction[0] = fraction[0]//divisor
		fraction[1] = fraction[1]//divisor
	print(fraction[0], "/", fraction[1])