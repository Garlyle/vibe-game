# render/pygame_render.py
import pygame
from render.renderer import Renderer

class PyGameRenderer(Renderer):
    def __init__(self, screen):
        self.screen = screen

    def draw_tile(self, tile, position):
        color = (0, 200, 0) if tile.passable else (200, 0, 0)
        pygame.draw.circle(self.screen, color, position, 10)
