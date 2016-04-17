from math import factorial

factorials = {0:1, 1:1, 2:2, 3:6, 4:24, 5:120, 6:720, 7:5040, 8:40320, 9:362880}

def factorial_chain(n):
	T = 0
	while n > 0:
		T += factorials[n % 10]
		n = n//10
	return T

if __name__ == '__main__':
	count = 0
	for i in range(1, 1000000):
		k = i
		chain_set = set()
		chain_set.add(k)
		chain = [k]
		while True:
			k = factorial_chain(k)
			if k in chain_set:
				chain.append(k)
				break
			chain_set.add(k)
			chain.append(k)
		if len(chain) - 1 == 60:
			count += 1
		if i % 1000 == 0:
			print(i)
	print(count)