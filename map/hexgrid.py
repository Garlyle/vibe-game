# map/hexgrid.py
from map.grid import Grid
from map.hexutils import neighbors as hex_neighbors
from map.hexutils import axial_to_pixel, pixel_to_axial, hex_round
import math

class FlatTopHexGrid(Grid):
    def __init__(self, size, origin=(0, 0)):
        self.size = size

    def neighbors(self, coord):
        return hex_neighbors(coord)

    def to_world(self, coord):
        return axial_to_pixel(*coord, self.size)

    def from_world(self, x, y):
        q, r = pixel_to_axial(x, y, self.size)
        return hex_round(q, r)
