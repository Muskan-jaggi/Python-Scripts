logo = """

 _____ _____ _____ _____ _____    _____ _____ _____ _____
|   __|  |  |   __|   __|   __|  |   __|  _  |     |   __|
|  |  |  |  |   __|__   |__   |  |  |  |     | | | |   __|
|_____|_____|_____|_____|_____|  |_____|__|__|_|_|_|_____|

"""
import random
print(logo)
print("welcome to the number guessing game!")
print("i m thinking of a number between 1 to 100.")

numbers = []
for i in range(1, 101):
    numbers.append(i)
choosen_number = random.choice(numbers)

def choose_difficulty():
    while True:
        difficulty = input("Choose difficulty (easy/hard): ").lower()
        if difficulty in ['easy', 'hard']:
            return difficulty
        else:
            print("Invalid input. Please choose either 'easy' or 'hard'.")

def set_attempts(difficulty):
    if difficulty == 'easy':
        return 11
    elif difficulty == 'hard':
        return 7
    
difficulty = choose_difficulty()
attempts = set_attempts(difficulty)

def attempts_left():
    global choosen_number
    global attempts  # Access the global variable
    attempts -= 1
    print(f"you have {attempts} attempts left")

def compare_guess(guess):
    global attempts
    global choosen_number
    if attempts == 1:
        print("you have 0 attempts left!")
        print(f"you lose! the correct answer was {choosen_number}")
        return
    if guess == choosen_number:
        print(f"you got it! the answer was {choosen_number}")
    elif guess > choosen_number and attempts > 0:
        print("too high")
        print("Guess again")
        make_guess()
    elif guess < choosen_number and attempts>0:
        print("too low")
        print("Guess again")
        make_guess()
    
def make_guess():
    attempts_left()
    guess = int(input("make a guess: "))
    return compare_guess(guess)
make_guess()

    
   
