digits = set("123456789")

def check_num(n):
	s = ""
	i = 1
	while len(s) < 9:
		s += str(n * i)
		i += 1
	if set(s) == digits:
		return int(s)

if __name__ == '__main__':
	num = 0
	for i in range(1, 10000):
		t = check_num(i)
		if t is not None:
			num = t
	print(num)