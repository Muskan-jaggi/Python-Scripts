import random

# Hangman ASCII Art
hangman_ascii = r"""
 _
| |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |
                   |___/
"""

print(hangman_ascii)

# List of words
word_list = [
    "banana", "computer", "programming", "elephant", "guitar",
    "jazz", "keyboard", "zebra", "restaurant", "xylophone",
    "kangaroo", "landscape", "mountain", "ocean", "penguin",
    "quilt", "robot", "sunflower", "volcano", "waterfall"
]

# Hangman stages
hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


def print_hangman(call_count):
    if call_count < len(hangman):
        print(hangman[call_count])
    else:
        print(hangman[-1])


def guessfn(word, blank_list, call_count):
    # Main loop to guess letters
    while call_count < len(hangman):
        guess = input("\nGuess a letter: ").lower()

        # Input validation (only single letters)
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        # Check if the guessed letter is in the word
        found = False
        for i in range(len(word)):
            if word[i] == guess:
                blank_list[i] = guess
                found = True

        # If the guess was incorrect, increment the call_count
        if not found:
            call_count += 1
            print_hangman(call_count)
        else:
            print("Good guess!")

        # Show current progress
        print("Current progress:", ' '.join(blank_list))

        # Check if the player has guessed the word
        if "_" not in blank_list:
            print("You win! Congratulations!")
            break
    else:
        print(f"You lose! The word was '{word}'.")


word = random.choice(word_list)
blank_list = ["_"] * len(word)
call_count = 0


print("The Word is:", ' '.join(blank_list))


guessfn(word, blank_list, call_count)


