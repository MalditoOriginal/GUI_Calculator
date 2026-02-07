# GUI Calculator

A modern calculator application built with Python using the MVVM (Model-View-ViewModel) architecture pattern.

## Features

- **Basic arithmetic operations**: Addition, subtraction, multiplication, division
- **Decimal support**: Accurate decimal number handling
- **Error handling**: Division by zero detection and error display
- **Keyboard support**: Full keyboard input support
- **Clean UI**: Simple and intuitive graphical interface

## Architecture

The application follows the MVVM pattern:

- **Model** ([`calculator_model.py`](calculator_model.py)): Core calculation logic and expression evaluation
- **ViewModel** ([`calculator_viewmodel.py`](calculator_viewmodel.py)): Manages UI state and handles user commands
- **View** ([`calculator_view.py`](calculator_view.py)): Graphical user interface using tkinter

## Requirements

- Python 3.6 or higher
- No external dependencies (uses standard library only)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/MalditoOriginal/GUI_Calculator.git
   cd GUI_Calculator
   ```

2. Run the calculator:
   ```bash
   python main.py
   ```

## Usage

### Mouse/Click Input
- Click number buttons to enter numbers
- Click operator buttons (+, -, *, /) to select operation
- Click `=` to calculate result
- Click `C` to clear all
- Click `CE` to clear entry
- Click `⌫` to backspace
- Click `±` to toggle sign
- Click `.` to enter decimal point

### Keyboard Input
- Numbers (0-9): Enter digits
- `+`, `-`, `*`, `/`: Select operator
- `Enter`: Calculate result
- `Esc`: Clear all
- `Backspace`: Delete last character
- `.`: Enter decimal point

## Division Logic Improvements

The calculator includes several improvements to division operations:

1. **Division-by-zero detection**: Enhanced regex pattern to detect `/0`, `/0.0`, `/00`, `/0.00`, etc.
2. **Decimal input validation**: Robust handling of decimal points in complex expressions
3. **Floating-point precision**: Uses Python's `Decimal` module for precise division results

## Testing

Run the test suite to verify functionality:

```bash
python test_calculator.py
```

## Project Structure

```
GUI_Calculator/
├── calculator_model.py      # Core calculation logic
├── calculator_view.py       # GUI implementation
├── calculator_viewmodel.py  # MVVM ViewModel
├── main.py                  # Entry point
├── test_calculator.py       # Unit tests
├── CMakeLists.txt           # C++ build config (for reference)
├── optimized_calculator.cpp # C++ implementation (for reference)
├── optimized_calculator.hpp # C++ header (for reference)
├── *.md files               # Documentation
└── .gitignore
```

## License

This project is open source and available under the MIT License.

## Acknowledgments

- Optimized C++ implementation included for performance comparison
- Build instructions for C++ version available in `COMPILATION_INSTRUCTIONS.md`
