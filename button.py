import pygame

from coordinate_drawable import CoordinateDrawable
from utils import leaf


@leaf
class Button(CoordinateDrawable):
    def __init__(self, x, y, image, scale):
        super().__init__(x, y)
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.click = False

    def draw(self, screen):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.click == False:
                action = True
                self.click = False
        screen.blit(self.image, (self.x, self.y))

        return action
