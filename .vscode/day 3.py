def get_number(prompt):
    """Handle user input and check for exit."""
    value = input(prompt)
    if value.strip().lower() == "exit":
        print("👋 Exiting calculator.")
        exit()
    try:
        return float(value)
    except ValueError:
        print("❌ Invalid number, try again.")
        return get_number(prompt)


def calculate(n1, n2, op):
    """Perform the operation based on the operator."""
    try:
        return {
            "+": n1 + n2,
            "-": n1 - n2,
            "*": n1 * n2,
            "/": n1 / n2,
            "//": n1 // n2,
            "%": n1 % n2,
            "**": n1**n2,
        }[op]
    except ZeroDivisionError:
        print("❌ Can't divide by zero.")
    except KeyError:
        print("❌ Unsupported operator.")


def run_calculator():
    print("\n=== Simple Python Calculator ===")
    print("Type 'exit' to quit at any time.\n")

    while True:
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        operator = input("Choose operator (+, -, *, /, //, %, **): ").strip()

        result = calculate(num1, num2, operator)
        if result is not None:
            print(f"✅ Result: {result}\n")


run_calculator()
