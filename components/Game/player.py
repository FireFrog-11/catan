from typing import TYPE_CHECKING
from globals.largest_army import largest_army
from globals.longest_road import longest_road

if TYPE_CHECKING: # only for types. NOT IMPORTANT
    from components.Game.settlement import Settlement
    from components.Game.city import City
    from components.Game.road import Road
    from components.Game.largest_army import LargestArmy
    from components.Game.longest_road import LongestRoad
    from components.Game.DevelopmentCards.template.development_card import DevelopmentCard

class Player:
    """
    This class represents a player and stores all the information related to each player.
    """
    def __init__(self, player_colour: str):
        # special cards
        self.largest_army: LargestArmy = largest_army
        self.longest_road: LongestRoad = longest_road

        # stats
        self.knights_played: int = 0 # very important stat, used for largest army
        self.roads_built: int = 0
        self.settlements_built: int = 0
        self.cities_built: int = 0


        self.player_colour: str = player_colour

        self.resource_cards: dict[str, int] = {}
        self.development_cards: dict[str, list[DevelopmentCard]] = {}
        self.used_development_cards: int[str, int] = {}

        self.roads: list[Road] = []
        self.buildings: list[Settlement | City] = []

    def calculate_victory_points(self) -> int:
        """
        This returns the amount of victory points the player has.
        """
        victory_points = 0

        # victory points from buildings
        for building in self.buildings:
            victory_points += building.victory_points

        # victory points from largest army and longest road
        if self.longest_road.current_owner == self:
            victory_points += self.longest_road.victory_points

        if self.largest_army.current_owner == self:
            victory_points += self.largest_army.victory_points

        # victory points from development cards
        victory_points += len(self.development_cards["victory_point"])

        return victory_points