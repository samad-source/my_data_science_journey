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