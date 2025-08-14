import pygame
import json
import sys

with open("config/settings.json", "r") as f:
    file = json.load(f)
    settings = file["general_settings"]

class Main:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()

    def run(self):
        while  True:
            self.clock.tick(settings["fps"])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

if __name__ == "__main__":
    main = Main()
    main.run()