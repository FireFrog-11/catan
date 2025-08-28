import pygame
import json
import sys

class Main:
    def __init__(self):
        pygame.init()

        self.settings = self.load_settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()

    def run(self):
        while  True:
            self.clock.tick(self.settings["fps"])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            pygame.display.update()

    def load_settings(self):
        """
        This is a temp function to load settings json.

        It will be replaced once the save/load system has been made.
        """
        with open("config/settings.json", "r") as f:
            file = json.load(f)
            settings = file["general_settings"]
        
        return settings

if __name__ == "__main__":
    main = Main()
    main.run()