

import numpy as np


# Matrix Array # 

A = np.array([
    [4,2,1],
    [4,0,0],
    [-1,-5,1]
], dtype=np.dtype(float))

b = np.array([3,5,1], dtype=np.dtype(float))
"""
print("Matrix A:", "\n", f"{A}")
print("Vector b:", "\n", f"{b}")
print()

print("shape of A is: ", np.shape(A))
print("Shape of b is: ", np.shape(b))
"""

# calculating the determinant of A and finding out if it is singular or non-singular
det_A = np.linalg.det(A)
"""
if det_A == 0:
    print(f"Matrix A is singular {det_A:.2f}")
else:
    print(f"Matrix A is non-singular {det_A:.2f}")

print()"""

# Row Reduction # 

    # to use row reduction, we will unify matrix A and array b into one matrix using np.hstack() function
    
    # it is important to remember that the shape of b matrix was (3,)
        # thus, to stack it with A matrix, we need to reshape b matrix into (3,1) matrix

