"""
Main entry point for the calculator application
This file initializes and runs the calculator using the MVVM architecture
"""

from calculator_view import run_calculator


def main():
    """
    Main function to start the calculator application.
    Initializes the calculator and starts the GUI event loop.
    """
    print("Starting Calculator Application...")
    print("Using MVVM Architecture Pattern")
    print("Press Ctrl+C to exit")
    
    try:
        # Run the calculator GUI
        run_calculator()
    except KeyboardInterrupt:
        print("\nCalculator application closed.")
    except Exception as e:
        print(f"An error occurred: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()