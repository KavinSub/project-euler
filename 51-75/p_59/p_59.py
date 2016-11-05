# Project Euler Problem 59: XOR Decryption
# Author: Kavin Subramanyam

def create_key(x, y, z):
	return x + 256 * y + (256 ** 2) * z

if __name__ == '__main__':
	text = []
	with open('cipher.txt', 'r') as f:
		text = [int(n) for n in f.read().strip().split(',')]
	print(len(text))