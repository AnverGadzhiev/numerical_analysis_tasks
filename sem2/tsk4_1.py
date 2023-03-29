import numpy as np

e = float(input())

def normalize(x):
    fac = abs(x).max()
    x_n = x / x.max()
    return fac, x_n

x = np.array([1, 1])
a = np.array([[0, 2], [2, 3]])

prev_lam = 10**10
lam = 0

while (abs(prev_lam-lam) >= e) :
    prev_lam = lam
    
x = np.dot(a, x)
lam, x = normalize(x)

print('Eigenvalue:', lam)
print('Eigenvector:', x)