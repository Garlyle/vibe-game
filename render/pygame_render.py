# render/pygame_render.py
import pygame
from render.renderer import Renderer
from map.hexutils import hex_vertices

class PyGameRenderer(Renderer):
    def __init__(self, grid, tilemap, hex_size):
        self.grid = grid
        self.tilemap = tilemap
        self.hex_size = hex_size

        self.grid_surface = None
        self.dirty = True  # re-render when tiles change

    def build_grid_surface(self):
        # Compute bounds in world space
        coords = self.tilemap.tiles.keys()
        positions = [self.grid.to_world(c) for c in coords]

        xs = [p[0] for p in positions]
        ys = [p[1] for p in positions]

        padding = self.hex_size * 2
        min_x, max_x = min(xs) - padding, max(xs) + padding
        min_y, max_y = min(ys) - padding, max(ys) + padding

        width = int(max_x - min_x)
        height = int(max_y - min_y)

        surface = pygame.Surface((width, height), pygame.SRCALPHA)
        surface.fill((0, 0, 0, 0))

        for coord, tile in self.tilemap.tiles.items():
            world_pos = self.grid.to_world(coord)
            local_pos = (world_pos[0] - min_x, world_pos[1] - min_y)
            self.draw_tile(surface, local_pos, tile)

        self.grid_surface = surface
        self.grid_origin = pygame.Vector2(min_x, min_y)
        self.dirty = False

    def draw_tile(self, surface, world_pos, tile):
        points = hex_vertices(world_pos, self.hex_size)
        fill = (min(255, tile.cost * 40), 120, 0) if tile.passable else (120, 0, 0)
        pygame.draw.polygon(surface, fill, points)
        pygame.draw.polygon(surface, (200, 200, 200), points, width=1)

    def render(self, screen, camera):
        if self.dirty:
            self.build_grid_surface()

        # Scale the grid surface according to camera zoom
        if camera.zoom != 1.0:
            scaled_size = (
                int(self.grid_surface.get_width() * camera.zoom),
                int(self.grid_surface.get_height() * camera.zoom)
            )
            scaled_surface = pygame.transform.smoothscale(self.grid_surface, scaled_size)
        else:
            scaled_surface = self.grid_surface

        # Apply camera offset
        screen_pos = camera.world_to_screen(self.grid_origin)
        screen.blit(scaled_surface, screen_pos)


    def draw_path(self, screen, camera, path):
        pts = [camera.world_to_screen(self.grid.to_world(c)) for c in path]
        pygame.draw.lines(screen, (255, 255, 0), False, pts, 3)

    def draw_highlight(self, screen, camera, coord, tile, kind):
        world_pos = self.grid.to_world(coord)
        screen_pos = camera.world_to_screen(world_pos)

        points = hex_vertices(screen_pos, self.hex_size * camera.zoom)

        if kind == "start":
            color = (0, 255, 0)
        elif kind == "end":
            color = (255, 0, 0)
        else:
            color = (200, 200, 200)

        pygame.draw.polygon(screen, color, points, width=3)
