import matplotlib.pyplot as plt
import random

def sierpinski(points, depth):
    if depth == 0:
        plt.plot([points[0][0], points[1][0]], [points[0][1], points[1][1]], 'k-')
        plt.plot([points[1][0], points[2][0]], [points[1][1], points[2][1]], 'k-')
        plt.plot([points[2][0], points[0][0]], [points[2][1], points[0][1]], 'k-')
    else:
        sierpinski([points[0], get_midpoint(points[0], points[1]), get_midpoint(points[0], points[2])], depth - 1)
        sierpinski([points[1], get_midpoint(points[1], points[2]), get_midpoint(points[1], points[0])], depth - 1)
        sierpinski([points[2], get_midpoint(points[2], points[0]), get_midpoint(points[2], points[1])], depth - 1)

def get_midpoint(point1, point2):
    x = (point1[0] + point2[0]) / 2
    y = (point1[1] + point2[1]) / 2
    return [x, y]

plt.figure(figsize=(8, 8))
points = [[0, 0], [1, 0], [0.5, 0.87]]
sierpinski(points, 5)
plt.axis('off')
plt.show()
