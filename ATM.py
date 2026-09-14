balance = 1000
for attempt in range(1,5):
    print("Welcome to the Olofa Bank ATM")
    print("Please select an option:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    option = int(input("Enter your option: "))
    if option == 1:
        print(f"Your balance is #{balance}")
        menu = input("Do you want to go back to the menu? (y/n): ")
        if menu.lower() == "y":
            continue
            print("Welcome to the Olofa Bank ATM")  
            print("Please select an option:")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")
            option = int(input("Enter your option: "))
        else:
            print("Thank you for using the Olofa Bank ATM")
            break
    elif option == 2:
        deposit = int(input("Enter your deposit amount: "))
        if deposit <= 0:
            print("Deposit amount must be greater than zero.")
            continue
        balance += deposit
        print(f"Your new balance is #{balance}")
        menu = input("Do you want to go back to the menu? (y/n): ")
        if menu.lower() == "y":
            continue
            print("Welcome to the Olofa Bank ATM")
            print("Please select an option:")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")
            option = int(input("Enter your option: "))
        else:
            print("Thank you for using the Olofa Bank ATM")
            break
    elif option == 3:
        withdrawal = int(input("Enter your withdrawal amount: "))
        if withdrawal <= 0:
            print("Withdrawal amount must be greater than zero.")
            continue
        if withdrawal <= balance:
            balance -= withdrawal
            print(f"Your new balance is #{balance}")
        else:
            print("Insufficient balance")
        menu = input("Do you want to go back to the menu? (y/n): ")
        if menu.lower() == "y":
            continue
            print("Welcome to the Olofa Bank ATM")
            print("Please select an option:")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")
            option = int(input("Enter your option: "))
        else:
            print("Thank you for using the Olofa Bank ATM")
            break
    elif option == 4:
        print("Thank you for using the Olofa Bank ATM")
        break    