def multiply(a, b):
	return (a * b) % 10000000000

if __name__ == '__main__':
	# First calculate the exponent
	num = 1
	for i in range(7830457):
		num = multiply(num, 2)
		if i % 10000 == 0:
			print(i)
	num = multiply(num, 28433)
	print(num + 1)