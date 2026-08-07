import os

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid numerical value.")

def get_operator():
    valid_operators = ['+', '-', '*', '/']
    while True:
        op = input("Enter an operation (+, -, *, /): ").strip()
        if op in valid_operators:
            return op
        print(f"Invalid operator. Please choose from: {', '.join(valid_operators)}")

def perform_calculation():
    print("\n--- New Calculation ---")
    num1 = get_number("Enter the first number: ")
    operator = get_operator()
    num2 = get_number("Enter the second number: ")
    
    # Check for division by zero defensively
    if operator == '/' and num2 == 0:
        print("Error: Division by zero is undefined. Calculation aborted.")
        return

    # Evaluate the operation
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2

    # Strip decimal if it is a whole number for cleaner output formatting
    formatted_num1 = int(num1) if num1.is_integer() else num1
    formatted_num2 = int(num2) if num2.is_integer() else num2
    formatted_result = int(result) if result.is_integer() else result

    equation = f"{formatted_num1} {operator} {formatted_num2} = {formatted_result}"
    
    # Display result to user
    print(f"\nResult: {equation}")
    
    # Record to equations.txt defensively
    try:
        with open("equations.txt", "a", encoding="utf-8") as file:
            file.write(equation + "\n")
    except IOError as e:
        print(f"Error writing to file: {e}")

def view_previous_calculations():
    """Reads and prints all equations from equations.txt safely."""
    print("\n--- Previous Calculations ---")
    filename = "equations.txt"
    
    # Defensive check: verify file exists before attempting to read
    if not os.path.exists(filename):
        print("No historical equations found. The file 'equations.txt' does not exist yet.")
        return
        
    try:
        with open(filename, "a+", encoding="utf-8") as file:
            content = file.read().strip()
            if not content:
                print("The 'equations.txt' file is currently empty.")
            else:
                print(content)
    except IOError as e:
        print(f"Error reading file: {e}")

def main():
    """Main application loop."""
    while True:
        print("    Simple Calculator App     ")
        print("==============================")
        print("1. Perform a calculation")
        print("2. View previous calculations")
        print("3. Exit program")
        
        choice = input("Please select an option (1-3): ").strip()
        if choice == '1':
            perform_calculation()
        elif choice == '2':
            view_previous_calculations()
        elif choice == '3':
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid selection. Please choose options 1, 2, or 3.")

if __name__ == "__main__":
    main()


