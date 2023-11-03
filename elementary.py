import mml
import numpy as np
import rowReduction as rr

# elementary operations do not change the solution set of a Linear System #
print("\n"*5)
def MultiplyRow(M, row_num, row_num_multiple):
    
    M_new = M.copy() # copy is used to avoid changing the original matrix
    M_new[row_num] = M_new[row_num] * row_num_multiple
    return M_new
Asys = rr.Asys

print("original matrix:")
print(Asys)

print() 

print(MultiplyRow(Asys,(),-1)) # multiply all row elements by -1
