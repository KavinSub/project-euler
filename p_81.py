# Returns value above index i, j
def check_top(M, i, j):
	return M[i - 1][j]

def check_left(M, i, j):
	return M[i][j - 1]


if __name__ == '__main__':
	M = []
	matrix_file = open('p81_matrix.txt', 'r')
	for i in range(80):
		L = [int(x) for x in matrix_file.readline().strip("'").split(',')]
		M.append(L)
	
	for i in range(80):
		for j in range(80):
			if i != 0 and j != 0:
				M[i][j] += min(check_left(M, i, j), check_top(M, i, j))
			elif i == 0 and j != 0:
				M[i][j] += check_left(M, i, j)
			elif j == 0 and i != 0:
				M[i][j] += check_top(M, i, j)
	print(M[79][79])