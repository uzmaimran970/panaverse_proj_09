import random

def guess_number():
    random_no = random.randint(1, 100)
    
    while True:
        try:
            user_guess = int(input("Guess a number between 1 and 100: "))
            if user_guess < 1 or user_guess > 100:
                print("Please enter a number within the valid range!")
                continue
            if user_guess > random_no:
                print("Too high! Try again.")
            elif user_guess < random_no:
                print("Too low! Try again.")
            else:
                print(f"Congratulations! You guessed the correct number: {random_no}")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

guess_number()
