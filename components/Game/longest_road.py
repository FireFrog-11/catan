import json
from typing import TYPE_CHECKING

if TYPE_CHECKING: # only for types. NOT IMPORTANT
    from components.Game.player import Player

class LongestRoad:
    """
    This class contains all the information related to the longest road.
    """
    def __init__(self):
        self.current_owner: None | Player = None

        self.victory_points = 2  # can be customized in longest road config (default value = 2)
        self.minimum_roads = 5  # can be customized in longest road config (default value = 5)

    def update_ownership(self):
        """
        This will be called whenever something changes to evaluate who has the longest road.
        """
        pass

    def load_config(self):
        """
        Loads config files for longest road.

        Will be replaced once save/load system is made.
        """
        with open(r"C:\Users\isaac\OneDrive\Documents\GitHub\catan\config\game_config.json", "r") as f:
            file = json.load(f)

            self.victory_points = file["longest_road"]["victory_points"]
            self.minimum_roads = file["longest_road"]["minimum_roads"]
