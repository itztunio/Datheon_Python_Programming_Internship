
import random

# List of English words
words = ["JAVA", "PYTHON", "COMPUTER", "DATHEON", "LEARNING"]

# Select a random word
secret_word = random.choice(words)

# Store guessed letters
guessed_letters = set()

# Maximum wrong attempts
max_attempts = 6
wrong_attempts = 0

# ASCII Hangman stages
hangman_stages = [
    """
     +---+
     |   |
         |
         |
         |
    =======
    """,
    """
     +---+
     |   |
     O   |
         |
         |
    =======
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
    =======
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
    =======
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
    =======
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
    =======
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
    =======
    """
]

print("=" * 35)
print("      HANGMAN WORD GUESSING GAME")
print("=" * 35)
print("Guess the hidden English word!")
print("You have 6 wrong attempts.")

# Main game loop
while wrong_attempts < max_attempts:

    # Display Hangman drawing
    print(hangman_stages[wrong_attempts])

    # Display guessed word
    masked_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            masked_word += letter + " "
        else:
            masked_word += "_ "

    print("Word:", masked_word)
    print("Wrong attempts:", wrong_attempts, "/", max_attempts)

    if guessed_letters:
        print("Guessed letters:", " ".join(sorted(guessed_letters)))
    else:
        print("Guessed letters: None")

    # Check if the word is complete
    if all(letter in guessed_letters for letter in secret_word):
        print("\nCongratulations! You Win!")
        print("The word was:", secret_word)
        break

    # Take user input
    guess = input("\nGuess a letter: ").strip().upper()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter (A-Z).")
        continue

    # Prevent duplicate guesses
    if guess in guessed_letters:
        print("You already guessed this letter. Try another!")
        continue

    guessed_letters.add(guess)

    # Check the guess
    if guess in secret_word:
        print("Correct guess!")
    else:
        wrong_attempts += 1
        print("Wrong guess!")

# Display final result
if wrong_attempts == max_attempts:
    print(hangman_stages[wrong_attempts])
    print("\nGAME OVER! You lost.")
    print("The correct word was:", secret_word)

print("\nThanks for playing!")
