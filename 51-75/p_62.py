# Project Euler Problem 62: Cubic Permutations
# Author: Kavin Subramanyam

def number_digits(n):
	digits = [0] * 10
	while n > 0:
		digits[n % 10] += 1
		n = n//10
	return "".join([str(d) for d in digits])

if __name__ == '__main__':
	cube_map = {}
	i = 1
	complete = False
	while not complete:
		cube = i ** 3
		digits = number_digits(cube)
		if digits not in cube_map.keys():
			cube_map[digits] = [i, 1]
		else:
			cube_map[digits][1] += 1
			if cube_map[digits][1] == 5:
				print("Solution:", cube_map[digits][0]**3)
				complete = True
		i += 1