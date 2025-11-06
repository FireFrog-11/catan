import os

from components.Game.hex import Hex
from components.Game.edge import Edge
from components.Game.vertex import Vertex
from globals.base_directory import get_project_root
import random
import json

class Board:
    """
    This class represents a game board.

    It contains all the vertices, edges and hexes.
    It also contains all the links between these components.
    """
    def __init__(self):
        self.size: int = 2 # radius of catan board (default catan board is radius 2)
        self.hexes: dict[tuple[int, int], Hex] = {} # dict of all hexes
        self.vertices: dict[tuple[int, int, int], Vertex] = {} # dict of all vertices
        self.edges: dict[tuple[tuple[int, int, int], tuple[int, int, int]], Edge] = {} # dict of all edges

        self.hex_type_amounts: list[str] = []
        self.number_tile_amounts: list[int] = []

        self._load_config()

        self.CORNER_OFFSETS: list[tuple[int, int, int]] = [
            (1, 0, -1),
            (1, -1, 0),
            (0, -1, 1),
            (-1, 0, 1),
            (-1, 1, 0),
            (0, 1, -1)
        ]

    def create_board(self):
        """
        This function creates the actual game board.

        THIS SHOULD ONLY BE CALLED ONCE.
        """
        for q in range(-self.size, self.size + 1):
            for r in range(-self.size, self.size + 1):
                if abs(q + r) <= self.size:
                    self.build_hex(q, r)

        self.link_graph() # automatically sets up board links

    def get_hex_info(self):
        """
        This function is the logic for giving each hex tile its type and number tile.
        """
        hex_type = random.choice(self.hex_type_amounts)
        self.hex_type_amounts.remove(hex_type)

        if hex_type != 'desert':
            number_tile = random.choice(self.number_tile_amounts)
            self.number_tile_amounts.remove(number_tile)
            return (hex_type, number_tile)
        else:
            return (hex_type, 0) # desert tile gets given number tile of 0

    def build_hex(self, q: int, r: int):
        """
        This function creates a hex for the given coordinates.

        THIS FUNCTION SHOULD NOT NEED TO BE CALLED OUTSIDE THE CREATE_BOARD FUNCTION.
        """
        hex_type, number_tile = self.get_hex_info()
        
        hex_ = Hex(q, r, hex_type, number_tile)

        self.hexes[(q, r)] = hex_
        x, y, z = hex_.cube_coordinates

        for i in range(6):
            # vertices
            offset1 = self.CORNER_OFFSETS[i]
            vertex1_key = (x + offset1[0], y + offset1[1], z + offset1[2])
            if vertex1_key not in self.vertices:
                self.vertices[vertex1_key] = Vertex(vertex1_key)
            vertex = self.vertices[vertex1_key]
            vertex.hexes.append(hex_)
            vertex.pixel_coordinates = hex_.vertices_pixel_coordinates[i]
            hex_.vertices.append(vertex)

            # edges
            next_i = (i + 1) % 6
            offset2 = self.CORNER_OFFSETS[next_i]
            vertex2_key = (x + offset2[0], y + offset2[1], z + offset2[2])

            edge_key = (vertex1_key, vertex2_key) if vertex1_key < vertex2_key else (vertex2_key, vertex1_key) # ensures consisted ordering. (V1, V2) == (V2, V1)
            if edge_key not in self.edges:
                self.edges[edge_key] = Edge(vertex1_key, vertex2_key)
            edge = self.edges[edge_key]
            edge.hexes.append(hex_)
            hex_.edges.append(edge)

    def link_graph(self):
        """
        This function creates all the links between the vertices and edges.

        THIS FUNCTION SHOULD NOT NEED TO BE CALLED OUTSIDE THE CREATE_BOARD FUNCTION.
        """
        # links edges to vertices and vertices to edges
        for edge_key, edge in self.edges.items():
            vertex1_key, vertex2_key = edge_key
            vertex1 = self.vertices[vertex1_key]
            vertex2 = self.vertices[vertex2_key]
            edge.vertices = [vertex1, vertex2]
            edge.pixel_coordinates = [vertex1.pixel_coordinates, vertex2.pixel_coordinates]
            vertex1.edges.append(edge)
            vertex2.edges.append(edge)

        # links vertices to neighbouring vertices
        for vertex in self.vertices.values():
            for edge in vertex.edges:
                for new_vertex in edge.vertices:
                    if new_vertex is not vertex and new_vertex not in vertex.vertices:
                        vertex.vertices.append(new_vertex)

        # links edges to neighbouring edges
        for edge in self.edges.values():
            for vertex in edge.vertices:
                for new_edge in vertex.edges:
                    if new_edge is not edge and new_edge not in edge.edges:
                        edge.edges.append(new_edge)

    def _load_config(self):
        """
        Loads config files for game.

        Will be replaced once save/load system is made.
        """
        root_path = get_project_root()
        config_path = os.path.join(root_path, "config", "game_config.json")

        with open(config_path, "r") as f:
            file = json.load(f)

            self.hex_type_amounts = file["hex_info"]["hex_type_list"]
            self.number_tile_amounts = file["hex_info"]["number_tile_list"]