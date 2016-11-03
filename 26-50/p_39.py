# Project Euler problem 39 - Integer Right Triangles
# Author: Kavin Subramanyam

from math import sqrt, floor
from collections import Counter

def hypotenuse(a, b):
	return sqrt(a**2 + b**2)

if __name__ == '__main__':
	solution_count = Counter()
	count = 0
	for a in range(1, 500):
		for b in range(1, 500):
			if a <= b:
				if a + b <= 500:
					h = hypotenuse(a, b)
					if h == floor(h):
						h = int(h)
						if a + b + h <= 1000:
							p = a + b + h
							solution_count[p] += 1
	print(solution_count.most_common(1))