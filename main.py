import numpy as np

# Define the coefficients matrix A
A = np.array([[1, 1, 1],
              [800, 900, 1200],
              [100, 150, 200]])

# Define the constants vector b
b = np.array([300000, 2500, 45000])

# Solve the system using least squares
result = np.linalg.lstsq(A, b, rcond=None)

# Extract the solution vector x
x = result[0]

# Print the results
print("Solution vector x:", x)
print("Residuals:", result[1])
print("Rank of matrix A:", result[2])
print("Singular values of A:", result[3])
