# Project Euler Problem 102: Triangle Containment
# Author: Kavin Subramanyam

import time

def normalize(v, p):
	x = v[0][0]
	y = v[0][1]

	v[1][0] -= x
	v[1][1] -= y
	v[2][0] -= x
	v[2][1] -= y
	point = (p[0]-x, p[1]-y)

	return point

def in_triangle(v, p):
	x, y = normalize(v, p)
	scalar = v[1][0]*v[2][1] - v[2][0]*v[1][1]
	wa = (x*(v[1][1] - v[2][1]) + y*(v[2][0] - v[1][0]) + v[1][0]*v[2][1] - v[2][0]*v[1][1])/scalar
	wb = (x*v[2][1] - y*v[2][0])/scalar
	wc = (y*v[1][0] - x*v[1][1])/scalar
	return in_range(wa) and in_range(wb) and in_range(wc)

def in_range(w):
	return w > 0 and w < 1

if __name__ == '__main__':
	begin = time.time()
	count = 0
	point = [0, 0]
	with open('triangles.txt', 'r') as f:
		while True:
			line = f.readline().strip()
			if line == '':
				break
			c = [int(x) for x in line.split(',')]
			vertices = [[c[0], c[1]], [c[2], c[3]], [c[4], c[5]]]
			if in_triangle(vertices, point):
				count += 1
	end = time.time()
	print("Time taken:", end - begin)
	print("Solution:", count)