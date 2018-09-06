#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = "Sayan Mukherjee"
__version__ = "0.1.0"
__license__ = "MIT"

from random import choice

'''
Messages are global so that they 
can be easily modified and re-used.
'''
MSG_ERROR = "Please enter a valid choice."
MSG_START = "Please choose 'R' for Rock, 'P' for Paper, 'S' for Scissors or 'Q' to quit:"
MSG_THANKS = "Thank you for playing!"

moves = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
rules = {
    'r': {'r': 2, 'p': 0, 's': 1},
    'p': {'r': 1, 'p': 2, 's': 0},
    's': {'r': 0, 'p': 1, 's': 2}
    }

def main():
    """ Main entry point of the app """
    collectUserInput()

def collectUserInput():
    """ Collects user input from console and verifies it is a letter before proceeding """
    user_input = input(MSG_START).lower()
    
    while user_input != 'q':
        initGame(user_input)
        user_input = input(MSG_START).lower()
        
    print(MSG_THANKS)

def initGame(user_input):
    """ Starts the Rock, Paper, Scissors game """
    if user_input == "r" or user_input == "p" or user_input == "s":
        playGame(user_input)
    else:
        print(MSG_ERROR)

def getComputerMove():
    """ Randomly returns either r/p/s """
    return choice(['r', 'p', 's'])

def playGame(user_choice):
    ''' Applies the game rules and declares game result ''' 
    print("You played", moves[user_choice])
    computer_move = getComputerMove()
    print("Computer played", moves[computer_move])
    
    result = rules[user_choice][computer_move]
    if result == 2: # Number 2 denotes Tie
        print("The game is tied!")
    elif result == 0: # Number 0 denotes loss for player
        print("Computer wins!")
    elif result == 1: # Number 1 denotes win for player
        print("Congratulations! You win.")

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
