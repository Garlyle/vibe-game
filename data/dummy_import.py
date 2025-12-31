# io/dummy_import.py
from map.tile import Tile

class DummyImporter:
    def load(self):
        data = {}
        for q in range(-5, 6):
            for r in range(-5, 6):
                data[(q, r)] = Tile(
                    terrain="grass",
                    elevation=0,
                    passable=True
                )
        return data
