import math

# ===== Calculator Functions =====
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def power(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of negative number.")
    return math.sqrt(a)

def factorial(n):
    if n < 0:
        raise ValueError("Cannot compute factorial of negative number.")
    return math.factorial(n)

def logarithm(a, base=10):
    if a <= 0:
        raise ValueError("Logarithm undefined for non-positive numbers.")
    if base <= 1:
        raise ValueError("Base must be greater than 1.")
    return math.log(a, base)

def modulus(a, b):
    if b == 0:
        raise ValueError("Cannot compute modulus with zero divisor.")
    return a % b


# ===== Helper Input Functions =====
def safe_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def safe_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")

def get_two_numbers():
    a = safe_float_input("Enter first number: ")
    b = safe_float_input("Enter second number: ")
    return a, b


# ===== CLI Menu =====
def show_menu():
    print("\n===== Welcome to CLI Calculator =====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Factorial")
    print("8. Logarithm")
    print("9. Modulus")
    print("0. Exit")
    choice = input("Please select an option (0–9): ")
    return choice.strip()


# ===== Main Loop =====
def main():
    while True:
        choice = show_menu()

        if choice == '0':
            print("\nThanks for using CLI Calculator. Goodbye!")
            break

        try:
            if choice == '1':
                a, b = get_two_numbers()
                print(f"Result: {add(a, b)}")

            elif choice == '2':
                a, b = get_two_numbers()
                print(f"Result: {subtract(a, b)}")

            elif choice == '3':
                a, b = get_two_numbers()
                print(f"Result: {multiply(a, b)}")

            elif choice == '4':
                a, b = get_two_numbers()
                print(f"Result: {divide(a, b)}")

            elif choice == '5':
                a = safe_float_input("Enter base number: ")
                b = safe_float_input("Enter exponent: ")
                print(f"Result: {power(a, b)}")

            elif choice == '6':
                a = safe_float_input("Enter number to find square root of: ")
                print(f"Result: {square_root(a)}")

            elif choice == '7':
                n = safe_int_input("Enter a non-negative integer for factorial: ")
                print(f"Result: {factorial(n)}")

            elif choice == '8':
                a = safe_float_input("Enter the number for logarithm: ")
                base_input = input("Enter the base (default is 10): ").strip()
                base = float(base_input) if base_input else 10
                print(f"Result: {logarithm(a, base)}")

            elif choice == '9':
                a, b = get_two_numbers()
                print(f"Result: {modulus(a, b)}")

            else:
                print("Invalid option. Please try again.")

        except ValueError as e:
            print(f"Error: {e}")

        input("\nPress Enter to continue...")

# ===== Run Program =====
if __name__ == "__main__":
    main()
