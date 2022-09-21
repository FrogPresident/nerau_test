import pygame

import drawable
from scene import Scene
from target import Target
from button import Button

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
        start_button = Button(10, 10, target_object, 1)
        start_button.draw(screen)
        start_button.add(main_view)
        ###
        pygame.display.flip()


if __name__ == '__main__':
    main()
