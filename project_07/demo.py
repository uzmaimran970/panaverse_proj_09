import random

print("Welcome to your password generator!")
char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@$%^&*()?"

# Ensure valid integer input
while True:
    try:
        number = int(input("Amount of passwords to generate: "))
        length = int(input("Enter your password length: "))
        if number <= 0 or length <= 0:
            print("Please enter a positive number.")
            continue
        break
    except ValueError:
        print("Invalid input! Please enter a valid number.")

print("\nHere are your passwords: ")
for _ in range(number):
    password = ''.join(random.choices(char, k=length))
    print(password)
