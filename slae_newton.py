from math import sin, cos, sqrt

eps = 1e-3
x_start, y_start = 3.25, 1.25

def norm(vector):
	return sqrt(sum([x*x for x in vector]))

def getStep(x, y):
	jacobi_determinant = sin(1-x)*sin(y) - 1
	f1 = cos(x - 1) + y - 0.5
	f2 = x - cos(y) - 3 
	return (
		-(sin(y)*f1 - f2) / jacobi_determinant,
		-(-f1 + sin(1-x)*f2) / jacobi_determinant
	)

def approximation(eps=eps):
	step = 1
	x, y = x_start, y_start
	x_prev, y_prev = x * 10, y * 10     
	while(norm([x-x_prev, y-y_prev]) >= eps):
		g_n, h_n = getStep(x, y)
		x_prev, y_prev = x, y
		x, y = x + g_n, y + g_n
		print("{} {:10.8f} {:10.8f} {:10.8f}".format(step, x, y, norm([x-x_prev, y-y_prev])))
		step+= 1
  
if __name__ == '__main__':
    approximation()
