# Project Euler Problem 346: Strong Repunits
# Author: Kavin Subramanyam

import time

if __name__ == '__main__':
	begin = time.time()

	psums = [i + 1 for i in range(10**6 + 1)]
	values = set()
	max_v = 10 ** 12
	total = 1 # To account for 1
	d = 2
	count = 0
	while psums[2] <= max_v:
		i = 2
		while psums[i] <= max_v:
			psums[i] += i**d
			if psums[i] > max_v:
				break
			if psums[i] not in values:
				values.add(psums[i])
				total += psums[i]
			i += 1
			count += 1
		d += 1
	
	end = time.time()
	print("Time taken:", end - begin)
	print("Iterations taken:", count)
	print("Solution:", total)