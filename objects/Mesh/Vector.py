from objects.Mesh.Point import Point


class Vector:
    def __init__(self, beg: Point, end: Point):
        self.x = end.x - beg.x
        self.y = end.y - beg.y
        self.z = end.z - beg.z
