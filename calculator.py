
import math

# Store calculation history in memory
history = []

while True:
    print("\n===== PYTHON CALCULATOR =====")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Square")
    print("6. Square Root")
    print("7. View History")
    print("8. Exit")

    choice = input("Choose an option (1-8): ")

    if choice == "8":
        print("Calculator closed. Goodbye!")
        break

    elif choice == "7":
        print("\n--- Calculation History ---")
        if history:
            for item in history:
                print(item)
        else:
            print("No calculations yet.")
        continue

    elif choice in ["1", "2", "3", "4"]:
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == "1":
                result = a + b
                operation = "+"

            elif choice == "2":
                result = a - b
                operation = "-"

            elif choice == "3":
                result = a * b
                operation = "*"

            elif choice == "4":
                if b == 0:
                    print("Error: Cannot divide by zero!")
                    continue
                result = a / b
                operation = "/"

            calculation = f"{a:g} {operation} {b:g} = {result:g}"
            print("Result:", result)
            history.append(calculation)

        except ValueError:
            print("Invalid input! Please enter numbers.")

    elif choice == "5":
        try:
            a = float(input("Enter a number: "))
            result = a ** 2
            calculation = f"{a:g} squared = {result:g}"
            print("Result:", result)
            history.append(calculation)

        except ValueError:
            print("Invalid input! Please enter a number.")

    elif choice == "6":
        try:
            a = float(input("Enter a number: "))

            if a < 0:
                print("Error: Cannot calculate the square root of a negative number.")
                continue

            result = math.sqrt(a)
            calculation = f"Square root of {a:g} = {result:g}"
            print("Result:", result)
            history.append(calculation)

        except ValueError:
            print("Invalid input! Please enter a number.")

    else:
        print("Invalid choice! Select an option from 1 to 8.")
