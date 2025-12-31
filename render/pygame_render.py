# render/pygame_render.py
import pygame
from render.renderer import Renderer
from map.hexutils import hex_vertices

class PyGameRenderer(Renderer):
    def __init__(self, screen, hex_size):
        self.screen = screen
        self.hex_size = hex_size

    def draw_tile(self, world_pos, tile, highlight=None):
        points = hex_vertices(world_pos, self.hex_size)

        # tile fill
        fill = (min(255, tile.cost * 40), 120, 0) if tile.passable else (120, 0, 0)
        pygame.draw.polygon(self.screen, fill, points)

        # highlight for start/end
        if highlight == "start":
            pygame.draw.polygon(self.screen, (0, 255, 0), points, width=3)
        elif highlight == "end":
            pygame.draw.polygon(self.screen, (255, 0, 0), points, width=3)
        else:
            pygame.draw.polygon(self.screen, (200, 200, 200), points, width=1)

    def draw_path(self, grid, path):
        # convert each path coord into pixel center
        pts = [ grid.to_world(c) for c in path ]
        pygame.draw.lines(self.screen, (255, 255, 0), False, pts, width=3)
