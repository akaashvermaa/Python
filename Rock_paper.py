import random

def rock_paper_scissors_game():
    """
    This function contains the main logic for the Rock, Paper, Scissors game.
    """
    
    # Define the possible choices for the game in a list.
    choices = ["rock", "paper", "scissors"]

    print("--- Welcome to Rock, Paper, Scissors! ---")
    
    # Get the player's choice.
    # We use .lower() to make the input case-insensitive (e.g., "Rock" becomes "rock").
    player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

    # --- Input Validation ---
    # Check if the player's choice is one of the valid options.
    # If not, inform the player and exit the function.
    if player_choice not in choices:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        return # Exit the function early

    # Get the computer's random choice from the list.
    computer_choice = random.choice(choices)

    # --- Display the choices ---
    print(f"\nYour choice: {player_choice}")
    print(f"Computer's choice: {computer_choice}\n")

    # --- Determine the winner ---

    # Case 1: It's a tie
    if player_choice == computer_choice:
        print("It's a tie! 🤝")
        
    # Case 2: Player wins
    # This block checks all the winning conditions for the player.
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        print("You win! �")
        
    # Case 3: If it's not a tie and the player didn't win, the computer must have won.
    else:
        print("You lose! 😢")

# This standard Python construct checks if the script is being run directly.
# If it is, it calls the main game function to start the game.
if __name__ == "__main__":
    rock_paper_scissors_game()
