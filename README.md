# Calculator Benchmark Application

This application benchmarks the performance of optimized calculator functions against standard implementations.

## Build Instructions

### Method 1: Using CMake (Cross-Platform)

```bash
mkdir build
cd build
cmake ..
make
```

On Windows with Visual Studio:
```cmd
mkdir build
cd build
cmake .. -G "Visual Studio 16 2019"
cmake --build . --config Release
```

### Method 2: Direct Compilation

#### On Linux/macOS with GCC:
```bash
g++ -std=c++17 -O3 -march=native -finline-functions -ffast-math -funroll-loops -flto -o calculator_benchmark main.cpp optimized_calculator.cpp
```

#### On Linux/macOS with Clang:
```bash
clang++ -std=c++17 -O3 -march=native -finline-functions -ffast-math -funroll-loops -flto -o calculator_benchmark main.cpp optimized_calculator.cpp
```

#### On Windows with MinGW:
```cmd
g++ -std=c++17 -O3 -march=native -finline-functions -ffast-math -funroll-loops -flto -o calculator_benchmark.exe main.cpp optimized_calculator.cpp
```

#### On Windows with MSVC (Developer Command Prompt):
```cmd
cl /EHsc /O2 /std:c++17 /Fe:calculator_benchmark.exe main.cpp optimized_calculator.cpp
```

## Running the Benchmark

After building, run the executable:

```bash
./calculator_benchmark    # Linux/macOS
calculator_benchmark.exe  # Windows
```

The console window will remain open after displaying the benchmark results. Press Enter to exit.

## Features

- Benchmarks all basic arithmetic operations (add, subtract, multiply, divide)
- Tests power and square root operations
- Includes expression evaluation benchmarks
- Runs millions of iterations for accurate timing
- Displays performance metrics in a formatted table
- Shows percentage improvement of optimized vs standard implementations
- Includes warm-up runs to eliminate cache effects

## Files Included

- `main.cpp`: Main benchmark application with console pause functionality
- `optimized_calculator.hpp`: Optimized calculator header with inline functions
- `optimized_calculator.cpp`: Calculator implementation
- `CMakeLists.txt`: Cross-platform build configuration
- `COMPILATION_INSTRUCTIONS.md`: Additional compilation guidance
- `PERFORMANCE_METRICS.md`: Performance analysis report