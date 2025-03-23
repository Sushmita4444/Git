# main_calculator.py

from dev1_addition import add
from dev2_subtraction import subtract
from dev3_multiplication import multiply
from dev4_division import divide

def get_input():
    """Get and validate user input."""
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            return num1, num2
        except ValueError:
            print("Invalid input! Please enter numeric values.")

def main():
    """Main function to execute the calculator."""
    while True:
        print("\nCLI Calculator")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        
        choice = input("Choose an operation (1-5): ")

        if choice == "5":
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ["1", "2", "3", "4"]:
            num1, num2 = get_input()

            if choice == "1":
                result = add(num1, num2)
                operation = "Addition"
            elif choice == "2":
                result = subtract(num1, num2)
                operation = "Subtraction"
            elif choice == "3":
                result = multiply(num1, num2)
                operation = "Multiplication"
            elif choice == "4":
                result = divide(num1, num2)
                operation = "Division"

            print(f"\n{operation} result: {result}\n")
        else:
            print("Invalid choice! Please select a valid option (1-5).")

if __name__ == "__main__":
    main()
