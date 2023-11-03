with open("mml.py", "r") as matrixFile:
    exec(matrixFile.read())

# Row Reduction # 

    # to use row reduction, we will unify matrix A and array b into one matrix using np.hstack() function
    
    # it is important to remember that the shape of b matrix was (3,)
        # thus, to stack it with A matrix, we need to reshape b matrix into (3,1) matrix

print(f"Determinant A is: {det_A})