# ============================================================
# TASK 2 - CALCULATOR
# CodSoft Python Programming Internship
# ============================================================

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None  # Division by zero
    return a / b

def modulus(a, b):
    if b == 0:
        return None
    return a % b

def power(a, b):
    return a ** b

def get_number(prompt):
    """Safely get a number from user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  ⚠️  Invalid input! Please enter a valid number.")

def main():
    print("\n" + "=" * 40)
    print("       🧮  SIMPLE CALCULATOR")
    print("=" * 40)

    operations = {
        "1": ("Addition (+)", add),
        "2": ("Subtraction (-)", subtract),
        "3": ("Multiplication (*)", multiply),
        "4": ("Division (/)", divide),
        "5": ("Modulus (%)", modulus),
        "6": ("Power (**)", power),
    }

    while True:
        print("\n  Select Operation:")
        for key, (name, _) in operations.items():
            print(f"  {key}. {name}")
        print("  7. Exit")
        print()

        choice = input("  Enter choice (1-7): ").strip()

        if choice == "7":
            print("\n  👋 Thanks for using the Calculator! Goodbye!\n")
            break

        if choice not in operations:
            print("  ⚠️  Invalid choice! Please select 1-7.")
            continue

        op_name, op_func = operations[choice]
        print(f"\n  --- {op_name} ---")

        num1 = get_number("  Enter first number : ")
        num2 = get_number("  Enter second number: ")

        result = op_func(num1, num2)

        print("\n" + "-" * 40)
        if result is None:
            print("  ❌ Error: Division by zero is not allowed!")
        else:
            # Display cleanly (remove .0 for whole numbers)
            n1 = int(num1) if num1 == int(num1) else num1
            n2 = int(num2) if num2 == int(num2) else num2
            res = int(result) if result == int(result) else round(result, 6)

            symbols = {"1": "+", "2": "-", "3": "*", "4": "/", "5": "%", "6": "**"}
            print(f"  {n1} {symbols[choice]} {n2} = {res}")
        print("-" * 40)

        again = input("\n  Perform another calculation? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("\n  👋 Thanks for using the Calculator! Goodbye!\n")
            break

if __name__ == "__main__":
    main()
