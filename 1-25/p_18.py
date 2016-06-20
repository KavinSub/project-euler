pyramid = open('path.txt', 'r')

P = []
while True:
	line = pyramid.readline().strip()
	if line == "":
		break
	P.append([int(num) for num in line.split(' ')])

for l in range(1, len(P)):
	cur_level = P[l]
	pre_level = P[l - 1]

	for i in range(len(cur_level)):
		top = 0
		left = 0
		if i < len(cur_level) - 1:
			top = cur_level[i] + pre_level[i]
		if i > 0:
			left = cur_level[i] + pre_level[i - 1]
		P[l][i] = max(top, left)

print(max(P[len(P) - 1]))