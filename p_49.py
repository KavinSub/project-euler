from math import *
from itertools import permutations

def sieve(n):
	L = [True] * (n + 1)
	L[0] = False
	L[1] = False
	prime = 2
	k = prime
	while prime < int(floor(sqrt(n))) + 1:
		while k <= n - prime:
			k += prime
			L[k] = False
		prime += 1
		while L[prime] == False:
			prime += 1
		k = prime

	L = [i for i in range(len(L)) if L[i] == True]
	return L

def check_sequence_exists(L, d):
	result = []
	P_set = set(L)
	P_list = sorted(list(P_set))
	i = 0
	while i < len(P_list):
		v = P_list[i]
		if v + d in P_set and v + 2*d in P_set:
			r = [v, v + d, v + 2 * d]
			result.append(r)
		i += 1
	return result


def check_permutation_exists(r):
	return set(str(r[0])) == set(str(r[1])) and set(str(r[1])) == set(str(r[2]))

if __name__ == '__main__':
	primes = sieve(10000)
	primes = [prime for prime in primes if prime >= 1000 and prime < 10000]

	diff = {}
	prime_pairs = permutations(primes, 2)
	for pair in prime_pairs:
		d = abs(pair[1] - pair[0])
		if d in diff:
			diff[d].append(pair[0])
			diff[d].append(pair[1])
		else:
			diff[d] = [pair[0]]
			diff[d].append(pair[1])

	for d in diff.keys():
		results = check_sequence_exists(diff[d], d)
		if results is not []:
			for result in results:
				if check_permutation_exists(result):
					print(result)
					S = ''.join([str(r) for r in result])
					print(S)
					# break
		# print(d)
