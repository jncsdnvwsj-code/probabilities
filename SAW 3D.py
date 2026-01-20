import random
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def MC_3D(n):
    directions = [(0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0), (0, 0, 1), (0, 0, -1)]
    grid = set()
    x, y, z = 0, 0, 0
    grid.add((x, y, z))
    path = [(x, y, z)]
    for _ in range(n):
        random.shuffle(directions)
        for dx, dy, dz in directions:
            new_x, new_y, new_z = x + dx, y + dy, z + dz
            if (new_x, new_y, new_z) not in grid:
                x, y, z = new_x, new_y, new_z
                grid.add((x, y, z))
                path.append((x, y, z))
                break
    return path

path = MC_3D(100)
x, y, z = zip(*path)

fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, 'o-', markersize=2)
plt.title('3D SAW')
plt.show()