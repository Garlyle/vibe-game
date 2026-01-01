# Example file showing a basic pygame "game loop"
import pygame

from map.hexgrid import FlatTopHexGrid
from map.tilemap import TileMap
from map.pathfinding import a_star
from data.dummy_import import DummyImporter
from render.pygame_render import PyGameRenderer
from render.camera import Camera

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

camera = Camera(offset=(screen_w // 2, screen_h // 2))
renderer = PyGameRenderer(grid, tilemap, TILE_SIZE)
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
                world_pos = camera.screen_to_world((mx, my))
                coord = grid.from_world(*world_pos)
                if not start:
                    start = coord
                else:
                    goal = coord
                    path = a_star(tilemap, start, goal)
            if event.button == 3:
                start = goal = path = None
            if event.button == 4:  # Mouse wheel up → zoom in
                camera.zoom_at(1.1, event.pos)
            if event.button == 5:  # Mouse wheel down → zoom out
                camera.zoom_at(0.9, event.pos)

    keys = pygame.key.get_pressed()
    pan_speed = 10
    if keys[pygame.K_a]:
        camera.offset.x += pan_speed
    if keys[pygame.K_d]:
        camera.offset.x -= pan_speed
    if keys[pygame.K_w]:
        camera.offset.y += pan_speed
    if keys[pygame.K_s]:
        camera.offset.y -= pan_speed

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE
    renderer.render(screen, camera)

    if start:
        renderer.draw_highlight(
            screen,
            camera,
            start,
            tilemap.get_tile(start),
            kind="start"
        )

    if goal:
        renderer.draw_highlight(
            screen,
            camera,
            goal,
            tilemap.get_tile(goal),
            kind="end"
        )

    if path:
        renderer.draw_path(screen, camera, path)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
