# Project Euler Problem 205: Dice Game
# Author: Kavin Subramanyam

from itertools import product
from collections import defaultdict
from decimal import *
import time

getcontext().prec = 50

def calculate_probabilities(p, total):
	for k in p.keys():
		p[k] = Decimal(p[k])/Decimal(total)

if __name__ == '__main__':
	begin = time.time()
	fd_outcomes = product([1, 2, 3, 4], repeat=9)
	sd_outcomes = product([1, 2, 3, 4, 5, 6], repeat=6)

	four_prob = defaultdict(int)
	six_prob = defaultdict(int)

	for o in fd_outcomes:
		four_prob[sum(o)] += 1
	for o in sd_outcomes:
		six_prob[sum(o)] += 1

	calculate_probabilities(four_prob, 4**9)
	calculate_probabilities(six_prob, 6**6)

	probability = 0
	for i in range(4, 37):
		for j in range(6, i):
			probability += four_prob[i]*six_prob[j]
	end = time.time()
	print("Time taken:", end - begin)
	print("Solution:", probability)