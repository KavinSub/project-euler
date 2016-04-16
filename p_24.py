from math import factorial

# Gets permutation number n
def get_permutation(n):
	s = ""
	L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	for i in range(10):
		d = n // factorial(9 - i)
		n = n % factorial(9 - i)
		s += str(L[d])
		L.pop(d)
	return s

if __name__ =='__main__':
	print(get_permutation(999999))