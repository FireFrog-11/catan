from typing import TYPE_CHECKING

if TYPE_CHECKING: # only for types. NOT IMPORTANT
    from components.Game.vertex import Vertex
    from components.Game.hex import Hex
    from components.Game.road import Road

class Edge:
    """
    This class represents an edge in the game board.
    """
    def __init__(self, vertex_1_key: tuple[int, int, int], vertex_2_key: tuple[int, int, int]):
        # BOARD STRUCTURE
        self.key: tuple[tuple[int, int, int], tuple[int, int, int]] = (vertex_1_key, vertex_2_key) if vertex_1_key < vertex_2_key else (vertex_2_key, vertex_1_key) # the unique coordinate for each edge
        self.vertices: list[Vertex] = [] # the 2 vertices on the end of the edge
        self.edges: list[Edge] = [] # the up to 4 edges around the edge
        self.hexes: list[Hex] = [] # all the hexes the edge is on (up to 2)

        # ROAD INFO
        self.road: None | Road = None