from typing import TYPE_CHECKING
from components.Game.city import City
import json

if TYPE_CHECKING: # only for types. NOT IMPORTANT
    from components.Game.player import Player

class Settlement:
    """
    This class represents a settlement on the game board.
    """
    def __init__(self, owner: Player):
        self.owner: Player = owner

        self.resource_amount: int = 1 # can be customized in settlement config (default value = 1)
        self.victory_points: int = 1 # can be customized in settlement config (default value = 1)
        self.load_settlement_config()

        self.owner.buildings.append(self) # adds settlement to owner

    def upgrade(self):
        """
        Upgrades the settlement into a city.
        """
        return City(self.owner)

    def load_settlement_config(self):
        """
        Loads config files for settlement.

        Will be replaced once save/load system is made.
        """
        with open(r"C:\Users\isaac\OneDrive\Documents\GitHub\catan\config\game_config.json", "r") as f:
            file = json.load(f)

            self.resource_amount = file["settlement"]["resource_amount"]
            self.victory_points = file["settlement"]["victory_points"]