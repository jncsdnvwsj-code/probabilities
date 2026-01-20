import random
import numpy as np
import matplotlib.pyplot as plt

def MC_2D(n):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    grid = set()
    x, y = 0, 0
    grid.add((x, y))
    path = [(x, y)]
    for _ in range(n):
        random.shuffle(directions)
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if (new_x, new_y) not in grid:
                x, y = new_x, new_y
                grid.add((x, y))
                len(grid)
                len(path)
                path.append((x, y))
                break
    return path

n = 10000

path = MC_2D(n)
x, y = zip(*path)

print(len(path))

plt.figure(figsize=(10, 10))
plt.plot(x, y, 'o-', markersize=1)
plt.title('2D SAW')
plt.show()

def avg_distance(path):
    distances = [np.sqrt(x**2 + y**2) for x, y in path]
    return np.mean(distances)

def ending_proba(path, n):
    return len(path) / n

avg_distance = avg_distance(path)
print(f"{avg_distance}")

ending_proba = ending_proba(path, n)
print(f"{ending_proba}")