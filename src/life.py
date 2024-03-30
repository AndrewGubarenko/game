import pygame

from fighter import Fighter


class Life(Fighter):

    def __init__(self, ai_game):
        super().__init__(ai_game)
        self.image = pygame.image.load(self.settings.fighter_image_ref)
        self.image = pygame.transform.smoothscale(self.image, (30, 30))
