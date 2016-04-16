def score(s):
	return sum([ord(c) - 64 for c in s])

names = open('names.txt', 'r')
L = names.readline().split(',')
L = [name.strip('"') for name in L]
L.sort()
print(sum([score(L[i]) * (i + 1) for i in range(len(L))]))