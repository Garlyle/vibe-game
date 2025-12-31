# Example file showing a basic pygame "game loop"
import pygame

from map.hexgrid import FlatTopHexGrid
from map.tilemap import TileMap
from data.dummy_import import DummyImporter
from render.pygame_render import PyGameRenderer

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

grid = FlatTopHexGrid(size=32)
tilemap = TileMap(grid)

importer = DummyImporter()
tilemap.tiles = importer.load()

renderer = PyGameRenderer(screen)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE
    for coord, tile in tilemap.tiles.items():
        pos = grid.to_world(coord)
        renderer.draw_tile(tile, pos)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
