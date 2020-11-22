class Board:

    def __init__(self):

        self.board = [
                [None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None]
                ]

    def print_board(self):

        
        i = 0
        print()

        while i < len(self.board):

            j = 0

            while j < len(self.board[i]):

                print("| {} ".format(self.board[i][j]), end = "")
                j += 1

            i += 1
            print("|")

        print()
