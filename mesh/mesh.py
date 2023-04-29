from objects.Mesh.Point import Point
from objects.Mesh.Triangle import Triangle
from objects.Mesh.Vector import Vector


def sign(pv: Point, cv: Point, nv: Point) -> float:
    return ((pv.x - nv.x) * (cv.y - nv.y)) - ((cv.x - nv.x) * (pv.y - nv.y))


def angle_is_convex(pv: Vector, nv: Vector) -> bool:
    if pv.x * nv.y - pv.y * nv.x > 0:
        return True
    return False


def triangle_is_empty(triangle: Triangle, vertices: [Point]) -> bool:
    flag = True
    for vertex_to_check in vertices:
        if vertex_to_check != triangle.v1 and vertex_to_check != triangle.v2 and vertex_to_check != triangle.v3:
            d1 = sign(vertex_to_check, triangle.v1, triangle.v2)
            d2 = sign(vertex_to_check, triangle.v2, triangle.v3)
            d3 = sign(vertex_to_check, triangle.v3, triangle.v1)

            has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
            has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)

            if not (has_neg and has_pos):
                flag = False
    return flag


def triangulation(vertices: [Point]) -> [Triangle]:
    triangles = []
    while len(vertices) >= 3:
        for i in range(len(vertices)):
            if angle_is_convex(Vector(vertices[i - 1], vertices[i]), Vector(vertices[i + 1], vertices[i])) \
                    and triangle_is_empty(Triangle(vertices[i - 1], vertices[i], vertices[i + 1]), vertices):
                triangles.append(Triangle(vertices[i - 1], vertices[i], vertices[i + 1]))
                vertices.pop(i)
                break
    triangles.append(Triangle(vertices[-1], vertices[0], vertices[1]))
    return triangles
