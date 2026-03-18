age = 22
if age > 30:
    message = "You are over 30 years old."
else:
    message = "You are 30 years old or younger."

print(message)

high_score = True
good_credit = False
student = False

if (high_score or good_credit) and not student:
    print("You are eligible for a loan.")
else:
    print("You are not eligible for a loan.")

    for number in range(1, 11):
        if number % 2 == 0:
            print(f"{number} is even.")
        else:
            print(f"{number} is odd.")
