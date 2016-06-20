squares = {}

def sum_squares(n):
	num = 0
	while n > 0:
		num += (n % 10) ** 2
		n = n//10
	return num

def square_chain(n):
	if n in squares:
		return squares[n]
	else:
		if n == 1 or n == 89:
			return n
		else:
			k = square_chain(sum_squares(n))
			squares[n] = k
			return k

if __name__ == '__main__':
	C = 0
	for i in range(1, 10000000):
		if square_chain(i) == 89:
			C += 1
		if i % 100000 == 0:
			print(i)
	print(C)