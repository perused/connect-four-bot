import random
import time
from board import Board

from node import Node

class Bot:

    def __init__(self):
        pass

    # bot makes a random move next
    def random_move(self, board):

        valid = False
        print("Hmm... bot thinking")
        time.sleep(1)
        
        while not valid:
            col = random.randint(0, 6)
            valid = Board.is_valid_move(board, col)

        return col

    # bot determines the next best move to make
    def get_move(self, board):

        # moves by value go in this order:
        # 1. getting four in a row on this move
        move = self.can_win_now(board)

        if move:
            return move

        # 2. blocking the other player from getting 4 in a row on their next move


        # 3. need more information to decide what comes next (idea: assuming the player makes the next best move, by our own heuristic measure, we then update the board through that and then make a decision based on that in order to get more information)


        # 4. repeat step 3, but for all these possibilities

        # below code is just a random idea, probably not modular enough but will use the concept

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

    # if we can win on the next turn we make, we will do this move straight away
    def can_win_now(self, board):
        
        original_board = board.copy()

        for col in range(7):
            game_end = 

        return None