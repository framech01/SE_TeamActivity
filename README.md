**Matrix Multiplication Benchmark in Python**</br>
This repository provides a simple benchmark and performance comparison of matrix multiplication implementations in Python:</br>
A pure Python triple-loop version (multiply)</br>
A NumPy-optimized version (multiply_numpy)</br>
It also integrates profiling tools to analyze and compare performance characteristics using:</br>
cProfile</br>
line_profiler</br>

**Features**</br>
Pure Python Implementation: Understand the computational cost of nested loops</br>
NumPy Vectorized Approach: Leverage optimized libraries for speed</br>
Profiling Ready: Integrated decorators and setup for line_profiler and cProfile</br>

**How to Run**
1. Basic Benchmark (No Profiling)</br>
python benchmark_profile.py</br>
2. With cProfile (Function-level timing)</br>
python -m cProfile -s cumtime benchmark_profile.py</br>
3. With line_profiler (Line-by-line timing)</br>
Install line_profiler:
pip install line_profiler</br>
Then run:
kernprof -l -v benchmark_profile.py</br>

**Use Cases**</br>
Benchmarking performance bottlenecks in Python code</br>
Teaching how algorithm complexity impacts runtime</br>
Comparing low-level vs library-based implementations</br>
Exploring profiling tools (cProfile, line_profiler) in software engineering education</br>
