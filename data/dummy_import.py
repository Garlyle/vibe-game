# io/dummy_import.py
from map.tile import Tile
from random import randint

class DummyImporter:
    def load(self):
        data = {}
        for q in range(-5, 6):
            for r in range(-5, 6):
                data[(q, r)] = Tile(
                    terrain="grass",
                    elevation=0,
                    passable=True,
                    cost=1+2*randint(1,3)
                )
        return data
