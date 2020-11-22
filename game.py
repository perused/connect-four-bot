from board import Board
from bot import Bot

class Game:
    def __init__(self, user_turn):
        self.game_over = False
        self.user_turn = user_turn
        self.board = Board()
        self.bot = Bot()

    def is_game_over(self):
        pass

    def request_player_move(self):
        
        print("Player makes move now")

        self.user_turn = False

        return 