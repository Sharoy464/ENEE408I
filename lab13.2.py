
## Part One : Go through the documentation and create a numpy array with the elements [1,2,3,4]##

import numpy as np

print("\n First Part: \n")

arr = np.array([1, 2, 3, 4])

print(arr)

print("\n Second Part: \n")

## Part Two : Use np.ones, np.zeros to create an array of 1’s with dimension 3x4 and an array of 0’s with 
# dimension 4x3##

array_ones = np.ones((3, 4))
print("Array of 1's with dimension (3x4):\n", array_ones)

print("-" * 20)

array_zeros = np.zeros((4, 3))
print("Array of 0's with dimension (4x3):\n", array_zeros)

print("\n Third Part: \n")

## Part Three: Create a 2x3 matrix A and a 3x4 matrix B and perform a matrix multiplication using numpy.##

A = np.array([[1, 2, 3],
              [4, 5, 6]])

B = np.array([[1, 1, 1, 1],
              [1, 1, 1, 1],
              [1, 1, 1, 1]])

result = np.matmul(A, B) 

print("Matrix A (2x3):\n", A)
print("\nMatrix B (3x4):\n", B)
print("\nResult (2x4):\n", result)


## Part Four: Find the eigenvalues and eigenvectors of the matrix given below? [3 1 | 1 2]##

print ("\n Fourth Part: \n")



A = np.array([[3, 1], [1, 2]])

w, v = np.linalg.eig(A)

print(A)
print("Eigenvalues:", w)
print("Eigenvectors:\n", v)
