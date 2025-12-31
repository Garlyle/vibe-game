# map/tilemap.py
class TileMap:
    def __init__(self, grid):
        self.grid = grid
        self.tiles = {}  # (q, r) → Tile

    def set_tile(self, coord, tile):
        self.tiles[coord] = tile

    def get_tile(self, coord):
        return self.tiles.get(coord)
