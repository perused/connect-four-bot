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

        print("Hmm... bot thinking")
        time.sleep(1)

        # first check which columns are valid and invalid
        valid_cols = []
        invalid_cols = []

        for col in range(7):
            if Board.is_valid_move(board, col):
                valid_cols.append(col)
            else:
                invalid_cols.append(col)

        # moves by value go in this order:
        # 1. getting four in a row on this move
        move = self.can_win_now(board, valid_cols)

        if move:
            return move

        # 2. blocking the other player from getting 4 in a row on their next move
        move = self.can_block_player(board, valid_cols)

        if move:
            return move

        # 3. need more information to decide what comes next (idea: assuming the player makes the next best move, by our own heuristic measure, we then update the board through that and then make a decision based on that in order to get more information) - i suppose the heuristic would be made up of whether we can a) win and b) block the other player
        # 4. repeat step 3, but for all these possibilities, and so on

        # below code is just a random idea, probably not modular enough but will use the concept
        
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
    def can_win_now(self, board, valid_cols):
        
        for col in valid_cols:
            row = Board.static_update_board(board, col, "O")

            if Board.check_row_win(row, "O", board) or Board.check_column_win(col, "O", board) or Board.check_ldiag_win(row, col, "O", board) or Board.check_rdiag_win(row, col, "O", board):
                board[row][col] = " "
                return col
            
            else:
                board[row][col] = " "

        return None

    def can_block_player(self, board, valid_cols):

        for col in valid_cols:
            row = Board.static_update_board(board, col, "X")

            if Board.check_row_win(row, "X", board) or Board.check_column_win(col, "X", board) or Board.check_ldiag_win(row, col, "X", board) or Board.check_rdiag_win(row, col, "X", board):
                board[row][col] = " "
                return col

            else:
                board[row][col] = " "

        return None