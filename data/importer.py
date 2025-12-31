# io/importer.py
from abc import ABC, abstractmethod

class TileMapImporter(ABC):
    @abstractmethod
    def load(self) -> dict:
        pass
