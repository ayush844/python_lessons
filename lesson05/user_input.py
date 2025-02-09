import sys  # Imports the sys module to allow the program to exit using sys.exit().
import random  # Imports the random module to generate random choices for the computer.
from enum import Enum  # Imports the Enum class to create an enumeration for Rock, Paper, Scissors.

# Define an Enum class for the Rock-Paper-Scissors choices.
class RPS(Enum):
    ROCK = 1  # Assigns the value 1 to ROCK.
    PAPER = 2  # Assigns the value 2 to PAPER.
    SCISSORS = 3  # Assigns the value 3 to SCISSORS.

print("")  # Prints a blank line for better formatting.

# Prompts the user to enter their choice (1, 2, or 3) for Rock, Paper, or Scissors.
playerchoice = input(
    "Enter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")

player = int(playerchoice)  # Converts the player's input to an integer.

# Checks if the player's choice is valid (1, 2, or 3). If not, exits the program with a message.
if player < 1 or player > 3:
    sys.exit("You must enter 1, 2, or 3.")

# Generates a random choice for the computer from the string "123" (equivalent to 1, 2, 3).
computerchoice = random.choice("123")

computer = int(computerchoice)  # Converts the computer's choice to an integer.

print("")  # Prints a blank line for better formatting.

# Prints the player's choice, converting the integer to the corresponding RPS enum value and removing 'RPS.' for a clean output.
print("You chose " + str(RPS(player)).replace('RPS.', '') + ".")

# Prints the computer's choice in the same way as the player's choice.
print("Python chose " + str(RPS(computer)).replace('RPS.', '') + ".")

print("")  # Prints another blank line for formatting.

# Determines the winner based on the Rock-Paper-Scissors rules.
if player == 1 and computer == 3:  # Player wins: Rock beats Scissors.
    print("🎉 You win!")
elif player == 2 and computer == 1:  # Player wins: Paper beats Rock.
    print("🎉 You win!")
elif player == 3 and computer == 2:  # Player wins: Scissors beat Paper.
    print("🎉 You win!")
elif player == computer:  # It's a tie if both player and computer choose the same.
    print("😲 Tie game!")
else:  # If none of the above conditions are true, the computer wins.
    print("🐍 Python wins!")
