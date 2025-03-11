import random

def computer_guess():
    low, high = 1, 100
    
    while True:
        guess = (low + high) 
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").lower()
        
        if feedback == 'c':
            print(f"The computer guessed your number {guess} correctly!")
            break
        elif feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        else:
            print("Invalid input. Please enter 'H', 'L', or 'C'.")

computer_guess()
