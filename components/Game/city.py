from typing import TYPE_CHECKING
import json

if TYPE_CHECKING: # only for types. NOT IMPORTANT
    from components.Game.player import Player

class City:
    """
    This class represents a city on the game board.
    """
    def __init__(self, owner: Player):
        self.owner: Player = owner

        self.resource_amount: int = 2 # can be customized in city config (default value = 2)
        self.victory_points: int = 2 # can be customized in city config (default value = 2)
        self.load_city_config()

        self.owner.buildings.append(self)  # adds city to owner

    def load_city_config(self):
        """
        Loads config files for city.

        Will be replaced once save/load system is made.
        """
        with open(r"C:\Users\isaac\OneDrive\Documents\GitHub\catan\config\game_config.json", "r") as f:
            file = json.load(f)

            self.resource_amount = file["city"]["resource_amount"]
            self.victory_points = file["city"]["victory_points"]