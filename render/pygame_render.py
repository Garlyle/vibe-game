# render/pygame_render.py
import pygame
from render.renderer import Renderer
from map.hexutils import hex_vertices

class PyGameRenderer(Renderer):
    def __init__(self, screen, hex_size):
        self.screen = screen
        self.hex_size = hex_size

    def draw_tile(self, world_pos, tile):
        points = hex_vertices(world_pos, self.hex_size)

        fill = (0, 120, 0) if tile.passable else (120, 0, 0)
        outline = (200, 200, 200)

        pygame.draw.polygon(self.screen, fill, points)
        pygame.draw.polygon(self.screen, outline, points, width=1)

    def draw_path(self, grid, path):
        # convert each path coord into pixel center
        pts = [ grid.to_world(c) for c in path ]
        pygame.draw.lines(self.screen, (255, 255, 0), False, pts, width=3)
