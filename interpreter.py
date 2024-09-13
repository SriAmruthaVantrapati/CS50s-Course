def main():
    # Prompt the user for an arithmetic expression
    expression = input("Enter an arithmetic expression (x y z): ").strip()

    # Split the expression into its components
    parts = expression.split()

    # Extract x, y, and z from the parts
    x = int(parts[0])
    operator = parts[1]
    z = int(parts[2])

    # Perform the arithmetic operation based on the operator
    if operator == '+':
        result = x + z
    elif operator == '-':
        result = x - z
    elif operator == '*':
        result = x * z
    elif operator == '/':
        result = x / z
    else:
        raise ValueError("Invalid operator")

    # Output the result formatted to one decimal place
    print(f"{result:.1f}")

# Call the main function
if __name__ == "__main__":
    main()
