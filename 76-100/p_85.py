# Project Euler Problem 85: Counting Rectangles
# Author: Kavin Subramanyam

import time

def triangle(n):
	return (n * (n + 1))//2

def rectangles(a, b):
	return triangle(a) * triangle(b)

if __name__ == '__main__':
	begin = time.time()
	target = 2000000
	min_diff = target
	area = 0
	i = 1
	while True:
		count = rectangles(1, i)
		if count > target and abs(count - target) >= min_diff:
			break
		for j in range(2, i + 1):
			count += j*triangle(i)
			if abs(count - target) < min_diff:
				min_diff = abs(count - target)
				area = i*j
			if count > target:
				break
		i += 1
	end = time.time()
	print("Time taken:", end - begin)
	print("Solution:", area)