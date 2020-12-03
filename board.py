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

    def is_valid_move(self, column):
        
        # only one space needs to be free for it to be a valid move
        if self.board[0][column] == " ":
            return True

        return False

    def is_full(self):

        i = 0
        while i < len(self.board[0]):
            # if even one space in the top row is empty, board is not full
            if self.board[0][i] == " ":
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
