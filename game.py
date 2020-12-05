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

    def is_game_over(self, board):

    
        # we only need to check for four in a row of the last person's turn
        if self.user_turn:
            symbol = "O"
        
        else:
            symbol = "X"

        # scenario 1: four in a row - only need to check the surroundings of last move

        # check row win
        if self.check_row_win(symbol, board):
            return symbol

        # check column win
        if self.check_column_win(symbol, board):
            return symbol

        # check left diagonal win
        if self.check_ldiag_win(symbol, board):
            return symbol

        # check right diagonal win
        if self.check_rdiag_win(symbol, board):
            return symbol

        # scenario 2: board is full
        if Board.is_full(board):
            return "draw"

        return None

    def check_row_win(self, symbol, board):

        row = self.last_move[1]
        count = 0

        for i in range(7):
            if board[row][i] == symbol:
                count += 1

            else:
                count = 0

            if count == 4:
                return True

        return False

    def check_column_win(self, symbol, board):

        col = self.last_move[0]
        count = 0

        for i in range(6):
            if board[i][col] == symbol:
                count += 1

            else:
                count = 0

            if count == 4:
                return True

        return False
    
    # left diagonal means the highest part of the diagonal is on the left hand side
    def check_ldiag_win(self, symbol, board):

        row = self.last_move[1]
        col = self.last_move[0]
        count = 0

        cur = self.find_ldiag(row, col)

        while cur[0] <= 5 and cur[1] <= 6:

            row = cur[0]
            col = cur[1]

            if board[row][col] == symbol:
                count += 1

            else:
                count = 0

            if count == 4:
                return True

            cur[0] += 1
            cur[1] += 1

        return False

    # finds the highest diagonally left point from the given coordinates
    def find_ldiag(self, row, col):

        while row > 0 and col > 0:
            row -= 1
            col -=1

        return [row, col]

    # right diagonal means the highest part of the diagonal is on the right hand side
    def check_rdiag_win(self, symbol, board):

        row = self.last_move[1]
        col = self.last_move[0]
        count = 0

        cur = self.find_rdiag(row, col)

        while cur[0] <= 5 and cur[1] >= 0:

            row = cur[0]
            col = cur[1]

            if board[row][col] == symbol:
                count += 1

            else:
                count = 0

            if count == 4:
                return True

            cur[0] += 1
            cur[1] -= 1

        return False
    
    # finds the highest diagonally right point from the given coordinates
    def find_rdiag(self, row, col):

        while row > 0 and col < 6:
            row -= 1
            col +=1

        return [row, col]