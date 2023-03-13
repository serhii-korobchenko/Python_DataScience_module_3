# In this version, the sierpinski function takes a list of points
# and a depth as arguments. If the depth is 0, it draws the triangle
# using plt.scatter with a size of 50 and color black, otherwise it
# recursively calls itself with the midpoints of each pair of points.
#
# The get_midpoint function calculates the midpoint between two points
# using their x and y coordinates.
#
# The plt.figure command creates a blank plot with a size of 8x8 inches.
# The plt.axis command turns off the axis labels and ticks, and the plt.show
# command displays the final plot.


import matplotlib.pyplot as plt
import random

def sierpinski(points, depth):
    if depth == 0:
        plt.scatter([points[0][0], points[1][0], points[2][0]],
                    [points[0][1], points[1][1], points[2][1]],
                    s=50, color='k')
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
