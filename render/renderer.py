# render/renderer.py
from abc import ABC, abstractmethod

class Renderer(ABC):
    @abstractmethod
    def draw_tile(self, tile, position):
        pass
