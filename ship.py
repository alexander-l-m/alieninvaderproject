import pygame

class Ship:
    # A class to manage the ship


    def __init__(self, ai_game):
        # Initialise the ship and set its starting position.
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load('alien_invasion/images/ship.bmp')
        
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom centre of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        # Draw the ship at its current location.
        self.screen.blit(self.image, self.rect)

    

class BackgroundCharacter:

    def __init__(self, ai_game):
        # Initliase the background character and place it in the middle of the screen  
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Loading the background image
        self.image2 = pygame.image.load('alien_invasion/images/alien.bmp')
        self.rect = self.image2.get_rect()

        # Start character in the middle of the screen
        self.rect.midtop = self.screen_rect.midtop
    
    def blitme(self):
        # Draw the ship at its current location.
        self.screen.blit(self.image2, self.rect)
        
 