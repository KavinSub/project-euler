def is_palindrome(n):
	s = str(n)
	for i in range(len(s)//2):
		if s[i] != s[len(s) - 1 - i]:
			return False
	return True

def reverse_add(n):
	s = str(n)
	num = int(s[::-1])
	return n + num

def is_lychrel(n):
	k = n
	for i in range(50):
		k = reverse_add(k)
		if is_palindrome(k):
			return False
	return True

if __name__ == '__main__':
	lychrel = 0
	for i in range(10, 10000):
		if is_lychrel(i):
			print(i)
			lychrel += 1
	print(lychrel)