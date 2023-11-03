import mml 
import numpy as np


# Row Reduction # 

    # to use row reduction, we will unify matrix A and array b into one matrix using np.hstack() function
    
    # it is important to remember that the shape of b matrix was (3,)
        # thus, to stack it with A matrix, we need to reshape b matrix into (3,1) matrix

print("Matrix A:", "\n", f"{mml.A}")
print("Vector b:", "\n", f"{mml.b}")
print("-------------------------    +")

# use reshape to change the shape of b matrix==>

nb = mml.b
nA = mml.A
rb = np.reshape(nb, (3,1))

# now lets stack A and b matrices together using np.hstack() function==>

Asys = np.hstack((nA, rb))

print("Augmenting Matrix [A|b]:", "\n", Asys)

