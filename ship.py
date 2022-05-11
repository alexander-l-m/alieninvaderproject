import pygame

class Ship:
    # A class to manage the ship


    def __init__(self, ai_game):
        # Initialise the ship and set its starting position.
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        # Calling the settings into the ship class
        self.settings = ai_game.settings

        # Load the ship image and get its rect
        self.image = pygame.image.load('alien_invasion/images/ship.bmp')
        
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom centre of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        # Draw the ship at its current location.
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        # Update the ship's position based on the movement flag
        # Update the ships x value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x
        self.rect.x = self.x
    
    def center_ship(self):
        # Centre the ship on the screen
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    

class BackgroundCharacter:

    def __init__(self, ai_game):
        # Initliase the background character and place it in the middle of the screen  
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Loading the background image
        self.image2 = pygame.image.load('alien_invasion/images/alien_background.bmp')
        self.rect = self.image2.get_rect()

        # Start character in the middle of the screen
        self.rect.midtop = self.screen_rect.midtop
    
    def blitme(self):
        # Draw the ship at its current location.
        self.screen.blit(self.image2, self.rect)
        
 