class Node:

    def __init__(self, board, col, parent, invalid_cols, moves_ahead):
        self.board = board
        self.col = col
        self.parent = parent
        self.invalid_cols = invalid_cols
        self.moves_ahead = moves_ahead

        self.heuristic = 0
        self.children = [] # append as you need, don't make moves in invalid columns

    def get_heuristic(self):
        return self.heuristic

    def get_col(self):
        return self.col

    def determine_heuristic(self):

        pass

    def generate_children(self):

        pass

