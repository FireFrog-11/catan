class Vertex:
    def __init__(self, key):
        vertex_key = key
        self.edges = [] # the up to 3 edges around a vertex
        self.vertices = [] # the up to 3 vertices around a vertex
        self.hexes = [] # all the hexes the vertex is on (up to 3)