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
                    
                    if not Board.is_valid_move(self.board.get_board(), move):
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
            self.last_move[0] = self.bot.get_move(self.board.get_board())
            self.last_move[1] = self.board.update_board(self.last_move[0], "O")
            self.user_turn = True
            return

    # symbol of the player who just had their turn
    def is_game_over(self, board):

    
        # we only need to check for four in a row of the last person's turn
        if self.user_turn:
            symbol = "O"
        
        else:
            symbol = "X"

        # scenario 1: four in a row - only need to check the surroundings of last move
        row = self.last_move[1]
        col = self.last_move[0]

        # check row win
        if Board.check_row_win(row, symbol, board):
            return symbol

        # check column win
        if Board.check_column_win(col, symbol, board):
            return symbol

        # check left diagonal win
        if Board.check_ldiag_win(row, col, symbol, board):
            return symbol

        # check right diagonal win
        if Board.check_rdiag_win(row, col, symbol, board):
            return symbol

        # scenario 2: board is full
        if Board.is_full(board):
            return "draw"

        return None