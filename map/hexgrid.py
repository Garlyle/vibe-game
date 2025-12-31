# map/hexgrid.py
from map.grid import Grid
from map.hexutils import neighbors as hex_neighbors
from map.hexutils import axial_to_pixel, pixel_to_axial, hex_round
import math

class FlatTopHexGrid(Grid):
    def __init__(self, size, origin=(0, 0)):
        self.size = size
        self.origin = origin

    def neighbors(self, coord):
        return hex_neighbors(coord)

    def to_world(self, coord):
        x, y = axial_to_pixel(*coord, self.size)
        ox, oy = self.origin
        return x + ox, y + oy

    def from_world(self, x, y):
        ox, oy = self.origin
        q, r = pixel_to_axial(x - ox, y - oy, self.size)
        return hex_round(q, r)
