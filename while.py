# WHILE LOOP
number = 100
while 1 < number :
    print("active")
    number -= 1
# PROMPT USER INPUT UNTIL CORRECT ANSWER IS GIVEN
count = 3
while True:
    answer = input("Did you love me ? (yes/no): ")
    if answer == "yes" :
        print("I LOVE YOU TOO !!!!")
        break      
    elif answer != "yes":
        count -= 1
        print(f"you have {count} attempt left")
        if count == 0:
            print("Time Out")
            break
# ATM BANKING SYSTEM (WHILE LOOP)
bank_balance = 1000
counter = 3
while counter > 0:
    counter -= 1
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    option = input("Choose an option (1/2/3): ")
    if option == "1" :
        print(f"Your balance is: #{bank_balance}")
        print(f"You have {counter} attempt left")
    elif option == "2" :
        deposit_amount = int(input("Enter the amount to deposit: "))
        bank_balance += deposit_amount
        print(f"Your new balance is: #{bank_balance}")
        print(f"You have {counter} attempt left")
    elif option == "3" :
        withdraw_amount = int(input("Enter the amount to withdraw: "))
        if withdraw_amount <= bank_balance:
            bank_balance -= withdraw_amount
            print(f"Your new balance is: #{bank_balance}")
        else:
            print("Insufficient funds.")
        print(f"You have {counter} attempt left")
    else:
        print("Invalid option. Please try again.")
        print(f"You have {counter} attempt left")
        