import matplotlib.pyplot as plt
import random

def sierpinski(points, depth):
    colors = ['r', 'g', 'b']
    if depth > 0:
        for i in range(1000):
            point = random.choice(points)
            x = (point[0] + random.uniform(-1, 1)) / 2
            y = (point[1] + random.uniform(-1, 1)) / 2
            points.append([x, y])
            plt.scatter(x, y, color=colors[depth % 3])
        sierpinski(points[:3], depth - 1)

plt.figure(figsize=(8, 8))
plt.axis('off')
points = [[0, 0], [1, 0], [0.5, 0.87]]
sierpinski(points, 5)
plt.show()
