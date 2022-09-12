import pygame
import time


class Target(pygame.sprite.Sprite):
    def __init__(self, x, y, image, size, remaining_time):
        super(Target, self).__init__()
        self.x = x
        self.y = y
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(size * width), int(size * height)))
        self.remaining_time = remaining_time

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))


