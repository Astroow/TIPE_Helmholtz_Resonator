from mesh.mesh import triangulation
from turtle import *

from objects.Mesh.Point import Point

# Initialize vertices
VERTICES = [
    (0, 0),
    (0, 50),
    (90, 50),
    (90, 85),
    (75, 85),
    (75, 135),
    (125, 135),
    (125, 85),
    (110, 85),
    (110, 50),
    (200, 50),
    (200, 0)
]
VERTICES = [Point(vertex[0], vertex[1]) for vertex in VERTICES]

# Initialize turtle
screensize(1000, 1000)
hideturtle()
penup()

# Plot vertices
goto(VERTICES[0].x, VERTICES[0].y)
pendown()
for vertex in VERTICES:
    goto(vertex.x, vertex.y)
goto(VERTICES[0].x, VERTICES[0].y)
penup()

# Compute triangles
TRIANGLES = triangulation(VERTICES)

# Plot triangles
for triangle in TRIANGLES:
    goto(triangle.v1.x, triangle.v1.y)
    pendown()
    goto(triangle.v2.x, triangle.v2.y)
    goto(triangle.v3.x, triangle.v3.y)
    goto(triangle.v1.x, triangle.v1.y)
    penup()

end_fill()
done()
