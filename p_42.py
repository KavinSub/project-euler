# Generates a set of the first n triangle numbers
def generate_triangle(n):
	triangle = set()
	i = 1
	T = 0
	while i <= n:
		T += i
		i += 1
		triangle.add(T)
	return triangle

def word_value(s):
	return sum([ord(c) - 64 for c in s])

if __name__ == '__main__':

	triangular_numbers = generate_triangle(200)

	word_file = open('p42_words.txt', 'r')
	words = word_file.readline().replace('"', '').strip().split(',')

	count = 0
	for word in words:
		if word_value(word) in triangular_numbers:
			count += 1
	print(count)