class Board:

    def __init__(self):

        self.board = [
                [" ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " "]
                ]

    def get_board(self):
        return self.board

    # is a static function since various types of boards will be passed in rather than instances of boards
    def is_valid_move(board, column):

        # only one space needs to be free for it to be a valid move
        if board[0][column] == " ":
            return True

        return False

    def is_full(board):

        i = 0
        while i < len(board[0]):
            # if even one space in the top row is empty, board is not full
            if board[0][i] == " ":
                return False
            i += 1

        return True

    # returns y coordinate of the move to store as the last move
    def update_board(self, column, symbol):
        
        i = 5

        while i >= 0:

            if self.board[i][column] == " ":
                self.board[i][column] = symbol
                return i

            i -= 1

        print("Error in update board")

        return None

    def static_update_board(board, column, symbol):

        i = 5

        while i >= 0:

            if self.board[i][column] == " ":
                self.board[i][column] = symbol
                return i

            i -= 1

        print("Error in update board")

        return None


    def print_board(self):

        
        i = 0
        print("\n| 0 | 1 | 2 | 3 | 4 | 5 | 6 |")

        while i < len(self.board):

            j = 0

            while j < len(self.board[i]):

                print("| {} ".format(self.board[i][j]), end = "")
                j += 1

            i += 1
            print("|")

        print()

    def check_row_win(row, symbol, board):

        count = 0

        for i in range(7):
            if board[row][i] == symbol:
                count += 1

            else:
                count = 0

            if count == 4:
                return True

        return False

    def check_column_win(col, symbol, board):

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
    def check_ldiag_win(row, col, symbol, board):

        count = 0

        cur = Board.find_ldiag(row, col)

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
    def find_ldiag(row, col):

        while row > 0 and col > 0:
            row -= 1
            col -=1

        return [row, col]

    # right diagonal means the highest part of the diagonal is on the right hand side
    def check_rdiag_win(row, col, symbol, board):

        count = 0

        cur = Board.find_rdiag(row, col)

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
    def find_rdiag(row, col):

        while row > 0 and col < 6:
            row -= 1
            col +=1

        return [row, col]