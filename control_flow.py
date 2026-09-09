# Do multiplication table 7 with for loop
for i in range(1,13):
    print(f"7 x {i} = {7*i}")
    
# print a left aligned pyramid of stars with 6 rows using for loop
for i in range(1,7):
    print("*" * i)
    
# Skip weekends in a calendar using for loop
days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
for day in days:
    if day == "Saturday" or day == "Sunday":
        print(f"Today is {day} and it is a weekend day")
        continue
    print(f"Today is {day} and it is a working day")
    
# Grading System
score = int(input("Enter your score: "))
if score >= 70:
    print("Grade : A")
elif score >= 60:
    print("Grade : B")
elif score >= 50:
    print("Grade : C")
elif score >= 45:
    print("Grade : D")
elif score >= 40:
    print("Grade : E")
elif score:
    print("Grade : F")

# Login System
username = input("Enter your username: ")
password = int(input("Enter your password: "))
l_username = username.lower()
print(l_username)

if l_username == "admin" and password == 1234:
    print("Login Successful")
else:
    print("Try Again!!!!")

# ATM
balance = 100000
withdrawal = int(input("Enter your withdrawal amount: "))

if withdrawal <= balance:
    balance -= withdrawal
    print("Transaction Successful")
    print(f"Your remaining balance = {balance}")
else:
    print("Insufficient Balance")

# Temperature
temperature = int(input("Enter the temperature of the day: "))
if temperature >= 35:
    print("It is very hot,drink water")
elif temperature >= 25:
    print("Warm")
elif temperature >= 15:
    print("Cool")
else:
    print("Cold")
    
# Write a program that asks the user for a number and determines whether it is even or odd.
number = int(input("Enter your number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Shopping Cart
cart = [1000,4550,3000,1200]
total = 0

for c in cart:
    total += c
print(f"Total item bought = ${total}")

# Calculate Average 
scores = [100, 90, 80, 70, 60]
total = 0

for score in scores:
    total += score
average = total / len(scores)
print(f"Average score = {average}")

