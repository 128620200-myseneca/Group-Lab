#!/usr/bin/env python3
import random
''''
The traditional "Rock paper and scissors" game was developed in Python.
The user must fight the computer in the game's single player mode.

The program prompts the user to choose between rock-paper-scissors options. 

Then the computer also randomly selects a selection for itself. The software will then decide who is the winner according to the rules of the game.

There are no complicated features or graphical user interfaces in this software.



August 5, 2023

'''' 
options = ("rock", "paper", "scissors") # list of options for the computer
computer = random.choice(options) # This will choose a random option from your list for the computer