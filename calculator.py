for attempt in range(1, 5):

    print("\n===== CASIO CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print("6. Coming soon...")

    option = int(input("Choose an option: "))

    if option == 1:

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        result = num1 + num2

        print(f"Result: {result}")

    elif option == 2:

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        result = num1 - num2

        print(f"Result: {result}")

    elif option == 3:

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        result = num1 * num2

        print(f"Result: {result}")

    elif option == 4:

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if num2 == 0:
            print("You cannot divide by zero.")
            continue

        result = num1 / num2

        print(f"Result: {result}")

    elif option == 5:

        print("Thank you for using CASIO Calculator.")
        break
    elif option == 6:
        pass
        print("This feature is coming soon. Stay tuned!")

    else:

        print("Invalid option.")
        continue