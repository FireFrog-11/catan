from typing import TYPE_CHECKING

if TYPE_CHECKING: # only for types. NOT IMPORTANT
    from components.Game.vertex import Vertex
    from components.Game.edge import Edge

class Hex:
    """
    This class represents a hex tile in the game board.
    """
    def __init__(self, q: int, r: int, hex_type: str, number_tile: int):
        self.axial_coordinates: tuple[int, int] = (q, r)
        self.cube_coordinates: tuple[int, int, int] = self.axial_to_cube(self.axial_coordinates)
        self.hex_type: str = hex_type
        self.number_tile: int = number_tile
        self.edges: list[Edge] = []
        self.vertices: list[Vertex] = []

    def axial_to_cube(self, axial_coordinates: tuple[int, int]) -> tuple[int, int, int]:
        """
        Converts the given axial coordinates to cube coordinates.
        """
        x = axial_coordinates[0]
        z = axial_coordinates[1]
        y = -x -z
        return (x, y, z)