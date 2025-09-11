import json
from typing import TYPE_CHECKING

if TYPE_CHECKING: # only for types. NOT IMPORTANT
    from components.Game.player import Player

class LargestArmy:
    """
    This class contains all the information related to the largest army.
    """
    def __init__(self):
        self.current_owner: None | Player = None

        self.victory_points = 2 # can be customized in largest army config (default value = 2)
        self.minimum_knights = 3 # can be customized in largest army config (default value = 3)

    def update_ownership(self):
        """
        This will be called whenever something changes to evaluate who has the largest army.
        """
        pass

    def load_config(self):
        """
        Loads config files for largest army.

        Will be replaced once save/load system is made.
        """
        with open(r"C:\Users\isaac\OneDrive\Documents\GitHub\catan\config\game_config.json", "r") as f:
            file = json.load(f)

            self.victory_points = file["largest_army"]["victory_points"]
            self.minimum_knights = file["largest_army"]["minimum_knights"]