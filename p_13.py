f = open("num.txt", 'r')

L = []
while True:
	line = f.readline();
	if line == "":
		break;
	L.append(int(line))

s = str(sum(L))
print(s[:10])