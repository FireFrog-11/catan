import pygame
from globals.game_session import game_session
import json
import math

pygame.init()

class BoardRenderer:
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
        background_colour = self.config["background_colour"]
        
        self.screen.fill(background_colour)

    def _draw_hexes(self):
        hexes = game_session.board.hexes

        for hex in hexes.values():
            x, y = self.axial_to_pixel(hex.axial_coordinates)
            x += self.config["hex_x_offset"]
            y += self.config["hex_y_offset"]
            points = self._get_hex_points((x, y))

            colour = self._get_hex_colour(hex.hex_type)

            pygame.draw.polygon(self.screen, colour, points) # draw hex

            self._draw_number_tile((x, y), hex.number_tile) # draw number tile ontop of hex

    def _get_hex_colour(self, hex_type: str):
        colour_config = self.config["hex_colours"]

        colour = colour_config[hex_type]

        return colour

    def _get_hex_points(self, center_coor: tuple[float, float]):
        center_x, center_y = center_coor
        hex_size = self.config["hex_size"]
        points = []

        for i in range(6):
            angle_deg = 60 * i - 30

            angle_rad = math.radians(angle_deg)
            x = center_x + hex_size * math.cos(angle_rad)
            y = center_y + hex_size * math.sin(angle_rad)
            points.append((x, y))

        return points

    def _draw_robber(self):
        pass

    def _draw_number_tile(self, coordinates: tuple[int, int], number_tile):
        
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

    def axial_to_pixel(self, axial_coor: tuple[int, int]):
        hex_size = self.config["hex_size"]
        q, r = axial_coor

        x = hex_size * math.sqrt(3) * (q + r/2)
        y = hex_size * 3/2 * r

        return (x, y)

    def _load_config(self):
        """
        Loads config files for game.

        Will be replaced once save/load system is made.
        """
        with open(r"C:\Users\isaac\OneDrive\Documents\GitHub\catan\config\renderer_config.json", "r") as f:
            file = json.load(f)

            return file