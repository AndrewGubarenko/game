import sys

import pygame

from settings import Settings
from fighter import Fighter


class AlienInvasion:
    """General class operation by the behavior and logic of the game"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        # Full screen mode
        """
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        """
        # Window mode
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.settings.game_name)

        self.image_link = pygame.image.load(self.settings.icon)
        pygame.display.set_icon(self.image_link)

        self.fighter = Fighter(self)

    def run_game(self):
        while True:
            self._check_events()
            self.fighter.update()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.fighter.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.fighter.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.fighter.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.fighter.moving_left = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.fighter.blit_me()

        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
