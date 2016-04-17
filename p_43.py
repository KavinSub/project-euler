from itertools import permutations

primes = [2, 3, 5, 7, 11, 13, 17]
def generate_num(L):
	total = 0
	for i in range(len(L)):
		total += L[-1 * (i + 1)] * 10 ** i
	return total

def check_num(n):
	for i in range(7):
		modulus = 10 ** (9 - i)
		divisor = 10 ** (6 - i)
		num = (n % modulus) // divisor
		if num % primes[i] != 0:
			return False
	return True

if __name__ == '__main__':
	total = 0
	i = 0
	for p in permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
		if p[0] != 0:
			n = generate_num(p)
			if check_num(n):
				total += n
		if i % 10000 == 0:
			print(i)
		i += 1
	print(total)