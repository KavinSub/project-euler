# Project Euler Problem 63: Powerful digit sum
# Author: Kavin Subramanyam

if __name__ == '__main__':
	count = 1 # 1 ** 1 = 1 -> is a 1 digit first power
	power = 1
	while 9 ** power >= 10 ** (power - 1):
		for i in range(2, 10):
			num = i ** power
			if len(str(num)) == power:
				count += 1
		power += 1
	print(count)