def next_num(n):
	if n % 2 == 0:
		return n//2
	else:
		return 3 * n + 1

def sequence(n):
	c = 1
	while n != 1:
		n = next_num(n)
		c += 1
	return c

if __name__ == '__main__':
	count = 0
	max_num = 0
	for i in range(1, 1000000):
		s = sequence(i)
		if s >= count:
			count = s
			max_num = i
		if i % 10000 == 0:
			print(i)

	print(max_num)