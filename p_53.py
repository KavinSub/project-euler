from math import factorial, ceil

factorials = {}

def combinations(n, r):
	f_n = factorial(n) if n not in factorials else factorials[n]
	f_nr = factorial(n - r) if (n - r) not in factorials else factorials[n - r]
	f_r = factorial(r) if r not in factorials else factorials[r]

	return (f_n)//(f_nr * f_r)

if __name__ == '__main__':
	count = 0
	for n in range(23, 101):
		for r in range(0, n//2 + 1):
			if combinations(n, r) > 1000000:
				if n % 2 == 0 and r == n // 2:
					count += 1
				else:
					count += 2
		if n % 5 == 0:
			print(n)
	print(count)