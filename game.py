from board import Board
from bot import Bot
import sys

class Game:
    def __init__(self, user_turn):
        self.game_over = False
        self.user_turn = user_turn
        self.board = Board()
        self.bot = Bot()
        self.last_move = [None, None] # x, y

    def next_move(self):

        if self.user_turn:
            valid = False

            while not valid:
                try:
                    move = int(input("Your turn: "))
                    
                    if move < 0 or move > 6:
                        raise Exception
                    
                    if not self.board.is_valid_move(move):
                        raise Exception

                    # update last move coordinates and move on the board
                    self.last_move[0] = move
                    self.last_move[1] = self.board.update_board(move, "X")
                    self.user_turn = False
                    valid = True
                    return

                except KeyboardInterrupt:
                    sys.exit()

                except:
                    print("Invalid. Please enter 0-6 in available column.")
            
        else:
            self.last_move = self.bot.make_move(self.board)
            self.user_turn = True
            return

    def is_game_over(self):
        
        # scenario 1: four in a row - only need to check the surroundings of last move


        # scenario 2: board is full
        if self.board.is_full():
            print("The board is full! It's a draw!")
            return True

        return False