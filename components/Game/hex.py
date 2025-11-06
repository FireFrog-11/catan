import os
from typing import TYPE_CHECKING
import math
import json
from globals.scale_factor import get_scale_factors
from globals.base_directory import get_project_root
import pygame

if TYPE_CHECKING: # only for types. NOT IMPORTANT
    from components.Game.vertex import Vertex
    from components.Game.edge import Edge

class Hex:
    """
    This class represents a hex tile in the game board.
    """
    def __init__(self, q: int, r: int, hex_type: str, number_tile: int):
        # scale factors
        self.scale_factor_x, self.scale_factor_y = get_scale_factors(pygame.display.get_surface())

        self.hex_x_offset = 0
        self.hex_y_offset = 0
        self.hex_size = 0
        self._load_config()

        self.axial_coordinates: tuple[int, int] = (q, r)
        self.cube_coordinates: tuple[int, int, int] = self.axial_to_cube(self.axial_coordinates)
        self.pixel_coordinates: tuple[float, float] = self.axial_to_pixel(self.axial_coordinates)
        self.hex_type: str = hex_type
        self.number_tile: int = number_tile
        self.edges: list[Edge] = []
        self.vertices: list[Vertex] = []
        self.vertices_pixel_coordinates: list[tuple[float, float]] = self.get_hex_vertex_coords()

    def axial_to_pixel(self, axial_coordinates: tuple[int, int]) -> tuple[float, float]:
        """
        This converts axial coordinates into pixel coordinates.
        """
        q, r = axial_coordinates

        x = self.hex_size * math.sqrt(3) * (q + r/2) * self.scale_factor_x
        y = self.hex_size * 3/2 * r * self.scale_factor_y

        x += self.hex_x_offset * self.scale_factor_x
        y += self.hex_y_offset * self.scale_factor_y

        return (x, y)
    
    def get_hex_vertex_coords(self) -> list[tuple[float, float]]:
        """
        This returns the pixel coordinates of each hex's vertices.
        """
        center_x, center_y = self.pixel_coordinates
        points = []

        for i in range(6):
            angle_deg = 60 * i - 30

            angle_rad = math.radians(angle_deg)
            x = center_x + self.hex_size * math.cos(angle_rad) * self.scale_factor_x
            y = center_y + self.hex_size * math.sin(angle_rad) * self.scale_factor_y
            points.append((x, y))

        return points

    def axial_to_cube(self, axial_coordinates: tuple[int, int]) -> tuple[int, int, int]:
        """
        Converts the given axial coordinates to cube coordinates.
        """
        x = axial_coordinates[0]
        z = axial_coordinates[1]
        y = -x -z
        return (x, y, z)
    
    def _load_config(self):
        """
        Loads config files for game.

        Will be replaced once save/load system is made.
        """
        root_path = get_project_root()
        config_path = os.path.join(root_path, "config", "renderer_config.json")

        with open(config_path, "r") as f:
            file = json.load(f)

            self.hex_x_offset = file["hex_x_offset"]
            self.hex_y_offset = file["hex_y_offset"]
            self.hex_size = file["hex_size"]