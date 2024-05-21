from scipy.sparse.linalg import eigs
import numpy as np

a = np.array([[1, 2, 3], [2, 1, 3], [3, 3, 6]], dtype=float)
b, c = np.linalg.eig(a)  # 为稠密矩阵求特征值和特征向量
d, e = eigs(a)  # 为稀疏矩阵求特征值和特征向量
print(f"eigenvalues: \n{d}")
print(f"eigenvectors: \n{e}")
