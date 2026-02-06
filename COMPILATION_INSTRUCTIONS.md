# Compilation Instructions for Optimized Calculator

## Prerequisites
- GCC 7+ or Clang 5+ (supports C++17)
- Make sure C++17 capable compiler is installed

## Compilation Commands

### For GCC:
```bash
g++ -std=c++17 -O3 -march=native -finline-functions -ffast-math -funroll-loops -flto -o benchmark_gcc benchmark.cpp optimized_calculator.cpp
```

### For Clang:
```bash
clang++ -std=c++17 -O3 -march=native -finline-functions -ffast-math -funroll-loops -flto -o benchmark_clang benchmark.cpp optimized_calculator.cpp
```

## Explanation of Optimization Flags

- `-std=c++17`: Use C++17 standard for modern features
- `-O3`: Maximum optimization level
- `-march=native`: Optimize for the host processor (includes all available instruction sets)
- `-finline-functions`: Enable function inlining (reduces call overhead)
- `-ffast-math`: Enable aggressive math optimizations (may affect precision slightly)
- `-funroll-loops`: Unroll loops to reduce iteration overhead
- `-flto`: Enable Link Time Optimization for whole-program optimization

## Alternative Compilation with Debug Info
If you need debugging capabilities alongside optimizations:
```bash
g++ -std=c++17 -O2 -g -march=native -finline-functions -o benchmark_debug benchmark.cpp optimized_calculator.cpp
```

## Running the Benchmark
After compilation:
```bash
./benchmark_gcc          # On Linux/Mac
# or
./benchmark_clang        # On Linux/Mac
# or
benchmark_gcc.exe        # On Windows
# or  
benchmark_clang.exe      # On Windows
```

## Building with Makefile (optional)
Create a Makefile with the following content:

```makefile
CXX = g++
CXXFLAGS = -std=c++17 -O3 -march=native -finline-functions -ffast-math -funroll-loops -flto
TARGET = benchmark
SOURCES = benchmark.cpp optimized_calculator.cpp

$(TARGET): $(SOURCES)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(SOURCES)

clean:
	rm -f $(TARGET)

.PHONY: clean
```

Then run:
```bash
make
./benchmark
```

## Expected Performance Improvements
With these optimizations, you should see:
- 10-30% improvement in basic arithmetic operations due to inlining
- Significant improvements in complex operations like power and square root calculations
- Better instruction-level parallelism due to loop unrolling
- Reduced memory access overhead through better register allocation