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

    
        # we only need to check for four in a row of the last person's turn
        if self.user_turn:
            symbol = "O"
        
        else:
            symbol = "X"

        # scenario 1: four in a row - only need to check the surroundings of last move

        # check row win
        if self.check_row_win(symbol):
            return symbol

        # check column win
        if self.check_column_win(symbol):
            return symbol

        # check left diagonal win
        if self.check_ldiag_win(symbol):
            return symbol

        # check right diagonal win
        if self.check_rdiag_win(symbol):
            return symbol

        # scenario 2: board is full
        if self.board.is_full():
            return "draw"

        return None

    def check_row_win(self, symbol):

        col = self.last_move[0]
        row = self.last_move[1]
        count = 0

        leftmost = max(0, col - 4)
        rightmost = min(6, col + 4)

        for i in range(leftmost, rightmost + 1):
            if self.board.board[row][i] == symbol:
                count += 1

            else:
                count = 0

            if count == 4:
                return True

        return False

    def check_column_win(self, symbol):

        col = self.last_move[0]
        row = self.last_move[1]
        count = 0

        lowmost = max(0, col - 4)
        topmost = min(5, col + 4)

        for i in range(lowmost, topmost + 1):
            if self.board.board[i][col] == symbol:
                count += 1

            else:
                count = 0

            if count == 4:
                return True

        return False
    
    def check_ldiag_win(self, symbol):
        
        return False

    def check_rdiag_win(self, symbol):
        
        return False