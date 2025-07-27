import random

def guess_the_number_game():
   
    secret_number = random.randint(1, 100)
    
    guess_count = 0
    player_guess = 0

    print("-------Welcome to Number Guessing Game!!!-------")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess what it is?")

    
    while player_guess != secret_number:
        try:
            player_guess_input = input("Enter your Guess: ")
            player_guess = int(player_guess_input)
            guess_count += 1
            
            # --- CORRECTED: The if/elif/else block now has proper alignment ---
            if player_guess < secret_number:
                print("Too Low!! Try a Higher Number.")
            elif player_guess > secret_number:
                print("Too High!!! Try a smaller number.")
            else:
                print(f"\nCongratulations! You guessed the right number.")
                print(f"The secret number was {secret_number}.")
                print(f"It took you {guess_count} guesses.")

        # --- CORRECTED: The 'except' now lines up with the 'try' ---
        except ValueError:
            print("Oops! That's not a valid number. Please enter an integer.")


if __name__ == "__main__":
    guess_the_number_game()
