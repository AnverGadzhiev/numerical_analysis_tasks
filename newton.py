from math import sin, cos, sqrt

def f(x: float) -> float:
	return  sqrt(x) - cos(x)

def f_deriv(x: float) -> float:
	return 1 / (2 * sqrt(x)) + sin(x) 

def newton(x0: float, eps: float=1e-7, kmax: int=1e3) -> float:
	x, x_prev, i = x0, x0 + 2 * eps, 0
	while ((abs(x - x_prev) >= eps) and (i < kmax)): 
		x, x_prev, i = x - f(x) / f_deriv(x), x, i + 1
		print(i, x, abs(x - x_prev))
        
	return x
    
    
x0 = 1
print(newton(x0))
