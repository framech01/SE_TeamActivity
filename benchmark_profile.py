import random
import numpy as np
from multiply import multiply, multiply_numpy

def run_benchmark():
    size = 500 
    matrix1 = [[random.uniform(-1, 1) for _ in range(size)] for _ in range(size)]
    matrix2 = [[random.uniform(-1, 1) for _ in range(size)] for _ in range(size)]

    result1 = multiply(matrix1, matrix2)

    np1 = np.array(matrix1)
    np2 = np.array(matrix2)
    result2 = multiply_numpy(np1, np2)

if __name__ == "__main__":
    run_benchmark()
