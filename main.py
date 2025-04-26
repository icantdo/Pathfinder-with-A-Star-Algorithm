import random
import numpy as np
import matplotlib.pyplot as plt
from collections import deque


class HuntAndKillMaze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = np.ones((height, width), dtype=int)  # 1 for walls, 0 for paths
        self.visited = np.zeros((height, width), dtype=bool)
        self.start = (1, 1)
        self.end = (height - 2, width - 2)

    def get_neighbors(self, x, y):
        directions = [(0, -2), (0, 2), (-2, 0), (2, 0)]  # Up, Down, Left, Right
        random.shuffle(directions)
        neighbors = []

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 < nx < self.height - 1 and 0 < ny < self.width - 1 and not self.visited[nx, ny]:
                neighbors.append((nx, ny))
        return neighbors

    def carve_path(self, x, y, nx, ny):
        self.grid[x, y] = 0
        self.grid[nx, ny] = 0
        self.grid[(x + nx) // 2, (y + ny) // 2] = 0  # Remove wall between

    def generate_maze(self):
        x, y = random.randrange(1, self.height, 2), random.randrange(1, self.width, 2)
        self.visited[x, y] = True
        self.grid[x, y] = 0

        while True:
            neighbors = self.get_neighbors(x, y)
            if neighbors:
                nx, ny = random.choice(neighbors)
                self.carve_path(x, y, nx, ny)
                self.visited[nx, ny] = True
                x, y = nx, ny
            else:
                found = False
                for i in range(1, self.height, 2):
                    for j in range(1, self.width, 2):
                        if not self.visited[i, j]:
                            for dx, dy in [(0, -2), (0, 2), (-2, 0), (2, 0)]:
                                ni, nj = i + dx, j + dy
                                if 0 < ni < self.height - 1 and 0 < nj < self.width - 1 and self.visited[ni, nj]:
                                    self.carve_path(i, j, ni, nj)
                                    self.visited[i, j] = True
                                    x, y = i, j
                                    found = True
                                    break
                            if found:
                                break
                    if found:
                        break
                if not found:
                    break

        # Ensure start and end points are open
        self.grid[self.start] = 0
        self.grid[self.end] = 0

    def display_maze(self):
        plt.figure(figsize=(10, 10))
        plt.imshow(self.grid, cmap='binary')
        plt.xticks([])
        plt.yticks([])

        # Mark start and end points
        plt.scatter(self.start[1], self.start[0], color='green', s=100, label='Start')
        plt.scatter(self.end[1], self.end[0], color='red', s=100, label='End')
        plt.legend()

        plt.show()


class BFSSolver:
    def __init__(self, maze):
        self.maze = maze.grid
        self.start = maze.start
        self.end = maze.end
        self.path = []

    def solve(self):
        queue = deque([(self.start, [])])  # (current position, path taken)
        visited = set()
        visited.add(self.start)

        while queue:
            (x, y), path = queue.popleft()
            path.append((x, y))

            if (x, y) == self.end:
                self.path = path
                return path

            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if (nx, ny) not in visited and self.maze[nx, ny] == 0:
                    visited.add((nx, ny))
                    queue.append(((nx, ny), path.copy()))
        return []

    def display_solution(self):
        solution_grid = np.copy(self.maze)
        for x, y in self.path:
            solution_grid[x, y] = 10

        plt.figure(figsize=(10, 10))
        plt.imshow(solution_grid, cmap='gray')
        plt.xticks([])
        plt.yticks([])

        # Mark start and end points
        plt.scatter(self.start[1], self.start[0], color='green', s=100, label='Start')
        plt.scatter(self.end[1], self.end[0], color='red', s=100, label='End')
        plt.legend()

        plt.show()


# Example Usage
width, height = 441, 441 #Actually that to be 21, 21 but I want bigger bc I can do
maze = HuntAndKillMaze(width, height)
maze.generate_maze()
maze.display_maze()

solver = BFSSolver(maze)
solver.solve()
solver.display_solution()
