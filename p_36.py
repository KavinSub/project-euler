def is_palindromic(s):
	for i in range(len(s)//2):
		if s[i] != s[len(s) - 1 - i]:
			return False
	return True

if __name__ == '__main__':
	total = 0
	for i in range(1, 1000000):
		if is_palindromic(str(i)) and is_palindromic(bin(i)[2:]):
			total += i
		if i % 10000 == 0:
			print(i)
	print(total)