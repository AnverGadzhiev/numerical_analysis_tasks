import matplotlib.pyplot as plt
import numpy as np
import math
from numpy.polynomial.polynomial import Polynomial
from scipy.interpolate import lagrange
 
 
def f(x):
	return (x**2 + 1 + math.acos(x)) * abs(x)
 
 
def getPoints(n, a, b):
	res = []
	for i in range(0, n + 1):
		res.append(((b - a) * math.cos(
		 (2 * i + 1) * math.pi / (2 * n + 2)) + b + a) / 2)
	return np.array(res)
 
 
xR = np.arange(-1, 1, 0.005)
 
plt.plot(xR, np.array([f(xi) for xi in xR]), label='Функция', c="C0")
 
x = np.arange(-1, 1 + 0.001, 0.25)
y = np.array([f(xi) for xi in x])
poly = lagrange(x, y)
plt.scatter(x, y, label='Свои точки интерполяции', c="C1")
plt.plot(xR,
         Polynomial(poly.coef[::-1])(xR),
         label='Интерполяция по своим точкам',
         c="C1")
 
x2 = getPoints(x.size, -1, 1)
y2 = np.array([f(xi) for xi in x2])
poly2 = lagrange(x2, y2)
plt.scatter(x2, y2, label='Точки формулы', c="C2")
plt.plot(xR,
         Polynomial(poly2.coef[::-1])(xR),
         label='Интерполяция по формуле',
         c="C2")
 
plt.legend()
plt.show()