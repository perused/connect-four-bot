import random
import time

class Bot:

    def __init__(self):
        pass

    def make_move(self, board):
        print("Hmm... computer thinking")
        # time.sleep(1)
        col = random.randint(0, 6)
        row = board.update_board(col, "O")
        return [col, row]
        
