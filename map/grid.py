# map/grid.py
from abc import ABC, abstractmethod

class Grid(ABC):
    @abstractmethod
    def neighbors(self, coord):
        pass

    @abstractmethod
    def to_world(self, coord):
        """Convert grid coord → world/screen position"""
        pass
