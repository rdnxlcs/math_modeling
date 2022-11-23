from math import sqrt, acos, degrees
a = [4, 3, 8]
b = [-2, 8, 7]
c = [-5, -6, 12]	

def vect_len(v):
	return sqrt(v[0]**2 + v[1]**2 + v[2] ** 2)

def vect_mult(v1, v2):
	return (v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2])
	
def angel(v1, v2):
	return degrees(acos(vect_mult(v1, v2)/(vect_len(v1)*vect_len(v2))))
	
print(angel(a, b))
print(angel(a, c))
print(angel(b, c))