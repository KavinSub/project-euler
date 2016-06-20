from math import *

def divisors(n):
	L = []
	for i in range(1, floor(sqrt(n)) + 1):
		if n % i == 0 and i ** 2 != n:
			L.append(i)
			L.append(n // i)
		elif i ** 2 == n:
			L.append(i)
	return L

if  __name__ == '__main__':
	i = 1
	T = 0
	while True:
		T += i
		i += 1
		if len(divisors(T)) > 500:
			print(T)
			break
		if i % 1000 == 0:
			print(i)