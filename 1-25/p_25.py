from math import *
# Generates fibonacci number n
def fibonacci(n):
	return floor(1/sqrt(5)*(((1 + sqrt(5))/2)**n - ((1 - sqrt(5))/2)**n))

if __name__ == '__main__':
	a = 1
	b = 1
	i = 2
	while True:
		c = a + b
		i += 1
		if(len(str(c))) % 100 == 0:
			print(i)
			if(len(str(c))) == 1000:
				break
		temp = b
		b = c
		a = temp
