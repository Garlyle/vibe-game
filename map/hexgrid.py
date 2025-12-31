# map/hexgrid.py
from map.grid import Grid
from map.hexutils import neighbors as hex_neighbors
import math

class FlatTopHexGrid(Grid):
    def __init__(self, size):
        self.size = size

    def neighbors(self, coord):
        return hex_neighbors(coord)

    def to_world(self, coord):
        q, r = coord
        x = self.size * (3/2 * q)
        y = self.size * (math.sqrt(3) * (r + q/2))
        return (x, y)
