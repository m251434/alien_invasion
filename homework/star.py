import sys
import pygame
from pygame.sprite import Sprite

WIDTH = 1000
HEIGHT = 600

class Star(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('hw_images/star.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

pygame.init()
screen = pygame.display.set_mode((1000, 600))
stars = pygame.sprite.Group()

star = Star()
star_width, star_height = star.rect.size
available_space_x = WIDTH - (2 * star_width)
available_space_y = HEIGHT - (2 * star_height)
number_stars_x = available_space_x // (1 * star_width)
number_rows = available_space_y // (1 * star_height)

for row_number in range(number_rows):
    for star_number in range(number_stars_x):
        star = Star()
        star_width, star_height = star.rect.size
        star.x = star_width + 2 * star_width * star_number
        star.rect.x = star.x
        star.rect.y = star_height + 2*star.rect.height * row_number
        stars.add(star)

screen.fill((195, 195, 195))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        star.update()
        screen.fill((195, 195, 195))
        stars.draw(screen)
        pygame.display.flip()


