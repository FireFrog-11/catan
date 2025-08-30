from typing import TYPE_CHECKING

if TYPE_CHECKING: # only for types. NOT IMPORTANT
    from components.Game.edge import Edge
    from components.Game.hex import Hex

class Vertex:
    """
    This class represents a vertex in the game board.
    """
    def __init__(self, key: tuple[int, int, int]):
        self.vertex_key: tuple[int, int, int] = key # the unique coordinate for each vertex
        self.edges: list[Edge] = [] # the up to 3 edges around a vertex
        self.vertices: list[Vertex] = [] # the up to 3 vertices around a vertex
        self.hexes: list[Hex] = [] # all the hexes the vertex is on (up to 3)