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

class Tile:
    def __init__(self, x, y, tile_type="normal", cube_id=None):
        self.x = x
        self.y = y
        self.type = tile_type  # "normal" ou "portal"
        self.cube_id = cube_id
        self.keeper = None

class CubeNexus:
    """
    Représente un cube Nexus sous forme de croix (5 tuiles),
    dont une branche fait 2 tuiles et porte le portail.
    """
    # Disposition relative des tuiles (0,0) = centre
    # (dx, dy, role)
    RELATIVE_TILES = [
        (0, 0, "center"),      # centre
        (0, -1, "top"),       # haut
        (-1, 0, "left"),      # gauche
        (1, 0, "right"),      # droite
        (0, 1, "start"),      # bas 1 (départ)
        (0, 2, "portal")      # bas 2 (portail)
    ]

    def __init__(self, origin_x, origin_y, cube_id, custom_tiles=None):
        self.cube_id = cube_id
        self.tiles = []
        if custom_tiles is None:
            custom_tiles = {}
        for dx, dy, tile_role in self.RELATIVE_TILES:
            tile_type = custom_tiles.get(tile_role, tile_role if tile_role == "portal" else "normal")
            self.tiles.append(
                Tile(origin_x + dx, origin_y + dy, tile_type, cube_id)
            )
