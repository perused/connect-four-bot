import os
import sys
from game import Game
import time

# asks if the user would like to start or not
def greeting():
    valid = False
 
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

# begins and runs the main game loop for the duration of the game
def start_game(game):

    os.system('cls' if os.name == 'nt' else 'clear')
    game.board.print_board()
    game_end = None

    while not game_end:

        game.next_move()
        os.system('cls' if os.name == 'nt' else 'clear')
        game.board.print_board()
        game_end = game.is_game_over(game.board.get_board())

    if game_end == "draw":
        print("Game over! It's a draw!")

    else:
        print(f"Game over! {game_end} wins!")

    return

# calls starter functions
def main():
    
    user_begins = greeting()
    game = Game(user_begins)
    start_game(game) 

# begins program
if __name__=="__main__":
    main()
