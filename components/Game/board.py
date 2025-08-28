from components.Game.hex import Hex
from components.Game.edge import Edge
from components.Game.vertex import Vertex

class Board:
    def __init__(self):
        self.size = 2
        self.hexes = {}
        self.vertices = {}
        self.edges = {}

        self.CORNER_OFFSETS = [
            (1, 0, -1),
            (1, -1, 0),
            (0, -1, 1),
            (-1, 0, 1),
            (-1, 1, 0),
            (0, 1, -1)
        ]

    def create_board(self):
        for q in range(-self.size, self.size + 1):
            for r in range(-self.size, self.size + 1):
                if abs(q + r) <= self.size:
                    self.build_hex(q, r)

    def build_hex(self, q, r):
        hex_ = Hex(q, r, "temp_type", "temp_num")
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
            hex_.vertices.append(vertex)

            # edges
            next_i = (i + 1) % 6
            offset2 = self.CORNER_OFFSETS[next_i]
            vertex2_key = (x + offset2[0], y + offset2[1], z + offset2[2])

            edge_key = tuple(sorted([vertex1_key, vertex2_key]))
            if edge_key not in self.edges:
                self.edges[edge_key] = Edge(vertex1_key, vertex2_key)
            edge = self.edges[edge_key]
            edge.hexes.append(hex_)
            hex_.edges.append(edge)

    def link_graph(self):
        # links edges to vertices and vertices to edges
        for edge_key, edge in self.edges.items():
            vertex1_key, vertex2_key = edge_key
            vertex1 = self.vertices[vertex1_key]
            vertex2 = self.vertices[vertex2_key]
            edge.vertices = [vertex1, vertex2]
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