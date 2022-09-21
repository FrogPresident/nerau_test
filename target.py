import pygame
import time

from pygame.sprite import Sprite

from coordinate_drawable import CoordinateDrawable


class Target(CoordinateDrawable):
    def __init__(self, x, y, image, size, remaining_time):
        super().__init__(x, y)
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(size * width), int(size * height)))
        self.remaining_time = remaining_time

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))


