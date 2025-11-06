import json
import os

from components.Game.player import Player
from components.Game.board import Board
from globals.base_directory import get_project_root

class GameSession:
    """
    This class is made to store the current state of a game of Catan.

    It stores everything required to know the exact state of the game.
    """
    def __init__(self, player_amount: int=4):
        # game configs
        self.player_colours: dict[str, list[str]] = {}
        self.resource_cards_supply: dict[str, int] = {}
        self.development_cards_supply: dict[str, int] = {}

        self.load_game_configs()

        # players
        self.players: list[Player] = self.create_players(player_amount)

        self.player_turn: int = 1 # default (game starts with player 1)

        # board
        self.board: Board = Board()
        self.board.create_board()

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
            players.append(Player(player_colours[i], i + 1)) # add one to start player number at 1

        return players

    def load_game_configs(self):
        """
        Loads config files for game.

        Will be replaced once save/load system is made.
        """
        root_path = get_project_root()
        config_path = os.path.join(root_path, "config", "game_config.json")

        with open(config_path, "r") as f:
            file = json.load(f)

            self.player_colours = file["players"]
            self.resource_cards_supply = file["resource_cards"]
            self.development_cards_supply = file["development_cards"]