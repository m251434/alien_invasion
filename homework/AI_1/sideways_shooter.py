import sys
import pygame
from pygame.sprite import Sprite

class Ship:
    def __init__(self, screen):
        self.character = pygame.image.load('hw_images/ship_0012.png')
        self.character_rect = self.character.get_rect()
        self.screen_rect = screen.get_rect()
        self.character_rect.left = self.screen_rect.left
        self.ship_speed = 1.0

        self.y = float(self.character_rect.y)

        self.moving_up = False
        self.moving_down = False

    def draw(self):
        screen.blit(self.character, self.character_rect)

    def update(self):
        if self.moving_up and self.character_rect.top > 0:
            self.y -= self.ship_speed
        if self.moving_down and self.character_rect.bottom < self.screen_rect.bottom:
            self.y += self.ship_speed

        self.character_rect.y = self.y

class Bullet:
    def __init__(self, screen):
        super().__init__()
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.screen = screen

        self.rect = pygame.Rect(0, 0, self.bullet_width,
                                self.bullet_height)
        self.rect.midtop = ship.character_rect.midtop

        self.x = float(self.rect.x)

    def update(self):
        self.x -= self.bullet_speed
        self.rect.y = self.x

    def draw_bullet(self):
        pygame.draw.rect(screen, self.bullet_color, self.rect)


pygame.init()
screen = pygame.display.set_mode((500, 500))
ship = Ship(screen)

sprites = Sprite
bullets = Bullet(screen)
new_bullet = Bullet
bull = pygame.sprite.Group


screen.fill((112, 146, 190))

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ship.moving_up = True
            elif event.key == pygame.K_DOWN:
                ship.moving_down = True
            elif event.key == pygame.K_q:
                sys.exit()
            elif event.key == pygame.K_SPACE:
                new_bullet = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                ship.moving_up = False
            elif event.key == pygame.K_DOWN:
                ship.moving_down = False

    ship.update()
    bullets.update()
    screen.fill((112, 146, 190))
    bullets.draw_bullet()
    ship.draw()
    pygame.display.flip()