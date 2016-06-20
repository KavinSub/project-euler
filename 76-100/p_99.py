from math import log

with open('p99_base_exp.txt', 'r') as f:
	linenum = 0
	max_val = 0
	max_line = 1
	while True:
		line = f.readline()
		if line == '':
			break
		linenum += 1
		base, exponent = (int(token) for token in line.split(','))
		value = exponent * log(base)
		if value > max_val:
			max_val = value
			max_line = linenum
	print(max_line)