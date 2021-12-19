import sys
import pygame
from ship import Ship
from settings import Settings

class AlienInvasion:
    """overall class to manage game asset and behavior."""

    def __init__(self):
        """initailize the game, and  create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

        # setting bg color
        self.bg_color = (230, 230, 230)

        self.ship = Ship(self)

    def run_game(self):
        """start the main loop for the game."""
        while True:
            # watch for keyboard and miuse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # redraw the screen during each pass through loop
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == "__main__":
    # making game instance & running it
    ai = AlienInvasion()
    ai.run_game()
