"""
Calculator View - GUI implementation using tkinter
This class creates the user interface and binds it to the ViewModel
"""

import tkinter as tk
from tkinter import messagebox
from calculator_viewmodel import CalculatorViewModel


class CalculatorView:
    """
    View component of the MVVM pattern.
    Creates the graphical user interface and binds it to the ViewModel.
    """
    
    def __init__(self, root):
        """
        Initialize the calculator view.
        
        Args:
            root: The root tkinter window
        """
        self.root = root
        self.viewmodel = CalculatorViewModel()
        
        # Set up the window
        self.root.title("Calculator - MVVM")
        self.root.geometry("300x400")
        self.root.resizable(False, False)
        
        # Bind the ViewModel's display updates to the View
        self.viewmodel.add_observer(self.update_display)
        
        # Create the GUI elements
        self.create_widgets()
        
        # Bind keyboard events
        self.bind_keyboard_events()
    
    def create_widgets(self):
        """Create and arrange all GUI widgets."""
        # Configure grid weights for responsive layout
        for i in range(5):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
        
        # Create the display field
        self.display_var = tk.StringVar()
        self.display_var.set(self.viewmodel.get_display_value())
        
        self.display = tk.Entry(
            self.root,
            textvariable=self.display_var,
            font=("Arial", 18),
            justify="right",
            state="readonly",
            bd=5,
            relief="sunken"
        )
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)
        
        # Define button labels and positions
        button_config = [
            ('C', 1, 0, self.clear_all),
            ('CE', 1, 1, self.clear_entry),
            ('⌫', 1, 2, self.backspace),
            ('/', 1, 3, lambda: self.input_operator('/')),
            
            ('7', 2, 0, lambda: self.input_digit('7')),
            ('8', 2, 1, lambda: self.input_digit('8')),
            ('9', 2, 2, lambda: self.input_digit('9')),
            ('*', 2, 3, lambda: self.input_operator('*')),
            
            ('4', 3, 0, lambda: self.input_digit('4')),
            ('5', 3, 1, lambda: self.input_digit('5')),
            ('6', 3, 2, lambda: self.input_digit('6')),
            ('-', 3, 3, lambda: self.input_operator('-')),
            
            ('1', 4, 0, lambda: self.input_digit('1')),
            ('2', 4, 1, lambda: self.input_digit('2')),
            ('3', 4, 2, lambda: self.input_digit('3')),
            ('+', 4, 3, lambda: self.input_operator('+')),
            
            ('±', 5, 0, self.toggle_sign),
            ('0', 5, 1, lambda: self.input_digit('0')),
            ('.', 5, 2, self.input_decimal),
            ('=', 5, 3, self.calculate_result)
        ]
        
        # Create buttons
        for (text, row, col, command) in button_config:
            btn = tk.Button(
                self.root,
                text=text,
                font=("Arial", 14),
                command=command,
                height=2
            )
            btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
    
    def bind_keyboard_events(self):
        """Bind keyboard events to calculator functions."""
        self.root.bind('<Key>', self.on_key_press)
        self.root.focus_set()  # Allow window to receive key events
    
    def on_key_press(self, event):
        """Handle keyboard input."""
        key = event.char
        
        if key.isdigit():
            self.input_digit(key)
        elif key == '.':
            self.input_decimal()
        elif key in '+-*/':
            self.input_operator(key)
        elif key == '\r':  # Enter key
            self.calculate_result()
        elif key.lower() == 'c':
            self.clear_all()
        elif key == '\x08':  # Backspace key
            self.backspace()
    
    def update_display(self, value):
        """
        Update the display with the new value.
        
        Args:
            value (str): New value to display
        """
        self.display_var.set(value)
    
    def input_digit(self, digit):
        """
        Handle input of a digit.
        
        Args:
            digit (str): The digit that was pressed
        """
        self.viewmodel.input_digit(digit)
    
    def input_decimal(self):
        """Handle input of a decimal point."""
        self.viewmodel.input_decimal()
    
    def input_operator(self, op):
        """
        Handle input of an operator (+, -, *, /).
        
        Args:
            op (str): The operator that was pressed
        """
        self.viewmodel.input_operator(op)
    
    def calculate_result(self):
        """Calculate the result of the current operation."""
        self.viewmodel.calculate_result()
    
    def clear_all(self):
        """Clear all calculator state (reset to initial state)."""
        self.viewmodel.clear_all()
    
    def clear_entry(self):
        """Clear the current entry (display value)."""
        self.viewmodel.clear_entry()
    
    def backspace(self):
        """Remove the last character from the current input."""
        self.viewmodel.backspace()
    
    def toggle_sign(self):
        """Toggle the sign of the current number."""
        self.viewmodel.toggle_sign()


def run_calculator():
    """Run the calculator application."""
    root = tk.Tk()
    app = CalculatorView(root)
    root.mainloop()


if __name__ == "__main__":
    run_calculator()