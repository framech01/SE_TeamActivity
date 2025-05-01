Matrix Multiplication Benchmark in Python
This repository provides a simple benchmark and performance comparison of matrix multiplication implementations in Python:
A pure Python triple-loop version (multiply)
A NumPy-optimized version (multiply_numpy)
It also integrates profiling tools to analyze and compare performance characteristics using:
cProfile
line_profiler

Features
Pure Python Implementation: Understand the computational cost of nested loops
NumPy Vectorized Approach: Leverage optimized libraries for speed
Profiling Ready: Integrated decorators and setup for line_profiler and cProfile


How to Run
1. Basic Benchmark (No Profiling)
python benchmark_profile.py
2. With cProfile (Function-level timing)
python -m cProfile -s cumtime benchmark_profile.py
3. With line_profiler (Line-by-line timing)
Install line_profiler:
pip install line_profiler
Then run:
kernprof -l -v benchmark_profile.py

Use Cases
Benchmarking performance bottlenecks in Python code
Teaching how algorithm complexity impacts runtime
Comparing low-level vs library-based implementations
Exploring profiling tools (cProfile, line_profiler) in software engineering education
