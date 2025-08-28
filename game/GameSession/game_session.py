import json
from components.Game.player import Player
from components.Game.board import Board

class GameSession:
    def __init__(self, player_amount):
        # game configs
        self.player_colours = None
        self.resource_cards_supply = None
        self.development_cards_supply = None

        self.load_game_configs()

        # players
        self.players = self.create_players(player_amount)

        # board
        self.board = Board()

    def create_players(self, player_amount):
        players = []

        # get player colours
        if player_amount == 3:
            player_colours = self.player_colours["3_player_colours"]
        else:
            player_colours = self.player_colours["4_player_colours"]

        for i in range(player_amount):
            players.append(Player(player_colours[i]))

    def load_game_configs(self):
        with open(r"C:\Users\isaac\OneDrive\Documents\GitHub\catan\config\game_config.json", "r") as f:
            file = json.load(f)

            self.player_colours = file["players"]
            self.resource_cards = file["resource_cards"]
            self.development_cards = file["development_cards"]