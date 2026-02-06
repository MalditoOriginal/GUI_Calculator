"""
Calculator ViewModel - Manages display state, current input, operation state, and command handlers
This class acts as an intermediary between the Model and View components
"""

from calculator_model import CalculatorModel


class CalculatorViewModel:
    """
    ViewModel component of the MVVM pattern.
    Manages the state of the calculator and handles user commands.
    Communicates with both the Model (for calculations) and the View (for UI updates).
    """
    
    def __init__(self):
        """Initialize the calculator ViewModel"""
        self.model = CalculatorModel()
        self.display_value = "0"
        self.current_input = ""
        self.operator = None
        self.previous_value = 0
        self.should_reset_display = False
        
        # Observers for display updates
        self.observers = []
    
    def add_observer(self, observer):
        """
        Add an observer to be notified when the display value changes.
        
        Args:
            observer: A callback function to be called when display updates
        """
        self.observers.append(observer)
    
    def notify_observers(self):
        """Notify all observers that the display value has changed."""
        for observer in self.observers:
            observer(self.display_value)
    
    def get_display_value(self):
        """
        Get the current display value.
        
        Returns:
            str: Current value to display
        """
        return self.display_value
    
    def input_digit(self, digit):
        """
        Handle input of a digit.
        
        Args:
            digit (str): The digit that was pressed
        """
        if self.should_reset_display:
            self.display_value = "0"
            self.should_reset_display = False
        
        if self.display_value == "0":
            self.display_value = digit
        else:
            self.display_value += digit
        
        self.notify_observers()
    
    def input_decimal(self):
        """Handle input of a decimal point."""
        if self.should_reset_display:
            self.display_value = "0"
            self.should_reset_display = False
        
        # Add decimal point only if not already present in current number
        if '.' not in self.display_value.split('/')[-1].split('*')[-1].split('+')[-1].split('-')[-1]:
            self.display_value += '.'
            self.notify_observers()
    
    def input_operator(self, op):
        """
        Handle input of an operator (+, -, *, /).
        
        Args:
            op (str): The operator that was pressed
        """
        # If there's already an operator pending, calculate the previous operation first
        if self.operator and not self.should_reset_display:
            self.calculate_result()
        
        # Store the current display value as the previous value
        self.previous_value = float(self.display_value)
        
        # Set the operator
        self.operator = op
        
        # Prepare for next input
        self.should_reset_display = True
    
    def calculate_result(self):
        """Calculate the result of the current operation."""
        if self.operator is None:
            return
        
        try:
            current_value = float(self.display_value)
            
            if self.operator == '+':
                result = self.model.add(self.previous_value, current_value)
            elif self.operator == '-':
                result = self.model.subtract(self.previous_value, current_value)
            elif self.operator == '*':
                result = self.model.multiply(self.previous_value, current_value)
            elif self.operator == '/':
                result = self.model.divide(self.previous_value, current_value)
            else:
                raise ValueError(f"Unknown operator: {self.operator}")
            
            # Format result to remove unnecessary decimal places
            if result == int(result):
                self.display_value = str(int(result))
            else:
                self.display_value = f"{result:g}"  # Removes trailing zeros
            
            # Reset operator and prepare for next calculation
            self.operator = None
            self.should_reset_display = True
            self.previous_value = 0
            
            self.notify_observers()
            
        except ZeroDivisionError:
            self.display_value = "Error"
            self.notify_observers()
        except Exception as e:
            self.display_value = "Error"
            self.notify_observers()
    
    def clear_all(self):
        """Clear all calculator state (reset to initial state)."""
        self.display_value = "0"
        self.current_input = ""
        self.operator = None
        self.previous_value = 0
        self.should_reset_display = False
        
        self.notify_observers()
    
    def clear_entry(self):
        """Clear the current entry (display value)."""
        self.display_value = "0"
        self.current_input = ""
        
        self.notify_observers()
    
    def backspace(self):
        """Remove the last character from the current input."""
        if len(self.display_value) > 1:
            self.display_value = self.display_value[:-1]
        else:
            self.display_value = "0"
        
        self.notify_observers()
    
    def toggle_sign(self):
        """Toggle the sign of the current number."""
        if self.display_value != "0":
            if self.display_value.startswith("-"):
                self.display_value = self.display_value[1:]
            else:
                self.display_value = "-" + self.display_value
            
            self.notify_observers()
    
    def calculate_percentage(self):
        """Calculate the percentage of the current number."""
        try:
            current_value = float(self.display_value)
            result = current_value / 100
            
            # Format result to remove unnecessary decimal places
            if result == int(result):
                self.display_value = str(int(result))
            else:
                self.display_value = f"{result:g}"  # Removes trailing zeros
            
            self.notify_observers()
        except Exception:
            self.display_value = "Error"
            self.notify_observers()