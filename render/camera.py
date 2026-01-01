# render/camera.py
import pygame

class Camera:
    def __init__(self, offset=(0, 0), zoom=1.0):
        self.offset = pygame.Vector2(offset)
        self.zoom = zoom
        self.min_zoom = 0.2
        self.max_zoom = 5.0

    def world_to_screen(self, pos):
        return (pygame.Vector2(pos) * self.zoom) + self.offset

    def screen_to_world(self, pos):
        return (pygame.Vector2(pos) - self.offset) / self.zoom

    def zoom_at(self, zoom_factor, screen_pos):
        """
        Zooms in/out while keeping the world position under the cursor fixed.
        zoom_factor > 1 → zoom in
        zoom_factor < 1 → zoom out
        """
        old_zoom = self.zoom
        new_zoom = max(self.min_zoom, min(self.max_zoom, self.zoom * zoom_factor))
        if new_zoom == old_zoom:
            return  # reached min/max zoom

        # World position under cursor before zoom
        world_before = self.screen_to_world(screen_pos)

        # Update zoom
        self.zoom = new_zoom

        # World position under cursor after zoom
        world_after = self.screen_to_world(screen_pos)

        # Adjust offset so the world position under cursor stays fixed
        self.offset += (world_after - world_before) * self.zoom
