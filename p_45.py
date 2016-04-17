# Generates first n triangular numbers
def triangle(n):
	return set([(i * (i + 1))//2 for i in range(1, n + 1)])

# Generates first n pentagonal numbers
def pentagon(n):
	return set([(i * (3*i - 1))//2 for i in range(1, n + 1)])

# Generates first hexagonal numbers
def hexagon(n):
	return set([i * (2*i - 1) for i in range(1, n + 1)])

if __name__ == '__main__':
	triangle_numbers = triangle(100000)
	pentagon_numbers = pentagon(100000)
	hexagon_numbers = hexagon(100000)

	for num in triangle_numbers:
		if num in pentagon_numbers and num in hexagon_numbers:
			print(num)