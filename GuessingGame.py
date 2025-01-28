# Name: Daniel Momoh
# student ID: 041114358
# Date: 2021-10-10
# Lab 4 : Guessing Game
import random

def main():
# Controls the game flow.
    playing = True
    while playing:
        print("Welcome to the Guessing Game!")
        play_choice = input("Do you want to play? (yes/no): ").lower()
        if play_choice == "yes":
            play()
        else:
            print("Goodbye!")
            playing = False
def play():
    secret_number = random.randint(1, 100)
    attempts = 5

    print("I'm thinking of a number between 1 and 100.")

    while attempts > 0:
        guess = integer_input(1, 100, "Enter your guess: ")

        if guess == secret_number:
            print("Congratulations! You guessed the number!")
            return 
        elif guess < secret_number:
            print("Your guess is too low! Try again.")
        else:
            print("Your guess is too high! Try again.")

        attempts -= 1

    print(f"Sorry, you've used all your guesses. The secret number was {secret_number}.")

def integer_input(min_value, max_value, message):

    while True:
        try:
            user_input = int(input(message))
            if min_value <= user_input <= max_value:
                return user_input
            else:
                print(f"Please enter a number between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()