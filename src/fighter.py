import pygame
from pygame.sprite import Sprite


class Fighter(Sprite):
    """Class for fighter logic"""

    def __init__(self, ai_game):
        super().__init__()
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load(self.settings.fighter_image_ref)
        self.image = pygame.transform.smoothscale(self.image,
                                                  (self.settings.fighter_width, self.settings.fighter_height))
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

    def blit_me(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.fighter_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.fighter_speed

        self.rect.x = self.x

    def center_fighter(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
