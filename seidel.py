import numpy as np

eps = 1e-6
##Входные данные
N = 3
myA = [[N + 2,   1,     1  ], 
	  [1,       N+4,    1  ],
	  [1,        1,    N+6]]
myB = [N+4,
	  N +6,
	  N+8]


def seidel(A, b, eps):
    n = len(A)
    x = np.zeros(n)  # zero vector

    converge = False
    while not converge:
        x_new = np.copy(x)
        for i in range(n):
            s1 = sum(A[i][j] * x_new[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - s1 - s2) / A[i][i]

        converge = np.sqrt(sum((x_new[i] - x[i]) ** 2 for i in range(n))) <= eps
        x = x_new

    return x

def printSolution(myA, myB, eps):
    print("\n Решение,полученное методом Зейделя")
    sd_an = seidel(myA, myB, eps)
    for i in range(len(sd_an)):
        print(f"X{i+1} =    {sd_an[i]}")

if __name__ == '__main__':
    printSolution(myA, myB, eps)