import numpy as np
import math

def main():
    # n = int(input())
    n = 5
    eps = 1e-10
    
    def random_matrix(n):
        matr_L = np.diag(np.random.rand(n))
        matr_C = np.random.rand(n, n)
        return np.matmul(np.linalg.inv(matr_C), matr_L, matr_C)
    
    A = random_matrix(n)
    # print(A)
    eig_val, eig_vec = InversePowerMethod(A, eps=eps)
    print(eig_val, eig_vec)

def InversePowerMethod(matr_A: np.ndarray, eps : float = 1e-3):
    
    def get_sigma_step(z, y, eps):
        mu = [z[i] / y[i] for i in range(len(z)) if y[i] > eps]
        return sum(mu) / len(mu) if len(mu) > 0 else 0

    n = len(matr_A)
    y = np.random.rand(n) 
    
    z = y / np.linalg.norm(y)
    z_prev = z * 10
    
    sigma_prev = np.random.random_sample()
    sigma = (sigma_prev + eps) * 10
        
    while ((abs(np.linalg.norm(z_prev) - np.linalg.norm(z)) > eps) or (abs(sigma - sigma_prev) > eps)):
        y = np.matmul(z, np.linalg.inv(matr_A - sigma_prev * np.identity(n=n)))
        
        z_prev = z
        z = y / np.linalg.norm(y)
        
        sigma_prev = sigma
        sigma = sigma_prev + get_sigma_step(z_prev, y, eps)
        print(sigma, z)
        
    else:
        return sigma, z

main()
