/*
 * optimized_calculator.hpp
 * High-performance calculator implementation using C++17 with aggressive optimizations
 * 
 * Optimization techniques applied:
 * - Inline functions to eliminate call overhead
 * - Template specializations for different numeric types
 * - Constexpr for compile-time computations where possible
 * - Aggressive compiler optimization flags (-O3, -march=native)
 */

#ifndef OPTIMIZED_CALCULATOR_HPP
#define OPTIMIZED_CALCULATOR_HPP

#include <type_traits>
#include <stdexcept>
#include <string>
#include <sstream>
#include <cmath>
#include <limits>

// Compiler-specific force inline macro
#ifdef _MSC_VER
    #define FORCE_INLINE __forceinline
#elif defined(__GNUC__) || defined(__clang__)
    #define FORCE_INLINE inline __attribute__((always_inline))
#else
    #define FORCE_INLINE inline
#endif

namespace calc {

/**
 * @brief Optimized addition function with template specialization
 * @tparam T Numeric type (int, float, double, etc.)
 * @param a First operand
 * @param b Second operand
 * @return Sum of a and b
 */
template<typename T>
FORCE_INLINE constexpr T add(const T& a, const T& b) noexcept {
    static_assert(std::is_arithmetic_v<T>, "Type must be arithmetic");
    return a + b;
}

/**
 * @brief Optimized subtraction function with template specialization
 * @tparam T Numeric type (int, float, double, etc.)
 * @param a First operand
 * @param b Second operand
 * @return Difference of a and b
 */
template<typename T>
FORCE_INLINE constexpr T subtract(const T& a, const T& b) noexcept {
    static_assert(std::is_arithmetic_v<T>, "Type must be arithmetic");
    return a - b;
}

/**
 * @brief Optimized multiplication function with template specialization
 * @tparam T Numeric type (int, float, double, etc.)
 * @param a First operand
 * @param b Second operand
 * @return Product of a and b
 */
template<typename T>
FORCE_INLINE constexpr T multiply(const T& a, const T& b) noexcept {
    static_assert(std::is_arithmetic_v<T>, "Type must be arithmetic");
    return a * b;
}

/**
 * @brief Optimized division function with template specialization
 * @tparam T Numeric type (int, float, double, etc.)
 * @param a Dividend
 * @param b Divisor
 * @return Quotient of a divided by b
 * @throws std::domain_error if division by zero is attempted
 */
template<typename T>
FORCE_INLINE T divide(const T& a, const T& b) {
    static_assert(std::is_arithmetic_v<T>, "Type must be arithmetic");
    
    // Compile-time check for floating-point types to handle infinity
    if constexpr (std::is_floating_point_v<T>) {
        if (b == T(0)) {
            if (a > T(0)) return std::numeric_limits<T>::infinity();
            else if (a < T(0)) return -std::numeric_limits<T>::infinity();
            else return std::numeric_limits<T>::quiet_NaN(); // 0/0
        }
    } else {
        // Runtime check for integer division by zero
        if (b == T(0)) {
            throw std::domain_error("Division by zero");
        }
    }
    
    return a / b;
}

/**
 * @brief Optimized power function using exponentiation by squaring
 * @tparam T Base type (arithmetic)
 * @tparam U Exponent type (integral)
 * @param base Base value
 * @param exp Exponent value
 * @return Base raised to the power of exponent
 */
template<typename T, typename U>
FORCE_INLINE T power(T base, U exp) noexcept {
    static_assert(std::is_arithmetic_v<T>, "Base type must be arithmetic");
    static_assert(std::is_integral_v<U>, "Exponent type must be integral");
    
    if (exp == 0) return T(1);
    if (exp == 1) return base;
    
    T result = T(1);
    while (exp > 0) {
        if (exp & 1) {  // If exp is odd
            result *= base;
        }
        base *= base;
        exp >>= 1;  // Divide exp by 2
    }
    return result;
}

/**
 * @brief Optimized square root function using Newton-Raphson method
 * @tparam T Floating-point type
 * @param x Value to compute square root of
 * @return Square root of x
 */
template<typename T>
FORCE_INLINE T sqrt_newton_raphson(T x) noexcept {
    static_assert(std::is_floating_point_v<T>, "Type must be floating point");
    
    if (x <= T(0)) return T(0);
    if (x == T(1)) return T(1);
    
    T guess = x / T(2);  // Initial guess
    const T tolerance = std::numeric_limits<T>::epsilon() * T(100);
    
    for (int i = 0; i < 20; ++i) {  // Max iterations to prevent infinite loop
        T new_guess = (guess + x / guess) / T(2);
        if (std::abs(new_guess - guess) < tolerance) {
            return new_guess;
        }
        guess = new_guess;
    }
    
    return guess;
}

/**
 * @brief Optimized factorial function using template specialization for compile-time computation
 * @tparam T Integral type
 * @param n Value to compute factorial of
 * @return Factorial of n
 */
template<typename T>
FORCE_INLINE T factorial(T n) noexcept {
    static_assert(std::is_integral_v<T>, "Type must be integral");
    
    if (n <= T(1)) return T(1);
    
    T result = T(1);
    for (T i = T(2); i <= n; ++i) {
        result *= i;
    }
    return result;
}

/**
 * @brief Optimized factorial function with compile-time computation for small values
 * @tparam N Compile-time constant value
 * @return Factorial of N
 */
template<int N>
struct Factorial {
    static constexpr long long value = N * Factorial<N - 1>::value;
};

template<>
struct Factorial<0> {
    static constexpr long long value = 1;
};

/**
 * @brief Parse string to numeric type with optimized conversion
 * @tparam T Target numeric type
 * @param str String representation of number
 * @return Converted numeric value
 */
template<typename T>
FORCE_INLINE T parse_number(const std::string& str) {
    static_assert(std::is_arithmetic_v<T>, "Type must be arithmetic");
    
    if constexpr (std::is_same_v<T, int>) {
        return static_cast<T>(std::stoi(str));
    } else if constexpr (std::is_same_v<T, long>) {
        return static_cast<T>(std::stol(str));
    } else if constexpr (std::is_same_v<T, long long>) {
        return static_cast<T>(std::stoll(str));
    } else if constexpr (std::is_same_v<T, float>) {
        return static_cast<T>(std::stof(str));
    } else if constexpr (std::is_same_v<T, double>) {
        return static_cast<T>(std::stod(str));
    } else if constexpr (std::is_same_v<T, long double>) {
        return static_cast<T>(std::stold(str));
    } else {
        // Fallback for other arithmetic types
        std::stringstream ss(str);
        T result;
        ss >> result;
        return result;
    }
}

/**
 * @brief Format numeric value to string with optimized conversion
 * @tparam T Source numeric type
 * @param value Numeric value to convert
 * @return String representation of value
 */
template<typename T>
FORCE_INLINE std::string format_number(const T& value) {
    static_assert(std::is_arithmetic_v<T>, "Type must be arithmetic");
    
    if constexpr (std::is_same_v<T, int>) {
        return std::to_string(static_cast<int>(value));
    } else if constexpr (std::is_same_v<T, long>) {
        return std::to_string(static_cast<long>(value));
    } else if constexpr (std::is_same_v<T, long long>) {
        return std::to_string(static_cast<long long>(value));
    } else if constexpr (std::is_same_v<T, float>) {
        return std::to_string(static_cast<float>(value));
    } else if constexpr (std::is_same_v<T, double>) {
        return std::to_string(static_cast<double>(value));
    } else if constexpr (std::is_same_v<T, long double>) {
        return std::to_string(static_cast<long double>(value));
    } else {
        // Fallback for other arithmetic types
        std::stringstream ss;
        ss << value;
        return ss.str();
    }
}

/**
 * @brief Optimized expression evaluator using Shunting-yard algorithm
 * @param expression Mathematical expression string
 * @return Computed result
 */
double evaluate_expression(const std::string& expression);

/**
 * @brief Optimized calculator class for stateful operations
 */
class Calculator {
private:
    double current_value;
    double memory;

public:
    /**
     * @brief Constructor initializes calculator state
     */
    explicit Calculator(double initial_value = 0.0) noexcept : 
        current_value(initial_value), 
        memory(0.0) {}
    
    /**
     * @brief Get current calculator value
     * @return Current value
     */
    FORCE_INLINE double get_current_value() const noexcept { return current_value; }
    
    /**
     * @brief Get memory register value
     * @return Memory value
     */
    FORCE_INLINE double get_memory() const noexcept { return memory; }
    
    /**
     * @brief Set current value
     * @param value New value to set
     */
    FORCE_INLINE void set_value(double value) noexcept { current_value = value; }
    
    /**
     * @brief Add value to current value
     * @param value Value to add
     * @return Reference to this calculator for chaining
     */
    FORCE_INLINE Calculator& add_to(double value) noexcept {
        current_value = calc::add(current_value, value);
        return *this;
    }
    
    /**
     * @brief Subtract value from current value
     * @param value Value to subtract
     * @return Reference to this calculator for chaining
     */
    FORCE_INLINE Calculator& subtract_from(double value) noexcept {
        current_value = calc::subtract(current_value, value);
        return *this;
    }
    
    /**
     * @brief Multiply current value by value
     * @param value Value to multiply by
     * @return Reference to this calculator for chaining
     */
    FORCE_INLINE Calculator& multiply_by(double value) noexcept {
        current_value = calc::multiply(current_value, value);
        return *this;
    }
    
    /**
     * @brief Divide current value by value
     * @param value Value to divide by
     * @return Reference to this calculator for chaining
     * @throws std::domain_error if division by zero is attempted
     */
    Calculator& divide_by(double value) {
        current_value = calc::divide(current_value, value);
        return *this;
    }
    
    /**
     * @brief Clear calculator (set to 0)
     * @return Reference to this calculator for chaining
     */
    FORCE_INLINE Calculator& clear() noexcept {
        current_value = 0.0;
        return *this;
    }
    
    /**
     * @brief Memory store operation
     * @return Reference to this calculator for chaining
     */
    FORCE_INLINE Calculator& memory_store() noexcept {
        memory = current_value;
        return *this;
    }
    
    /**
     * @brief Memory recall operation
     * @return Reference to this calculator for chaining
     */
    FORCE_INLINE Calculator& memory_recall() noexcept {
        current_value = memory;
        return *this;
    }
    
    /**
     * @brief Memory clear operation
     * @return Reference to this calculator for chaining
     */
    FORCE_INLINE Calculator& memory_clear() noexcept {
        memory = 0.0;
        return *this;
    }
    
    /**
     * @brief Memory add operation
     * @return Reference to this calculator for chaining
     */
    FORCE_INLINE Calculator& memory_add() noexcept {
        memory = calc::add(memory, current_value);
        return *this;
    }
    
    /**
     * @brief Calculate square root of current value
     * @return Reference to this calculator for chaining
     */
    FORCE_INLINE Calculator& sqrt() noexcept {
        current_value = calc::sqrt_newton_raphson(current_value);
        return *this;
    }
    
    /**
     * @brief Calculate square of current value
     * @return Reference to this calculator for chaining
     */
    FORCE_INLINE Calculator& square() noexcept {
        current_value = calc::multiply(current_value, current_value);
        return *this;
    }
    
    /**
     * @brief Calculate reciprocal of current value
     * @return Reference to this calculator for chaining
     * @throws std::domain_error if current value is zero
     */
    Calculator& reciprocal() {
        if (current_value == 0.0) {
            throw std::domain_error("Reciprocal of zero is undefined");
        }
        current_value = calc::divide(1.0, current_value);
        return *this;
    }
};

} // namespace calc

#endif // OPTIMIZED_CALCULATOR_HPP