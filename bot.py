import random
import time
from board import Board

class Bot:

    def __init__(self):
        pass

    def get_move(self, board):

        valid = False
        print("Hmm... bot thinking")
        time.sleep(1)
        
        while not valid:
            col = random.randint(0, 6)
            valid = Board.is_valid_move(board, col)

        return col
        
