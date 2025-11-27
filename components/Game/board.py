import os
import random
import json

from components.Game.hex import Hex
from components.Game.edge import Edge
from components.Game.vertex import Vertex
from globals.base_directory import get_project_root

# cube neighbor directions (pointy-top)
NEIGHBORS = [
    (1, -1, 0),   # 0 E
    (1, 0, -1),   # 1 NE
    (0, 1, -1),   # 2 NW
    (-1, 1, 0),   # 3 W
    (-1, 0, 1),   # 4 SW
    (0, -1, 1),   # 5 SE
]


def add_cube(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


class Board:
    """
    Represents the full game board including:
    - hexes
    - vertices
    - edges
    - all links between them
    """

    def __init__(self):
        self.size: int = 2  # radius of board

        # keys:
        #   hexes    -> (q, r)
        #   vertices -> frozenset of cube coords (1–3 hex centers)
        #   edges    -> frozenset of two vertex keys
        self.hexes: dict[tuple[int, int], Hex] = {}
        self.vertices: dict[frozenset, Vertex] = {}
        self.edges: dict[frozenset, Edge] = {}

        self.hex_type_amounts: list[str] = []
        self.number_tile_amounts: list[int] = []

        self._load_config()

    # --------------------------------------------------------
    # MAIN ENTRY POINT
    # --------------------------------------------------------

    def create_board(self):
        """
        Generates the full hex board. Call only once.
        Radius 2 Catan board: 19 hexes.
        """
        
        for q in range(-self.size, self.size + 1):
            for r in range(-self.size, self.size + 1):
                if abs(q + r) <= self.size:
                    self.build_hex(q, r)
        """
        self.link_graph()
        
        """
    # --------------------------------------------------------
    # HEX / TILE ASSIGNMENT
    # --------------------------------------------------------

    def get_hex_info(self):
        """Assign random type and number tile."""
        hex_type = random.choice(self.hex_type_amounts)
        self.hex_type_amounts.remove(hex_type)

        if hex_type != "desert":
            number_tile = random.choice(self.number_tile_amounts)
            self.number_tile_amounts.remove(number_tile)
            return hex_type, number_tile
        else:
            return hex_type, 0

    # --------------------------------------------------------
    # CORE BOARD CONSTRUCTION
    # --------------------------------------------------------

    def build_hex(self, q: int, r: int):
        """Construct a single hex and its vertices/edges."""
        hex_type, number_tile = self.get_hex_info()
        hex_ = Hex(q, r, hex_type, number_tile)
        self.hexes[(q, r)] = hex_

        center = hex_.cube_coordinates  # cube coordinate (x, y, z)      




        # 3 hex-centres that meet at this vertex: center + two neighbours
        n1 = add_cube(center, NEIGHBORS[0])
        n2 = add_cube(center, NEIGHBORS[(-1) % 6])

        # geometric vertex ID (works even if some hexes are "off-board")
        vertex_key = frozenset([center, n1, n2])

        # create vertex if needed
        if vertex_key not in self.vertices:
            self.vertices[vertex_key] = Vertex(vertex_key)

        vertex = self.vertices[vertex_key]
        vertex.hexes.append(hex_)

        # pixel corner order in Hex is already BR, TR, T, TL, BL, B
        vertex.pixel_coordinates = hex_.vertices_pixel_coordinates[0]
        hex_.vertices.append(vertex)






        # 3 hex-centres that meet at this vertex: center + two neighbours
        n1 = add_cube(center, NEIGHBORS[1])
        n2 = add_cube(center, NEIGHBORS[(0) % 6])

        # geometric vertex ID (works even if some hexes are "off-board")
        vertex_key = frozenset([center, n1, n2])

        # create vertex if needed
        if vertex_key not in self.vertices:
            self.vertices[vertex_key] = Vertex(vertex_key)

        vertex = self.vertices[vertex_key]
        vertex.hexes.append(hex_)

        # pixel corner order in Hex is already BR, TR, T, TL, BL, B
        vertex.pixel_coordinates = hex_.vertices_pixel_coordinates[1]
        hex_.vertices.append(vertex)






        '''
        # 3 hex-centres that meet at this vertex: center + two neighbours
        n1 = add_cube(center, NEIGHBORS[2])
        n2 = add_cube(center, NEIGHBORS[(1) % 6])

        # geometric vertex ID (works even if some hexes are "off-board")
        vertex_key = frozenset([center, n1, n2])

        # create vertex if needed
        if vertex_key not in self.vertices:
            self.vertices[vertex_key] = Vertex(vertex_key)

        vertex = self.vertices[vertex_key]
        vertex.hexes.append(hex_)

        # pixel corner order in Hex is already BR, TR, T, TL, BL, B
        vertex.pixel_coordinates = hex_.vertices_pixel_coordinates[2]
        hex_.vertices.append(vertex)
        '''

        '''
        # --- build all 6 corners ---
        for i in range(6):
            # 3 hex-centres that meet at this vertex: center + two neighbours
            n1 = add_cube(center, NEIGHBORS[i])
            n2 = add_cube(center, NEIGHBORS[(i - 1) % 6])

            # geometric vertex ID (works even if some hexes are "off-board")
            vertex_key = frozenset([center, n1, n2])

            # create vertex if needed
            if vertex_key not in self.vertices:
                self.vertices[vertex_key] = Vertex(vertex_key)

            vertex = self.vertices[vertex_key]
            vertex.hexes.append(hex_)

            # pixel corner order in Hex is already BR, TR, T, TL, BL, B
            vertex.pixel_coordinates = hex_.vertices_pixel_coordinates[i]
            hex_.vertices.append(vertex)

            # --- build edge between this corner and the next one ---
            next_i = (i + 1) % 6

            nn1 = add_cube(center, NEIGHBORS[next_i])
            nn2 = add_cube(center, NEIGHBORS[(next_i - 1) % 6])
            vertex2_key = frozenset([center, nn1, nn2])

            if vertex2_key not in self.vertices:
                # in practice this will usually be created when that corner
                # itself is processed, but this makes it bulletproof
                self.vertices[vertex2_key] = Vertex(vertex2_key)

            edge_key = frozenset([vertex_key, vertex2_key])

            if edge_key not in self.edges:
                self.edges[edge_key] = Edge(vertex_key, vertex2_key)

            edge = self.edges[edge_key]
            edge.hexes.append(hex_)
            hex_.edges.append(edge)
        '''

    # --------------------------------------------------------
    # GRAPH LINKING
    # --------------------------------------------------------

    def link_graph(self):
        """Connect all vertices, edges, and hexes in both directions."""

        # --- edges → vertices & vertices → edges ---
        for edge_key, edge in self.edges.items():
            vkeys = list(edge_key)  # two vertex keys
            vertex1 = self.vertices[vkeys[0]]
            vertex2 = self.vertices[vkeys[1]]

            edge.vertices = [vertex1, vertex2]
            edge.pixel_coordinates = [
                vertex1.pixel_coordinates,
                vertex2.pixel_coordinates,
            ]

            vertex1.edges.append(edge)
            vertex2.edges.append(edge)

        # --- vertices → neighbouring vertices ---
        for vertex in self.vertices.values():
            for edge in vertex.edges:
                for other_v in edge.vertices:
                    if other_v is not vertex and other_v not in vertex.vertices:
                        vertex.vertices.append(other_v)

        # --- edges → neighbouring edges ---
        for edge in self.edges.values():
            for vertex in edge.vertices:
                for other_edge in vertex.edges:
                    if other_edge is not edge and other_edge not in edge.edges:
                        edge.edges.append(other_edge)

    # --------------------------------------------------------
    # LOADING
    # --------------------------------------------------------

    def _load_config(self):
        root_path = get_project_root()
        config_path = os.path.join(root_path, "config", "game_config.json")

        with open(config_path, "r") as f:
            data = json.load(f)
            self.hex_type_amounts = data["hex_info"]["hex_type_list"]
            self.number_tile_amounts = data["hex_info"]["number_tile_list"]
