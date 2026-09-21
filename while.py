# number = 100
# while 1 < number :
#     print("active")
#     number -= 1

counter = 3
while True:
    answer = input("Did you love me ? (yes/no): ")
    if answer == "yes" :
        print("I LOVE YOU TOO !!!!")
        break      
    elif answer != "yes":
        counter -= 1
        print(f"you have {counter} attempt left")
        if counter == 0:
            print("Time Out")
            break
        