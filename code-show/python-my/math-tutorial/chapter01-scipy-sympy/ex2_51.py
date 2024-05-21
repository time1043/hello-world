import numpy as np
import sympy as sp

# a = sp.Matrix([[0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0]])
a = np.eye(4)
a = np.rot90(a)
a = sp.Matrix(a)
print(f"eigenvalues of a: \n{a.eigenvals()}\n")
print(f"eigenvectors of a: \n{a.eigenvects()}\n")
