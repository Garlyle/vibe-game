# map/tile.py
from dataclasses import dataclass

@dataclass
class Tile:
    terrain: str
    elevation: int
    passable: bool
