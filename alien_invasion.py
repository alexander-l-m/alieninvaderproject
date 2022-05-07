import sys
import pygame
from ship import BackgroundCharacter
from settings import Settings
from ship import Ship

class AlienInvastion:
    # Overall class to manage game assets and behaviour

    def __init__(self):
        # Initialise the game and create game resources
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        # Set the background colour.
        self.bg_color = (0, 0, 0)

        # Applying the ship to the main class
        self.ship = Ship(self)
        self.alien = BackgroundCharacter(self)        

    
    def run_game(self):
        # Start the main loop for the game
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()           

            
    def _check_events(self):
        # Respond to key presses and mouse events 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            

            
    def _check_keydown_events(self, event):

        # Conditional statements for keys when pressed
        
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = True
            elif event.key == pygame.K_q:
                sys.exit()
    
    def _check_keyup_events(self, event):

        # Conditional statements for keys when released
            
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = False

    
    def _update_screen(self):

        # Redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)

        # Placing the ship to the instance of the game
        self.alien.blitme()
        self.ship.blitme()
            
        # Make the most recently drawn screen visable
        pygame.display.flip()    



if __name__ == '__main__':
    # Make a game instance, and run the game
    ai = AlienInvastion()
    ai.run_game()
