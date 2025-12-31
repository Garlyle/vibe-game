# map/hexgrid.py
from map.grid import Grid
import math

class FlatTopHexGrid(Grid):
    def __init__(self, size):
        self.size = size

    def neighbors(self, coord):
        q, r = coord
        directions = [(1,0), (1,-1), (0,-1), (-1,0), (-1,1), (0,1)]
        return [(q+dq, r+dr) for dq, dr in directions]

    def to_world(self, coord):
        q, r = coord
        x = self.size * (3/2 * q)
        y = self.size * (math.sqrt(3) * (r + q/2))
        return (x, y)
