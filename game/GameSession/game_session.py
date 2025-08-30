import json
from components.Game.player import Player
from components.Game.board import Board

class GameSession:
    """
    This class is made to store the current state of a game of Catan.

    It stores everything required to know the exact state of the game.
    """
    def __init__(self, player_amount: int):
        # game configs
        self.player_colours: dict[str, list[str]] = {}
        self.resource_cards_supply: dict[str, int] = {}
        self.development_cards_supply: dict[str, int] = {}

        self.load_game_configs()

        # players
        self.players: list[Player] = self.create_players(player_amount)

        # board
        self.board: Board = Board()

    def create_players(self, player_amount: int):
        """
        Creates all the players and assigns player colours based on amount of players.
        """
        players = []

        # get player colours
        if player_amount == 3:
            player_colours = self.player_colours["3_player_colours"]
        else:
            player_colours = self.player_colours["4_player_colours"]

        # create players
        for i in range(player_amount):
            players.append(Player(player_colours[i]))

        return players

    def load_game_configs(self):
        """
        Loads config files for game.

        Will be replaced once save/load system is made.
        """
        with open(r"C:\Users\isaac\OneDrive\Documents\GitHub\catan\config\game_config.json", "r") as f:
            file = json.load(f)

            self.player_colours = file["players"]
            self.resource_cards_supply = file["resource_cards"]
            self.development_cards_supply = file["development_cards"]