s = ""
i = 1
while len(s) < 1000000:
	s += str(i)
	i += 1
product = 1
for i in range(7):
	product *= int(s[(10 ** i) - 1])
print(product)