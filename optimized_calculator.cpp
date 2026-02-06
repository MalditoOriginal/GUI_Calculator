/*
 * optimized_calculator.cpp
 * Implementation of non-template functions for the optimized calculator
 * 
 * Contains the expression evaluator implementation using Shunting-yard algorithm
 */

#include "optimized_calculator.hpp"
#include <stack>
#include <queue>
#include <cctype>
#include <stdexcept>
#include <string>
#include <vector>

namespace calc {

/**
 * @brief Helper function to determine operator precedence
 * @param op Operator character
 * @return Precedence level (higher number means higher precedence)
 */
static int get_precedence(char op) {
    switch(op) {
        case '+':
        case '-':
            return 1;
        case '*':
        case '/':
            return 2;
        case '^':
            return 3;
        default:
            return 0;
    }
}

/**
 * @brief Helper function to check if character is an operator
 * @param c Character to check
 * @return True if character is an operator, false otherwise
 */
static bool is_operator(char c) {
    return c == '+' || c == '-' || c == '*' || c == '/' || c == '^';
}

/**
 * @brief Helper function to apply an operator to two operands
 * @param op Operator to apply
 * @param b Second operand
 * @param a First operand
 * @return Result of applying operator to operands
 */
static double apply_operator(char op, double b, double a) {
    switch(op) {
        case '+': return calc::add(a, b);
        case '-': return calc::subtract(a, b);
        case '*': return calc::multiply(a, b);
        case '/': return calc::divide(a, b);
        case '^': return calc::power(a, static_cast<int>(b));
        default: throw std::runtime_error("Invalid operator");
    }
}

/**
 * @brief Optimized expression evaluator using Shunting-yard algorithm
 * @param expression Mathematical expression string
 * @return Computed result
 */
double evaluate_expression(const std::string& expression) {
    if (expression.empty()) return 0.0;
    
    std::stack<char> operators;
    std::queue<double> output;
    
    for (size_t i = 0; i < expression.length(); ) {
        char c = expression[i];
        
        // Skip whitespace
        if (std::isspace(c)) {
            i++;
            continue;
        }
        
        // Handle numbers (including decimals)
        if (std::isdigit(c) || c == '.') {
            std::string num_str;
            while (i < expression.length() && 
                   (std::isdigit(expression[i]) || expression[i] == '.')) {
                num_str += expression[i];
                i++;
            }
            output.push(parse_number<double>(num_str));
            continue;
        }
        
        // Handle negative numbers
        if (c == '-' && (i == 0 || expression[i-1] == '(' || is_operator(expression[i-1]))) {
            // This is a unary minus, treat as -1 * (next number)
            i++; // Move past the minus
            if (i < expression.length() && (std::isdigit(expression[i]) || expression[i] == '.')) {
                std::string num_str = "-";
                while (i < expression.length() && 
                       (std::isdigit(expression[i]) || expression[i] == '.')) {
                    num_str += expression[i];
                    i++;
                }
                output.push(parse_number<double>(num_str));
                continue;
            } else {
                throw std::runtime_error("Invalid expression: unary minus not followed by number");
            }
        }
        
        // Handle operators
        if (is_operator(c)) {
            while (!operators.empty() && 
                   operators.top() != '(' &&
                   get_precedence(operators.top()) >= get_precedence(c)) {
                double b = output.front(); output.pop();
                double a = output.front(); output.pop();
                char op = operators.top(); operators.pop();
                output.push(apply_operator(op, b, a));
            }
            operators.push(c);
            i++;
            continue;
        }
        
        // Handle left parenthesis
        if (c == '(') {
            operators.push(c);
            i++;
            continue;
        }
        
        // Handle right parenthesis
        if (c == ')') {
            while (!operators.empty() && operators.top() != '(') {
                double b = output.front(); output.pop();
                double a = output.front(); output.pop();
                char op = operators.top(); operators.pop();
                output.push(apply_operator(op, b, a));
            }
            if (!operators.empty()) {
                operators.pop(); // Remove the '('
            } else {
                throw std::runtime_error("Mismatched parentheses");
            }
            i++;
            continue;
        }
        
        // Invalid character
        throw std::runtime_error(std::string("Invalid character in expression: ") + c);
    }
    
    // Process remaining operators
    while (!operators.empty()) {
        if (operators.top() == '(' || operators.top() == ')') {
            throw std::runtime_error("Mismatched parentheses");
        }
        double b = output.front(); output.pop();
        double a = output.front(); output.pop();
        char op = operators.top(); operators.pop();
        output.push(apply_operator(op, b, a));
    }
    
    if (output.empty()) {
        throw std::runtime_error("Empty expression");
    }
    
    return output.front();
}

} // namespace calc