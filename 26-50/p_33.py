# Project Euler problem 33 - Digit Canceling Fractions
# Author: Kavin Subramanyam

def gcd(a, b):
	while b != 0:
		temp = b
		b = a % b
		a = temp
	return a

# Assumes a, b are two digit numbers
def common_digit(a, b):
	fdigita = a//10
	sdigita = a % 10
	fdigitb = b//10
	sdigitb = b % 10
	if fdigita == fdigitb:
		return (fdigita, sdigita, sdigitb)
	if fdigita == sdigitb:
		return (fdigita, sdigita, fdigitb)
	if sdigita == fdigitb:
		return (sdigita, fdigita, sdigitb)
	if sdigita == sdigitb:
		return (sdigita, fdigita, fdigitb)
	return (-1, 0, 0)


if __name__ == '__main__':

	valid_fractions = [(4, 8)]
	count = 0
	for x in range(10, 99): # numerator
		for y in range(11, 100): # denominator
			d = common_digit(x, y)
			if d[0] != -1 and d[0] != 0: 
				if d[1] != d[2]:
					v = gcd(x, y)
					if x//v == d[1] and y//v == d[2] and (x//v)/(y//v) < 1:
						count += 1
						valid_fractions.append((d[1], d[2]))
	prod = [1, 1]
	for x, y in valid_fractions:
		prod[0] *= x
		prod[1] *= y
	print(prod)