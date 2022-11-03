import sys
import pygame

class Key:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((200, 200))
        self.bg_color = (233, 173, 226)

        pygame.display.set_caption("KeyGame")

    def game(self):
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        print(event.key)
        if event.key == pygame.K_q:
            sys.exit()

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        pygame.display.flip()

if __name__ == '__main__':
    kg = Key()
    kg.game()



