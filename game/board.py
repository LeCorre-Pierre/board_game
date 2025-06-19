# Plateau de jeu (Board)
class Board:
    def __init__(self, width=5, height=5):
        self.width = width
        self.height = height
        self.tiles = [[None for _ in range(width)] for _ in range(height)]

    def place_keeper(self, keeper, x, y):
        self.tiles[y][x] = keeper
        keeper.x = x
        keeper.y = y

    def move_keeper(self, keeper, new_x, new_y):
        self.tiles[keeper.y][keeper.x] = None
        self.tiles[new_y][new_x] = keeper
        keeper.x = new_x
        keeper.y = new_y
