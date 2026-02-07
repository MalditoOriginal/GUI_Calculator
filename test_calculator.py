"""
Test script to verify calculator functionality without GUI
"""

from calculator_model import CalculatorModel
from calculator_viewmodel import CalculatorViewModel


def test_calculator_model():
    """Test the calculator model functions."""
    print("Testing Calculator Model...")
    
    model = CalculatorModel()
    
    # Test basic operations
    assert model.add(2, 3) == 5
    assert model.add(-5, 3) == -2
    assert model.add(0, 100) == 100
    
    assert model.subtract(5, 3) == 2
    assert model.subtract(3, 5) == -2
    assert model.subtract(0, 0) == 0
    
    assert model.multiply(4, 3) == 12
    assert model.multiply(-4, 3) == -12
    assert model.multiply(0, 100) == 0
    
    assert model.divide(10, 2) == 5
    assert model.divide(7, 2) == 3.5
    assert model.divide(-10, 2) == -5
    
    # Test division by zero
    try:
        model.divide(10, 0)
        assert False, "Should raise ZeroDivisionError"
    except ZeroDivisionError:
        print("[PASS] Division by zero handled correctly")
    
    # Test expression evaluation
    assert model.evaluate_expression("2 + 3") == 5
    assert model.evaluate_expression("10 - 4") == 6
    assert model.evaluate_expression("3 * 4") == 12
    assert model.evaluate_expression("15 / 3") == 5
    assert model.evaluate_expression("2.5 + 3.7") == 6.2
    
    # Test complex expression
    assert model.evaluate_expression("(2 + 3) * 4") == 20
    assert model.evaluate_expression("((2 + 3) * (4 - 1)) / 5") == 3
    
    # Test division by zero in expression
    try:
        model.evaluate_expression("10 / 0")
        assert False, "Should raise ZeroDivisionError"
    except ZeroDivisionError:
        print("[PASS] Division by zero in expression handled correctly")
    
    # Test negative numbers
    assert model.evaluate_expression("-5 + 3") == -2
    assert model.evaluate_expression("10 - -4") == 14
    
    # Test chained operations
    assert model.evaluate_expression("2 + 3 + 4 + 5") == 14
    assert model.evaluate_expression("100 / 2 / 5") == 10
    
    # Test parse_number
    assert model.parse_number("42") == 42
    assert model.parse_number("3.14") == 3.14
    assert model.parse_number("-5") == -5
    
    try:
        model.parse_number("abc")
        assert False, "Should raise ValueError for invalid number string"
    except ValueError:
        print("[PASS] Invalid number string 'abc' handled correctly")
    
    print("[PASS] Calculator Model tests passed!")


def test_calculator_viewmodel():
    """Test the calculator viewmodel functions."""
    print("\nTesting Calculator ViewModel...")
    
    vm = CalculatorViewModel()
    
    # Test initial state
    assert vm.get_display_value() == "0"
    
    # Test digit input
    vm.input_digit("5")
    assert vm.get_display_value() == "5"
    
    vm.input_digit("3")
    assert vm.get_display_value() == "53"
    
    # Test decimal input
    vm.input_decimal()
    vm.input_digit("7")
    assert vm.get_display_value() == "53.7"
    
    # Test clear
    vm.clear_all()
    assert vm.get_display_value() == "0"
    
    # Test simple calculation: 5 + 3 = 8
    vm.input_digit("5")
    vm.input_operator("+")
    vm.input_digit("3")
    vm.calculate_result()
    assert vm.get_display_value() == "8"
    
    # Reset for next test
    vm.clear_all()
    
    # Test another calculation: 10 - 4 = 6
    vm.input_digit("1")
    vm.input_digit("0")
    vm.input_operator("-")
    vm.input_digit("4")
    vm.calculate_result()
    assert vm.get_display_value() == "6"
    
    # Reset for next test
    vm.clear_all()
    
    # Test multiplication: 6 * 7 = 42
    vm.input_digit("6")
    vm.input_operator("*")
    vm.input_digit("7")
    vm.calculate_result()
    assert vm.get_display_value() == "42"
    
    # Reset for next test
    vm.clear_all()
    
    # Test division: 15 / 3 = 5
    vm.input_digit("1")
    vm.input_digit("5")
    vm.input_operator("/")
    vm.input_digit("3")
    vm.calculate_result()
    assert vm.get_display_value() == "5"
    
    # Reset for next test
    vm.clear_all()
    
    # Test division by zero (now shows full error message)
    vm.input_digit("5")
    vm.input_operator("/")
    vm.input_digit("0")
    vm.calculate_result()
    assert vm.get_display_value().startswith("Error:")
    
    vm.clear_all()
    assert vm.get_display_value() == "0"
    
    # Test backspace
    vm.input_digit("1")
    vm.input_digit("2")
    vm.input_digit("3")
    assert vm.get_display_value() == "123"
    vm.backspace()
    assert vm.get_display_value() == "12"
    vm.backspace()
    assert vm.get_display_value() == "1"
    vm.backspace()
    assert vm.get_display_value() == "0"
    
    # Test clear entry (CE)
    vm.input_digit("5")
    vm.input_digit("6")
    assert vm.get_display_value() == "56"
    vm.clear_entry()
    assert vm.get_display_value() == "0"
    
    # Test toggle sign
    vm.clear_all()  # Reset display to "0"
    vm.input_digit("5")
    assert vm.get_display_value() == "5"
    vm.toggle_sign()
    assert vm.get_display_value() == "-5"
    vm.toggle_sign()
    assert vm.get_display_value() == "5"
    
    # Test percentage calculation
    vm.clear_all()  # Reset display to "0"
    vm.input_digit("5")
    vm.input_digit("0")
    vm.calculate_percentage()
    assert vm.get_display_value() == "0.5"
    
    vm.clear_all()
    vm.input_digit("2")
    vm.input_digit("5")
    vm.calculate_percentage()
    assert vm.get_display_value() == "0.25"
    
    # Test chained calculations
    vm.clear_all()
    vm.input_digit("1")
    vm.input_operator("+")
    vm.input_digit("2")
    vm.calculate_result()  # 1+2=3
    assert vm.get_display_value() == "3"
    
    vm.input_operator("+")
    vm.input_digit("3")
    vm.calculate_result()  # 3+3=6
    assert vm.get_display_value() == "6"
    
    # Test negative number input: -5 + 3 = -2
    vm.clear_all()
    vm.input_digit("5")
    vm.toggle_sign()
    vm.input_operator("+")
    vm.input_digit("3")
    vm.calculate_result()
    assert vm.get_display_value() == "-2"
    
    # Test decimal precision
    vm.clear_all()
    vm.input_digit("1")
    vm.input_decimal()
    vm.input_digit("5")
    vm.input_operator("*")
    vm.input_digit("2")
    vm.calculate_result()
    assert vm.get_display_value() == "3"
    
    # Test error display after invalid operation
    vm.clear_all()
    vm.input_digit("1")
    vm.input_operator("/")
    vm.input_digit("0")
    vm.calculate_result()
    assert vm.get_display_value().startswith("Error:")
    
    print("[PASS] Calculator ViewModel tests passed!")


def test_calculator_view():
    """Test the calculator view functions."""
    print("\nTesting Calculator View...")
    
    import tkinter as tk
    from calculator_view import CalculatorView
    
    root = tk.Tk()
    view = CalculatorView(root)
    
    # Test initial display
    assert view.viewmodel.get_display_value() == "0"
    
    # Test digit input through view
    view.input_digit("7")
    assert view.viewmodel.get_display_value() == "7"
    
    # Test operator input through view
    view.input_operator("+")
    assert view.viewmodel.operator == "+"
    
    # Test clear through view
    view.clear_all()
    assert view.viewmodel.get_display_value() == "0"
    
    # Test backspace through view
    view.input_digit("9")
    view.input_digit("8")
    view.backspace()
    assert view.viewmodel.get_display_value() == "9"
    
    root.destroy()
    
    print("[PASS] Calculator View tests passed!")


def main():
    """Run all tests."""
    print("Running Calculator Tests...\n")
    
    try:
        test_calculator_model()
        test_calculator_viewmodel()
        test_calculator_view()
        print("\n[PASS] All tests passed! The calculator components are working correctly.")
    except Exception as e:
        print(f"\n[FAIL] Test failed with error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
