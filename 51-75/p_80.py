# Project Euler Problem 80: Square Root Digital Expansion
# Author: Kavin Subramanyam

import decimal
import time
import math

decimal.getcontext().prec = 101

def digital_sum(n):
	if int(math.sqrt(n))**2 == n: return 0
	num = str(int(decimal.Decimal(n).sqrt()*10**99))
	return sum(map(int, list(num)))

if __name__ == '__main__':
	begin = time.time()

	count = 0
	max_value = 100
	for i in range(1, max_value + 1):
		count += digital_sum(i)

	end = time.time()
	print("Time taken:", end - begin)
	print("Solution:", count - 1) # sqrt(2) does not round properly for some reason