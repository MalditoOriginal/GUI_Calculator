"""
Calculator Model - Contains the core calculation logic
This class handles all mathematical operations and number parsing
"""

import re


class CalculatorModel:
    """
    Model component of the MVVM pattern.
    Responsible for performing calculations and handling mathematical operations.
    """
    
    def __init__(self):
        """Initialize the calculator model"""
        pass
    
    def evaluate_expression(self, expression):
        """
        Evaluates a mathematical expression string and returns the result.
        
        Args:
            expression (str): Mathematical expression to evaluate
            
        Returns:
            float: Result of the calculation
            
        Raises:
            ValueError: If the expression is invalid
            ZeroDivisionError: If division by zero occurs
        """
        if not expression:
            return 0
        
        # Remove any whitespace
        expression = expression.replace(' ', '')
        
        # Validate the expression contains only valid characters
        if not self._is_valid_expression(expression):
            raise ValueError("Invalid expression")
        
        # Check for division by zero
        if self._has_division_by_zero(expression):
            raise ZeroDivisionError("Division by zero")
        
        try:
            # Evaluate the expression using Python's eval function
            # Note: In a production environment, a safer parser would be recommended
            result = eval(expression)
            
            # Check if result is a valid number
            if isinstance(result, (int, float)):
                return result
            else:
                raise ValueError("Invalid result")
        except (SyntaxError, NameError, TypeError):
            raise ValueError("Invalid expression")
        except ZeroDivisionError:
            raise ZeroDivisionError("Division by zero")
    
    def _is_valid_expression(self, expression):
        """
        Validates that the expression contains only valid mathematical characters.
        
        Args:
            expression (str): Expression to validate
            
        Returns:
            bool: True if valid, False otherwise
        """
        # Regular expression to match valid mathematical expressions
        # Allows digits, decimal points, operators (+, -, *, /), and parentheses
        pattern = r'^[0-9+\-*/.() ]+$'
        return bool(re.match(pattern, expression))
    
    def _has_division_by_zero(self, expression):
        """
        Checks if the expression contains division by zero.
        
        Args:
            expression (str): Expression to check
            
        Returns:
            bool: True if division by zero detected, False otherwise
        """
        # Look for division by zero patterns
        # This is a simplified check - in a real application, a more robust parser would be needed
        # Check for /0 followed by an operator or end of string
        div_by_zero_pattern = r'/\s*0(?=[+\-*/\)])|/\s*0$'
        return bool(re.search(div_by_zero_pattern, expression))
    
    def add(self, a, b):
        """
        Adds two numbers.
        
        Args:
            a (float): First number
            b (float): Second number
            
        Returns:
            float: Sum of a and b
        """
        return a + b
    
    def subtract(self, a, b):
        """
        Subtracts second number from first number.
        
        Args:
            a (float): First number
            b (float): Second number
            
        Returns:
            float: Difference of a and b
        """
        return a - b
    
    def multiply(self, a, b):
        """
        Multiplies two numbers.
        
        Args:
            a (float): First number
            b (float): Second number
            
        Returns:
            float: Product of a and b
        """
        return a * b
    
    def divide(self, a, b):
        """
        Divides first number by second number.
        
        Args:
            a (float): First number (dividend)
            b (float): Second number (divisor)
            
        Returns:
            float: Quotient of a divided by b
            
        Raises:
            ZeroDivisionError: If b is zero
        """
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
    
    def parse_number(self, number_str):
        """
        Parses a string representation of a number to float.
        
        Args:
            number_str (str): String representation of a number
            
        Returns:
            float: Parsed number
            
        Raises:
            ValueError: If the string cannot be parsed as a number
        """
        try:
            # Check if it's a valid number string
            if '.' in number_str:
                return float(number_str)
            else:
                return int(number_str)
        except ValueError:
            raise ValueError(f"Cannot parse '{number_str}' as a number")