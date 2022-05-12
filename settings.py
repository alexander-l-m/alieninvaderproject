from pygame import init


class Settings:
    # A Class to store all settings for Alien Invasion


    def __init__(self):
        
        # Initialise the games settings
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (20, 20, 10)

        # Ship settings, speed etc
        self.ship_limit = 3

        # Bullet settings
        
        self.bullet_width = 10000
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings       
        self.fleet_drop_speed = 10
       

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initilize_dynamic_settings()

    def initilize_dynamic_settings(self):
        # Initialize settings that changed throughout the game
        self.ship_speed = 1.5
        self.bullet_speed = 2.0
        self.alien_speed = 1.0
        # Scoring
        self.alien_points = 50

        # Fleet direction of 1, represents right, -1 represents left
        self.fleet_direction = 1
    
    def increase_speed(self):
        # Increase speed settings and alien point values
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        # To test to see if points are increasing in the terminal
        #print(self.alien_points)
        