from board import Board

class Bot:

    def __init__(self, board, user_starts):

        if user_starts:
            self.request_move(board)

        else:
            self.make_move(board)

    def request_move(self, board):
        print("User makes move now")

    def make_move(self, board):
        print("Computer makes move now")
