import sys
from time import sleep

import pygame

from settings import Settings
from fighter import Fighter
from bullet import Bullet
from alien import Alien
from game_stats import GameStats


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

        self.stats = GameStats(self)

        self.fighter = Fighter(self)

        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        while True:
            self._check_events()

            if self.stats.game_active:
                self.fighter.update()
                self._update_bullets()
                self._update_aliens()

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
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.fighter.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.fighter.moving_left = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.fighter.blit_me()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        pygame.display.flip()

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullet_allowed_quantity:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

    def _create_fleet(self):
        for row_number in range(self.settings.aliens_row_quantity):
            for alien_number in range(self.settings.aliens_in_row_quantity):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien.x = self.settings.alien_width + 2 * self.settings.alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = self.settings.alien_height + 2 * self.settings.alien_height * row_number
        self.aliens.add(alien)

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.fighter, self.aliens):
            self._fighter_hit()

        self._check_aliens_landed()

    def _check_aliens_landed(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._fighter_hit()
                break

    def _fighter_hit(self):
        if self.stats.fighters_left > 0:
            self.stats.fighters_left -= 1

            self.aliens.empty()
            self.bullets.empty()

            self._create_fleet()
            self.fighter.center_fighter()

            sleep(1.0)
        else:
            self.stats.game_active = False

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
