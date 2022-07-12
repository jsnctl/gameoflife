from core import game


class Controller:
    def __init__(self):
        self.board = None


    def create_board(self, width, height):
        self.board = game.Board(width, height)
        return self.board
