from typing import TYPE_CHECKING

if TYPE_CHECKING: # only for types. NOT IMPORTANT
    from components.Game.settlement import Settlement
    from components.Game.city import City

class Player:
    def __init__(self, player_colour):
        self.player_colour = player_colour
        self.victory_points = self.calculate_victory_points()

        self.resource_cards = {}
        self.development_cards = {}

        self.roads = []
        self.buildings: list[Settlement | City] = []

    def calculate_victory_points(self):
        victory_points = 0

        for building in self.buildings:
            victory_points += building.victory_points

        if self.has_largest_army:
            victory_points += 2

        if self.has_longest_road:
            victory_points += 2