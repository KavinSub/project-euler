# Project Euler Problem 65: Convergents of e
# Author: Kavin Subramanyam


if __name__ == '__main__':
	numerators = [0, 1]
	denominators = [1, 0]
	max_value = 100
	k = 1
	for i in range(max_value):
		term = 1
		if i == 0:
			term = 2
		elif i % 3 == 2:
			term = 2 * k
			k += 1
		n = term * numerators[1] + numerators[0]
		numerators.pop(0)
		numerators.append(n)

		d = term * denominators[1] + denominators[0]
		denominators.pop(0)
		denominators.append(d)
	x = numerators[1]
	print(sum([int(c) for c in str(x)]))