from itertools import permutations

# Generates the first n pentagon numbers
def pentagon_numbers(n):
	return [(i * (3 * i - 1))//2 for i in range(1, n + 1)]

if __name__ == '__main__':
	pentagon = pentagon_numbers(3000)
	pentagon_set = set(pentagon)
	pairs = permutations(pentagon, 2)

	D = float('inf')
	i = 0
	for pair in pairs:
		s = pair[0] + pair[1]
		d = max(pair[0], pair[1]) - min(pair[0], pair[1])
		if s in pentagon_set and d in pentagon_set:
			print(d)
			D = min(D, d)
		if i % 100000 == 0:
			print(i)
		i += 1
	print(D)