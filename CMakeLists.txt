cmake_minimum_required(VERSION 3.10)

# Project name and C++ standard
project(CalculatorBenchmark VERSION 1.0.0)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Compiler-specific optimization flags
if(CMAKE_CXX_COMPILER_ID STREQUAL "GNU" OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
    # GCC or Clang
    set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} -O3 -march=native -finline-functions -ffast-math -funroll-loops -flto")
    set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -flto")
elseif(MSVC)
    # Microsoft Visual C++
    set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} /O2 /Ob2 /Oi /Ot /Oy /GL")
    set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} /LTCG")
endif()

# Add executable target
add_executable(calculator_benchmark
    main.cpp
    optimized_calculator.cpp
)

# Include directories
target_include_directories(calculator_benchmark PRIVATE ${CMAKE_CURRENT_SOURCE_DIR})

# Link libraries (if needed)
if(CMAKE_CXX_COMPILER_ID STREQUAL "GNU" OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
    target_link_libraries(calculator_benchmark m)  # Math library for GCC/Clang
endif()

# Enable link-time optimization for release builds
set_property(TARGET calculator_benchmark PROPERTY INTERPROCEDURAL_OPTIMIZATION_RELEASE ON)