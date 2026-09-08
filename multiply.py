import numpy as np


try:
    from line_profiler import profile
except ImportError:
    def profile(func):  
        return func

@profile
def multiply(matrix1, matrix2):
    if not matrix1 or not matrix2 or not matrix1[0] or not matrix2[0]:
        raise ValueError("Matrices must be non-empty")
    if any(len(row) != len(matrix1[0]) for row in matrix1) or any(len(row) != len(matrix2[0]) for row in matrix2):
        raise ValueError("Matrices must be rectangular")
    rows1 = len(matrix1)
    columns1 = len(matrix1[0])
    row2 = len(matrix2)
    columns2 = len(matrix2[0])

    if columns1 != row2:
        raise ValueError(f"Incompatible dimensions: {rows1}x{columns1} and {row2}x{columns2}")

    result = [[0 for _ in range(columns2)] for _ in range(rows1)]

    transposed = list(zip(*matrix2))
    for i in range(rows1):
        for j in range(columns2):
            result[i][j] = sum(a * b for a, b in zip(matrix1[i], transposed[j]))

    return result

@profile
def multiply_numpy(matrix1, matrix2):
    return np.matmul(matrix1, matrix2)
