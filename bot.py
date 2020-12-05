import random
import time
from board import Board

from node import Node

class Bot:

    def __init__(self):
        pass

    # def get_move(self, board):

    #     valid = False
    #     print("Hmm... bot thinking")
    #     time.sleep(1)
        
    #     while not valid:
    #         col = random.randint(0, 6)
    #         valid = Board.is_valid_move(board, col)

    #     return col

    def get_move(self, board):

        valid_cols = []
        invalid_cols = []

        for col in range(7):
            if Board.is_valid_move(board, col):
                valid_cols.append(col)
            else:
                invalid_cols.append(col)
        
        children = []

        for col in valid_cols:
            node = Node(board, col, None, invalid_cols, 0)
            children.append(node)

        best = children[0]

        for node in children:
            if node.get_heuristic() > best.get_heuristic():
                best = node

        return best.get_col()
