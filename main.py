import pygame
import json
import sys
from globals.gamestatemanager import gamestate_manager
from gamestates.catan_state import CatanState

class Main:
    def __init__(self):
        pygame.init()

        self.settings = self.load_settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()

        self.gamestate_manager = gamestate_manager

        self.catan_state = CatanState()

        self.gamestate_manager.push_state(self.catan_state)

    def run(self):
        while True:
            dt = self.clock.tick(self.settings["fps"]) / 1000


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

                self.gamestate_manager.handle_event(event)

            self.gamestate_manager.update(dt)

            self.gamestate_manager.render(self.screen)

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