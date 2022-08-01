attempt=5
for i in range(5):
    user_input=int(input("Enter your number: "))

    if user_input ==7:
        print("You won!")
        break
    else:
        print("Sorry! Try again later.")