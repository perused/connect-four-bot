import random
import time

class Bot:

    def __init__(self):
        pass

    def make_move(self, board):
        valid = False
        print("Hmm... bot thinking")
        time.sleep(1)
        
        while not valid:
            col = random.randint(0, 6)
            valid = board.is_valid_move(col)

        row = board.update_board(col, "O")
        return [col, row]
        
