import numpy as np

# matrix
A = np.array([[1, 1, 1],
              [800, 900, 1200],
              [100, 150, 200]])

# constants vector
b = np.array([300000, 2500, 45000])

# Solve the system
x = np.linalg.lstsq(A, b, rcond=None)[0]
print(x)
