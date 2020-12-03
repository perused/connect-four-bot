from board import Board
from bot import Bot
import sys

class Game:
    def __init__(self, user_turn):
        self.game_over = False
        self.user_turn = user_turn
        self.board = Board()
        self.bot = Bot()

    def is_game_over(self):
        pass

    def next_move(self):

        if self.user_turn:
            valid = False

            while not valid:
                try:
                    move = int(input("Your turn: "))
                    
                    if move < 0 or move > 6:
                        assert False
                    
                    valid = True

                    if not self.board.is_valid_move(move):
                        assert False

                    self.board.update_board(move, "X")
                    self.user_turn = False

                except KeyboardInterrupt:
                    sys.exit()

                except:
                    print("Invalid. Please enter 0-6 in available column.")
            
        else:
            self.bot.make_move(self.board)
            self.user_turn = True