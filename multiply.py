import numpy as np


try:
    from line_profiler import profile
except ImportError:
    def profile(func):  
        return func

@profile
def multiply(matrix1, matrix2):
    rows1 = len(matrix1)
    columns1 = len(matrix1[0])
    row2 = len(matrix2)
    columns2 = len(matrix2[0])

    if columns1 != row2:
        return None

    result = [[0 for _ in range(columns2)] for _ in range(rows1)]

    for i in range(rows1):
        for j in range(columns2):
            sum_cell = 0
            for k in range(columns1):
                sum_cell += matrix1[i][k] * matrix2[k][j]
            result[i][j] = sum_cell

    return result

@profile
def multiply_numpy(matrix1, matrix2):
    return np.matmul(matrix1, matrix2)
