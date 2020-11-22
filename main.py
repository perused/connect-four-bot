import os
import sys
from game import Game

def greeting():
    valid = False
 
    print("Welcome to the connect four bot! The bot is a command line application that takes in a number from 0-6 to identify what the last move was, where 0 is the first column and 6 is the last column. Press 'q' at any time to quit. Would you like to start the game? (y/n)", end = " ")

    while not valid:
        starter = input()
        if "y" in starter and "n" not in starter:
            return True
        
        elif "n" in starter and "y" not in starter:
            return False

        elif "q" in starter:
            sys.exit()

        else:
            print("Invalid input, please type y or n to indicate if you would like to start: ", end = "")

def start_game(game):

    game.board.print_board()

def main():
    
    user_begins = greeting()
    game = Game(user_begins)
    start_game(game) 

if __name__=="__main__":
    main()
