# Example file showing a basic pygame "game loop"
import pygame

from map.hexgrid import FlatTopHexGrid
from map.tilemap import TileMap
from map.pathfinding import a_star
from data.dummy_import import DummyImporter
from render.pygame_render import PyGameRenderer

TILE_SIZE = 32
start = (0,0)
goal = (2,3)

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

screen_w, screen_h = screen.get_size()

grid = FlatTopHexGrid(
    size=TILE_SIZE,
    origin=(screen_w // 2, screen_h // 2)
)
tilemap = TileMap(grid)

importer = DummyImporter()
tilemap.tiles = importer.load()

renderer = PyGameRenderer(screen, TILE_SIZE)
path = a_star(tilemap, start, goal)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mx, my = event.pos
                coord = grid.from_world(mx, my)
                if not start:
                    start = coord
                else:
                    goal = coord
                    path = a_star(tilemap, start, goal)
            if event.button == 3:
                start = goal = path = None

    keys = pygame.key.get_pressed()
    pan_speed = 10
    if keys[pygame.K_LEFT]:
        grid.origin = (grid.origin[0] + pan_speed, grid.origin[1])
    if keys[pygame.K_RIGHT]:
        grid.origin = (grid.origin[0] - pan_speed, grid.origin[1])
    if keys[pygame.K_UP]:
        grid.origin = (grid.origin[0], grid.origin[1] + pan_speed)
    if keys[pygame.K_DOWN]:
        grid.origin = (grid.origin[0], grid.origin[1] - pan_speed)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE
    for coord, tile in tilemap.tiles.items():
        pos = grid.to_world(coord)
        renderer.draw_tile(pos, tile)

    # Draw highlighted start/end tiles
    if start:
        renderer.draw_tile(grid.to_world(start), tilemap.get_tile(start), highlight="start")
    if goal:
        renderer.draw_tile(grid.to_world(goal), tilemap.get_tile(goal), highlight="end")
    
    # draw search path (if exists)
    if path:
        renderer.draw_path(grid, path)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
