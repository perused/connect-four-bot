import os
import sys
from game import Game
import time

def greeting():
    valid = False
 
    # print("Welcome to the connect four bot! The bot is a command line application that takes in a number from 0-6 to identify what the last move was, where 0 is the first column and 6 is the last column. Press 'q' at any time to quit. Would you like to start the game? (y/n)", end = " ")

    print("Would you like to start? (y/n)", end = " ")

    while not valid:
        starter = input()
        if "y" in starter and "n" not in starter:
            return True
        
        elif "n" in starter and "y" not in starter:
            return False

        elif "q" in starter:
            sys.exit()

        else:
            print("Please type y or n: ", end = "")

def start_game(game):

    os.system('cls' if os.name == 'nt' else 'clear')
    game.board.print_board()
    game_end = None

    while not game_end:

        game.next_move()
        os.system('cls' if os.name == 'nt' else 'clear')
        game.board.print_board()
        game_end = game.is_game_over()

    if game_end == "draw":
        print("Game over! It's a draw!")

    else:
        print(f"Game over! {game_end} wins!")

    return


def main():
    
    user_begins = greeting()
    game = Game(user_begins)
    start_game(game) 

if __name__=="__main__":
    main()
