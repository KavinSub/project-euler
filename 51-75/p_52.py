def check_num(n):
	L = [set(str(n * i)) for i in range(1, 7)]
	for i in range(len(L) - 1):
		if L[i] != L[i + 1]:
			return False
	return True

if __name__ == '__main__':
	i = 1
	found = False
	while not found:
		for j in range(10 ** i, 2 * (10 ** i) + 1):
			if check_num(j):
				print(j)
				found = True
				break
		i += 1
		print(i)