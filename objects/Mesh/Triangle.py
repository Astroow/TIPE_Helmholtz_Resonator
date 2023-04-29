from objects.Mesh.Point import Point


class Triangle:
    def __init__(self, v1: Point, v2: Point, v3: Point):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
