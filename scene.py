import pygame

from drawable import Drawable

background = pygame.image.load('white_background.jpg')


class Scene(Drawable):

    def draw(self, screen):
        screen.blit(background, (0, 0))
