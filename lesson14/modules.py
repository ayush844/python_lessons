# Importing specific constants and functions from modules

from math import pi  # Importing the mathematical constant 'pi' from the built-in 'math' module

import sys  # Importing the 'sys' module, which provides system-specific functions and parameters

import random as rdm  # Importing the 'random' module and renaming it to 'rdm' for shorter usage

from enum import Enum  # Importing 'Enum' from the 'enum' module, used to create enumerations

import kansas  # Importing a custom module named 'kansas'

from rps7 import rock_paper_scissors  # Importing the 'rock_paper_scissors' function from a module named 'rps7'

# Printing the value of pi (mathematical constant)
print(pi)  # Output: 3.141592653589793

# Listing all attributes and functions available in the 'random' module
# Uncommenting the following lines will print all available functions inside the 'random' module
# for item in dir(rdm):
#     print(item)

# Accessing and printing a variable from the 'kansas' module
print(kansas.capital)  # Output: Topeka

# Calling a function from the 'kansas' module
kansas.randomfunfact()  
# Output: A random fact about Kansas, e.g., "Wichita is the largest city in the state, but many would guess that it is Kansas City."

# Printing the special __name__ variable
# '__name__' is a built-in variable in Python that represents the name of the module currently being executed.
# If the script is being run directly, '__name__' will be '__main__'.
print(__name__)  # Output: __main__

# Printing the __name__ attribute of the 'kansas' module
# When a module is imported, its '__name__' will be the module's actual name.
print(kansas.__name__)  # Output: kansas

# Calling the 'rock_paper_scissors' function from the 'rps7' module
rock_paper_scissors()  
# This function starts a game of Rock, Paper, Scissors.
# The function will prompt the user for input, generate a random move for Python, and determine the winner.

# Sample output from 'rock_paper_scissors()' function:
# Enter... 
# 1 for Rock,
# 2 for Paper, or 
# 3 for Scissors:
# 
# 3
# 
# You chose Scissors.
# Python chose Scissors.
# 
# 😲 Tie game!
# 
# Game count: 1
# 
# Player wins: 0
# 
# Python wins: 0
# 
# Play again?
# 
# Y for Yes or 
# Q to Quit
# q
# 
# 🎉🎉🎉🎉
# Thank you for playing!
# 
# Bye! 👋
