## Number Guessing Game 🎲

This is a Python-based number guessing game where the player has to guess a randomly chosen number between 1 and 100. The game allows the player to choose the difficulty level, which determines the number of attempts allowed.

### How It Works

1. **Welcome Message**: The game prints a welcome message and informs the player that a number between 1 and 100 is being chosen.
2. **Choose Difficulty**: The player selects the difficulty level (`easy` or `hard`), which affects the number of attempts allowed:
   - **Easy**: 11 attempts
   - **Hard**: 7 attempts
3. **Make a Guess**: The player makes guesses until they either guess the number correctly or run out of attempts.
4. **Feedback**: After each guess, the game provides feedback whether the guess is too high or too low, and informs the player of the number of attempts left.
5. **End of Game**: The game ends when the player guesses the number correctly or exhausts all attempts.

### How to Run

1. Make sure Python is installed.
2. Copy the code into a file named `number_guessing_game.py`.
3. In the terminal, run:
   ```bash
   python number_guessing_game.py
