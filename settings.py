from pygame import init


class Settings:
    # A Class to store all settings for Alien Invasion


    def __init__(self):
        
        # Initialise the games settings
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        # Ship settings, speed etc
        self.ship_speed = 5.5

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3