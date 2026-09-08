import random
import numpy as np
import argparse
from time import perf_counter
from multiply import multiply, multiply_numpy

def run_benchmark(size=200, seed=42):
    rng = random.Random(seed)
    matrix1 = [[rng.uniform(-1, 1) for _ in range(size)] for _ in range(size)]
    matrix2 = [[rng.uniform(-1, 1) for _ in range(size)] for _ in range(size)]

    started = perf_counter()
    result1 = multiply(matrix1, matrix2)
    python_seconds = perf_counter() - started

    np1 = np.asarray(matrix1)
    np2 = np.asarray(matrix2)
    started = perf_counter()
    result2 = multiply_numpy(np1, np2)
    numpy_seconds = perf_counter() - started
    if not np.allclose(result1, result2):
        raise AssertionError("Python and NumPy results do not match")
    print(f"Matrix size: {size}x{size}")
    print(f"Pure Python: {python_seconds:.6f}s")
    print(f"NumPy:       {numpy_seconds:.6f}s")
    print(f"Speedup:     {python_seconds / max(numpy_seconds, 1e-12):.2f}x")
    return python_seconds, numpy_seconds

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pure Python vs NumPy matrix multiplication benchmark")
    parser.add_argument("--size", type=int, default=200)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()
    if args.size <= 0:
        parser.error("--size must be positive")
    run_benchmark(args.size, args.seed)
