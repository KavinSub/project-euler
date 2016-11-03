# Project Euler problem 26 - Reciprocal Cycles
# Author: Kavin Subramanyam

def cycle_length(n):
	if n % 2 != 0 and n % 5 != 0:
		t = 1
		while 10**t % n != 1:
			t += 1
		return t
	else:
		values = {}
		x = 1
		while 10**x % n not in values.keys():
			values[10**x % n] = x
			x += 1
		s = values[10**x % n]
		t = x - s
		return t

if __name__ == '__main__':
	max_length = 0
	num = 0
	for i in range(2, 1000):
		cycle = cycle_length(i)
		if cycle > max_length:
			max_length = cycle
			num = i
	print(num)