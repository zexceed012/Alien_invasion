import sys
import pygame

from settings import Settings


class AlienInvasion:
    """overall class to manage game asset and behavior."""

    def __init__(self):
        """initailize the game, and  create game resources."""
        pygame.init()

        self.screen = pygame.display.set_mode((1265, 665))
        pygame.display.set_caption("Alien Invasion")

        # setting bg color
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """start the main loop for the game."""
        while True:
            # watch for keyboard and miuse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # redraw the screen during each pass through loop
            self.screen.fill(self.bg_color)

            # make the most recently drawn screen visible.
            pygame.display.flip()


if __name__ == "__main__":
    # making game instance & running it
    ai = AlienInvasion()
    ai.run_game()
