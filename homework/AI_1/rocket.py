import pygame

class Ship:
    def __init__(self, screen):
        self.character = pygame.image.load('hw_images/ship_0009.png')
        self.character_rect = self.character.get_rect()
        self.screen_rect = screen.get_rect()
        self.character_rect.center = self.screen_rect.center
        self.ship_speed = 1.0

        self.x = float(self.character_rect.x)
        self.y = float(self.character_rect.y)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def draw(self):
        screen.blit(self.character, self.character_rect)

    def update(self):
        if self.moving_right and self.character_rect.right < self.screen_rect.right:
            self.x += self.ship_speed
        if self.moving_left and self.character_rect.left > 0:
            self.x -= self.ship_speed
        if self.moving_up and self.character_rect.top > 0:
            self.y -= self.ship_speed
        if self.moving_down and self.character_rect.bottom < self.screen_rect.bottom:
            self.y += self.ship_speed

        self.character_rect.x = self.x
        self.character_rect.y = self.y

pygame.init()
screen = pygame.display.set_mode((500, 500))
ship = Ship(screen)

screen.fill((181, 255, 255))

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
            elif event.key == pygame.K_UP:
                ship.moving_up = True
            elif event.key == pygame.K_DOWN:
                ship.moving_down = True


        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False
            elif event.key == pygame.K_UP:
                ship.moving_up = False
            elif event.key == pygame.K_DOWN:
                ship.moving_down = False

    ship.update()
    screen.fill((181, 255, 255))
    ship.draw()
    pygame.display.flip()
