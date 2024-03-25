class Settings:
    """Class for game settings"""

    def __init__(self):
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.icon = "static/images/logo.bmp"
        self.game_name = "Alien Invasion"

        # fighter settings
        self.fighter_width = 55
        self.fighter_height = 79
        self.fighter_speed = 1.1

        # bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed_quantity = 3
