power = 5
power_dict = {}
def power_num(n):
	s = str(n)
	a = 0
	for c in s:
		if c not in power_dict:
			power_dict[c] = int(c) ** power
		a += power_dict[c]
	return a == n

count = 0
for i in range(1, 1000000):
	if i % 1000000 == 0:
		print(i)
	if power_num(i):
		count += i
print(count - 1)