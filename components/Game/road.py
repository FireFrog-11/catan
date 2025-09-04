from typing import TYPE_CHECKING

if TYPE_CHECKING: # only for types. NOT IMPORTANT
    from components.Game.player import Player

class Road:
    """
    This class represents a road on the game board.
    """
    def __init__(self, owner: Player):
        self.owner: Player = owner

        self.owner.roads.append(self)  # adds road to owner