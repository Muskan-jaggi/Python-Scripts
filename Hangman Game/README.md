## Hangman Game 🎉

This is a Python-based Hangman game where you try to guess a word by suggesting letters within a certain number of attempts. The game displays a hangman figure that gets progressively drawn as incorrect guesses are made.

### How It Works

1. **Introduction**: The game starts with a hangman ASCII art and a list of words.
2. **Word Selection**: A random word from the list is chosen.
3. **Guessing**: You are prompted to guess letters. Each correct guess fills in the blanks, while each incorrect guess progresses the hangman figure.
4. **Winning or Losing**: The game ends when you either guess the word correctly or the hangman figure is fully drawn.

### Hangman Stages

The hangman figure progresses through six stages:
1. No figure
2. Head
3. Head and torso
4. Head, torso, and arms
5. Head, torso, arms, and one leg
6. Full figure (Game Over)

### How to Run

1. Ensure Python is installed on your machine.
2. Copy the code into a file named `hangman_game.py`.
3. In the terminal, run:
   ```bash
   python hangman_game.py
