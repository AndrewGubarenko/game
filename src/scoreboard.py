import pygame.font
from pygame.sprite import Group

from life import Life

class Scoreboard:

    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 24)

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_lives()

    def prep_score(self):
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        title = "Scores: "
        self.score_image = self.font.render(title + score_str, True, self.text_color, self.settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 10

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.lives.draw(self.screen)

    def prep_high_score(self):
        high_score = round(self.stats.high_score)
        high_score_str = "{:,}".format(high_score)
        title = "High score: "
        self.high_score_image = self.font.render(title + high_score_str, True, self.text_color, self.settings.bg_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_level(self):
        level_str = str(self.stats.level)
        title = "Level: "
        self.level_image = self.font.render(title + level_str, True, self.text_color, self.settings.bg_color)

        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom

    def prep_lives(self):
        self.lives = Group()
        for life_number in range(self.stats.fighters_left):
            life = Life(self.ai_game)
            life.rect.x = 10 + life_number * life.rect.width
            life.rect.y = 10
            self.lives.add(life)
