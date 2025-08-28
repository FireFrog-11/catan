class Edge:
    def __init__(self, vertex_1_key, vertex_2_key):
        self.key = tuple(sorted([vertex_1_key, vertex_2_key]))
        self.vertices = [] # the 2 vertices on the end of the edge
        self.edges = [] # the up to 4 edges around the edge
        self.hexes = [] # all the hexes the edge is on (up to 2)