class Hex:
    def __init__(self, q, r, hex_type, number_tile):
        self.axial_coordinates = (q, r)
        self.cube_coordinates = self.axial_to_cube(self.axial_coordinates)
        self.hex_type = hex_type
        self.number_tile = number_tile
        self.edges = []
        self.vertices = []

    def axial_to_cube(axial_coordinates):
        x = axial_coordinates[0]
        z = axial_coordinates[1]
        y = -x -z
        return (x, y, z)