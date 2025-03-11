import random
import string


words = ["python", "developer", "keyboard", "monitor", "laptop", "programming", "hangman",
         "internet", "software", "hardware", "algorithm", "debugging", "variable", "function",
         "condition", "database", "compiler", "syntax", "library", "framework", "browser",
         "virtual", "encryption", "authentication", "network", "frontend", "backend"]

# Hangman visual stages
hangman_stages = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]

def get_valid_word(words):
    return random.choice(words).upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = len(hangman_stages) - 1  

    print("Welcome to Hangman! Try to guess the word.")

    while len(word_letters) > 0 and incorrect_guesses < max_incorrect_guesses:
        print(hangman_stages[incorrect_guesses])  
        print(f"\nUsed letters: {' '.join(sorted(used_letters))}")
        word_display = [letter if letter in used_letters else '_' for letter in word]
        print("Word: " + ' '.join(word_display))

        user_letter = input("\nGuess a letter: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                incorrect_guesses += 1
                print(f"Wrong guess! Attempts left: {max_incorrect_guesses - incorrect_guesses}")
        elif user_letter in used_letters:
            print("You already guessed that letter. Try again.")
        else:
            print("Invalid input. Please enter a letter (A-Z).")

    # Endgame
    if len(word_letters) == 0:
        print(f"\nCongratulations! You guessed the word: {word}")
    else:
        print(hangman_stages[-1])  # Show final hangman stage
        print(f"\nGame Over! The word was: {word}")

# Start the game
hangman()
