import pygame
from globals.game_session import game_session
import json
import math

pygame.init()

class BoardRenderer:
    """
    This class is what actually renders the game board.
    """
    def __init__(self, screen: pygame.Surface):
        self.screen: pygame.Surface = screen
        self.config = self._load_config()

    def render_board(self):
        self._draw_background()

        self._draw_hexes()

        self._draw_robber()

        self._draw_buildings()

        self._draw_roads()

    def _draw_background(self):
        """
        Draws background
        """
        background_colour = self.config["background_colour"]
        
        self.screen.fill(background_colour)

    def _draw_hexes(self):
        """
        Draws all the hexes and number tiles.
        """
        hexes = game_session.board.hexes

        for hex in hexes.values():
            x, y = hex.pixel_coordinates
            points = hex.vertices_pixel_coordinates

            colour = self._get_hex_colour(hex.hex_type)

            pygame.draw.polygon(self.screen, colour, points) # draw hex

            self._draw_number_tile((x, y), hex.number_tile) # draw number tile ontop of hex

    def _get_hex_colour(self, hex_type: str) -> tuple[int, int, int]:
        """
        Gets the hex colours based on the hex type using the config.
        """
        colour_config = self.config["hex_colours"]

        colour = colour_config[hex_type]

        return colour

    def _draw_robber(self):
        pass

    def _draw_number_tile(self, coordinates: tuple[float, float], number_tile: int):
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

        pygame.draw.circle(self.screen, background_colour, coordinates, background_radius)

        self.screen.blit(text, text_rect)

    def _draw_buildings(self):
        pass

    def _draw_roads(self):
        pass

    def _load_config(self):
        """
        Loads config files for game.

        Will be replaced once save/load system is made.
        """
        with open(r"C:\Users\isaac\OneDrive\Documents\GitHub\catan\config\renderer_config.json", "r") as f:
            file = json.load(f)

            return file