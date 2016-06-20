# Computes the sum of digits of n
def digit_sum(n):
	total = 0
	while n > 0:
		total += n % 10
		n = n//10
	return total

if __name__ == '__main__':
	max_digit_sum = 0
	for a in range(1, 100):
		num = 1
		for b in range(1, 100):
			num *= a
			max_digit_sum = max(digit_sum(num), max_digit_sum)
	print(max_digit_sum)