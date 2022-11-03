import pygame
import time

pygame.init()
screen = pygame.display.set_mode((500, 500))
screen.fill((181, 255, 255))

class Ship:
    character = pygame.image.load('hw_images/ship_0009.png')
    character_rect = character.get_rect()
    screen_rect = screen.get_rect()
    character_rect.center = screen_rect.center

    screen.blit(character, character_rect)

pygame.display.flip()
time.sleep(10)