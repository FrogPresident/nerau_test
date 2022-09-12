import pygame

import drawable
from scene import Scene
from target import Target

screen_height = 800
screen_width = 600
background = pygame.image.load('white_background.jpg')
target_object = pygame.image.load('target.png')
res = (screen_height, screen_width)
screen = pygame.display.set_mode(res)


def main():
    pygame.init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        # Code in here
        main_view = Scene()
        main_view.draw(screen)
        target = Target(22, 33, target_object, 1, 3)
        target.draw(screen)
        ###
        pygame.display.flip()


if __name__ == '__main__':
    main()
