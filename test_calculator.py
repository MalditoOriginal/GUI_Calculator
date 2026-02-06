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
    assert model.subtract(5, 3) == 2
    assert model.multiply(4, 3) == 12
    assert model.divide(10, 2) == 5
    
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
    
    # Test division by zero in expression
    try:
        model.evaluate_expression("10 / 0")
        assert False, "Should raise ZeroDivisionError"
    except ZeroDivisionError:
        print("[PASS] Division by zero in expression handled correctly")
    
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
    
    # Test division by zero
    vm.input_digit("5")
    vm.input_operator("/")
    vm.input_digit("0")
    vm.calculate_result()
    assert vm.get_display_value() == "Error"
    
    vm.clear_all()
    assert vm.get_display_value() == "0"
    
    print("[PASS] Calculator ViewModel tests passed!")


def main():
    """Run all tests."""
    print("Running Calculator Tests...\n")
    
    try:
        test_calculator_model()
        test_calculator_viewmodel()
        print("\n[PASS] All tests passed! The calculator components are working correctly.")
    except Exception as e:
        print(f"\n[FAIL] Test failed with error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()