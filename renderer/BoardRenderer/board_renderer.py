from __future__ import annotations

import os
from typing import TYPE_CHECKING
import pygame
import json
from globals.base_directory import get_project_root

if TYPE_CHECKING: # only for types. NOT IMPORTANT
    from game.GameSession.game_session import GameSession

pygame.init()

class BoardRenderer:
    """
    This class is what actually renders the game board.
    """
    def __init__(self, game_session: GameSession):
        self.config = self._load_config()

        self.game_session: GameSession = game_session

    def render_board(self, screen):
        self._draw_background(screen)

        self._draw_hexes(screen)

        self._draw_robber()

        self._draw_buildings()

        self._draw_roads()

    def _draw_background(self, screen: pygame.Surface):
        """
        Draws background
        """
        background_colour = self.config["background_colour"]
        
        screen.fill(background_colour)

    def _draw_hexes(self, screen: pygame.Surface):
        """
        Draws all the hexes and number tiles.
        """
        hexes = self.game_session.board.hexes

        for hex in hexes.values():
            x, y = hex.pixel_coordinates
            points = hex.vertices_pixel_coordinates

            colour = self._get_hex_colour(hex.hex_type)

            pygame.draw.polygon(screen, colour, points) # draw hex

            self._draw_number_tile((x, y), hex.number_tile, screen) # draw number tile ontop of hex

    def _get_hex_colour(self, hex_type: str) -> tuple[int, int, int]:
        """
        Gets the hex colours based on the hex type using the config.
        """
        colour_config = self.config["hex_colours"]

        colour = colour_config[hex_type]

        return colour

    def _draw_robber(self):
        pass

    def _draw_number_tile(self, coordinates: tuple[float, float], number_tile: int, screen: pygame.Surface):
        """
        This function draws the number tile for a certain hex tile.
        """
        font_name = self.config["number_tile"]["font"]
        font_size = self.config["number_tile"]["font_size"]
        font_colour = self.config["number_tile"]["font_colour"]
        font_bold = self.config["number_tile"]["bold"]

        background_colour = self.config["number_tile"]["number_tile_background_colour"]
        background_radius = self.config["number_tile"]["background_radius"]

        font = pygame.font.SysFont(font_name, font_size, font_bold)

        text = font.render(str(number_tile), True, font_colour)
        text_rect = text.get_frect(center=(coordinates))

        pygame.draw.circle(screen, background_colour, coordinates, background_radius)

        screen.blit(text, text_rect)

    def _draw_buildings(self):
        pass

    def _draw_roads(self):
        pass

    def _load_config(self):
        """
        Loads config files for game.

        Will be replaced once save/load system is made.
        """
        root_path = get_project_root()
        config_path = os.path.join(root_path, "config", "renderer_config.json")

        with open(config_path, "r") as f:
            file = json.load(f)

            return file