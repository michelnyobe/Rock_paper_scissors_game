"""Import Libraries"""
import random
import time
import os
import getpass

# Define a list of choices
choises = ["rock", "paper", "scissors"]

# Defining a function to check if the user input is valid


def verify_input(answer):
    """verifying the user input

    Args:
        answer (Str):The user input to check. 

    Returns:
        bool: True if the entry is valid, False otherwise.
    """
    if answer.lower() in choises:
        return True
    return False

# Defining a function to check if the user wins


def winning_answers(answer1, answer2):
    """Determines if Player 1 wins based on their answer choices.

    Args:
        answer1 (Str): Player 2's answer choice.
        answer2 (Str): Player 2's answer choice.

    Returns:
        bool: True if player 1 wins, False otherwise
    """
    if answer1 == "rock" and answer2 == "scissors":

        return True

    if answer1 == "paper" and answer2 == "rock":
        return True

    if answer1 == "scissors" and answer2 == "paper":

        return True
    return False


def anime(answer1, answer2):
    """Check if the answers of both players are the same.

    Args:
        answer1 (Str): Player 1's response.
        answer2 (Str): Player 2's response.

    Returns:
        bool or None: True if the answers are identical, otherwise None.
    """
    if answer1 == answer2:

        return True
    return None


# Clearing the console and printing the game title
def clean_console():
    """Clears the console depending on the operating system."""
    os.system("cls" if os.name == "nt" else "clear")

def play_game_pc():
    """Allows one player to play against the computer at rock-paper-scissors

    This function starts a game where the player enters his choice (rock, paper
    or scissors), then the computer randomly chooses between the same options.
    The result is displayed to the user and the game offers to replay or
    to leave.
    """
    # Setting a flag for the game loop
    running = True

    # Game loop
    while running:

        # Asking the user for their choice
        print(" type your choice: ")

        player_answer = input().strip().lower()

        change = True

        # Validating the user input
        while change:
            if not verify_input(player_answer):

                print("not a valid option, expecting: ",
                    choises[0], choises[1], "or", choises[2])

                player_answer = input().strip()

            else:

                change = False

        # Printing the user choice
        print("you choose: ", player_answer)

        # Adding a delay before revealing the computer choice
        time.sleep(0.5)
        print("computer is thinking...")
        time.sleep(1)

        # Generating a random choice for the computer
        pc_answer = random.choice(choises)

        # Printing the computer choice
        print("computer choose: ", pc_answer)
        print('\n')

        # Checking if the game is a tie
        if anime(player_answer, pc_answer):
            print("IT'S A TIE!!!")

        # Checking if the user wins
        if winning_answers(player_answer, pc_answer) is True:
            print(player_answer, " beats ", pc_answer)
            print("YOU WIN!!!")

        # Checking if the user loses
        elif not winning_answers(player_answer, pc_answer) and not anime(player_answer, pc_answer):
            print(pc_answer, " beats ", player_answer)
            print("YOU LOOSE!, ")
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

def play_game_users():
    """
    Function allowing two players to play rock-paper-scissors.
   
    This function prompts both players to enter their choice (rock, paper or
    scissors). Then it determines the winner and displays the result. The game
    also offers to replay or quit after each game.
    """
    # Starts an infinite loop to allow players to play multiple rounds
    while True:
        # Prompts player 1 to enter their choice while hiding their input
        player1 = getpass.getpass("Player 1, enter your choice").lower().strip()
        while player1 not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please enter rock, paper, or scissors.")
            player1 = getpass.getpass("Player 1, enter your choice:").lower().strip()

        player2 = getpass.getpass("Player 2, enter your choice: ").lower()
        while player2 not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please enter rock, paper, or scissors.")
            player2 = getpass.getpass("Player 2, enter your choice: ").lower().strip()
        if anime(player1, player2):
            print("IT'S A TIE!!!")

        winner = winning_answers(player1, player2)
        if winner is True:  # Checks if player 1 wins
            print("Player 1 wins!")
        elif not winning_answers(player1, player2) and not anime(player1, player2):
            print("Player 2 wins!")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes': # Checks if players want to stop playing
            break

    print("Thanks for playing!") # Displays a thank you message at the end of the game

def display_rules():
    """Displays the rules of the game.

    This function prints out the rules of the game, explaining how it works.
    It describes the process of making choices between rock, paper, and scissors,
    how the winner is determined, and what happens in the case of a tie.
    Additionally, it outlines the hierarchy of choices where rock beats scissors,
    scissors beats paper, and paper beats rock."""

    print("The game works as the following:")
    print("When the game is launched, it ask you")
    print("which make choice between rock, paper, and scissors")
    print("The computer will then make a choice and the winner will be displayed")
    print("If both of you choose the same thing, it's a tie")
    print("Rock beats scissors, scissors beats paper, and paper beats rock")
    print("\n")


def main():
    """
    Main function to run the Rock, Paper, Scissors game.

    This function serves as the main entry point for the Rock, Paper, Scissors game.
    It displays a menu where the user can choose to play against the computer,
    play against another player, display the rules of the game, or quit the game.
    The function then calls the appropriate sub-functions based on the user's choice.
    The loop continues until the user chooses to quit the game."""

    clean_console() # Clears the console before displaying the menu
    while True: # Starts an infinite loop to keep the game running until the user chooses to quit
        print("# Welcome to Rock, Paper, Scissors! #\n")
        # Displaying the menu options
        print("\nMenu:")
        print("1. Play against the computer")
        print("2. Play against another player")
        print("3. Display rules")
        print("4. Quit")
         # Prompting the user to enter their choice
        choice = input("Enter your choice (1-4): ").strip()
        # Processing the user's choice
        if choice == '1':
            play_game_pc()
        elif choice == '2':
            play_game_users()
        elif choice == '3':
            display_rules()
        elif choice == '4':
            print("Goodbye!")
            break
        else: # If the user enters an invalid choice
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
