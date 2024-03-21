import pygame
from settings import Settings

class Fighter:
    """Class for fighter logic"""

    def __init__(self, ai_game):
        self.settings = Settings()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('static/images/fighter.bmp')
        self.image = pygame.transform.smoothscale(self.image, (self.settings.fighter_width, self.settings.fighter_height))
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

    def blit_me(self):
        self.screen.blit(self.image, self.rect)
