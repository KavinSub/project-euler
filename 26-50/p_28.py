size = 1001
count = 1
current = 1
for l in range(1, size//2 + 1):
	for i in range(4):
		current = (2 * l) + current
		count += current
print(count)