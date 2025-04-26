import random
import heapq


class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[{'visited': False, 'walls': {'N': True, 'S': True, 'E': True, 'W': True}}
                      for _ in range(width)] for _ in range(height)]

    def generate_maze(self):
        x, y = random.randint(0, self.width - 1), random.randint(0, self.height - 1)
        self.grid[y][x]['visited'] = True

        while self._hunt_and_kill(x, y):
            pass

    def _hunt_and_kill(self, x, y):
        while True:
            neighbors = self._get_unvisited_neighbors(x, y)
            if neighbors:
                nx, ny, direction = random.choice(neighbors)
                self._remove_wall(x, y, direction)
                x, y = nx, ny
                self.grid[y][x]['visited'] = True
            else:
                break

        for j in range(self.height):
            for i in range(self.width):
                if not self.grid[j][i]['visited']:
                    neighbors = self._get_visited_neighbors(i, j)
                    if neighbors:
                        x, y, direction = random.choice(neighbors)
                        self._remove_wall(i, j, direction)
                        self.grid[j][i]['visited'] = True
                        return True
        return False

    def _get_unvisited_neighbors(self, x, y):
        directions = {'N': (0, -1), 'S': (0, 1), 'E': (1, 0), 'W': (-1, 0)}
        neighbors = []
        for d, (dx, dy) in directions.items():
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.width and 0 <= ny < self.height and not self.grid[ny][nx]['visited']:
                neighbors.append((nx, ny, d))
        return neighbors

    def _get_visited_neighbors(self, x, y):
        directions = {'N': (0, -1), 'S': (0, 1), 'E': (1, 0), 'W': (-1, 0)}
        neighbors = []
        for d, (dx, dy) in directions.items():
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.width and 0 <= ny < self.height and self.grid[ny][nx]['visited']:
                neighbors.append((nx, ny, d))
        return neighbors

    def _remove_wall(self, x, y, direction):
        dx, dy = {'N': (0, -1), 'S': (0, 1), 'E': (1, 0), 'W': (-1, 0)}[direction]
        nx, ny = x + dx, y + dy
        self.grid[y][x]['walls'][direction] = False
        opposite = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}
        self.grid[ny][nx]['walls'][opposite[direction]] = False

    def solve_maze(self, start, end):
        def heuristic(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        open_set = []
        heapq.heappush(open_set, (0, start))
        came_from = {}
        g_score = {start: 0}
        f_score = {start: heuristic(start, end)}

        while open_set:
            _, current = heapq.heappop(open_set)

            if current == end:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                return path[::-1]

            x, y = current
            for direction, (dx, dy) in {'N': (0, -1), 'S': (0, 1), 'E': (1, 0), 'W': (-1, 0)}.items():
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height and not self.grid[y][x]['walls'][direction]:
                    neighbor = (nx, ny)
                    tentative_g_score = g_score[current] + 1
                    if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                        came_from[neighbor] = current
                        g_score[neighbor] = tentative_g_score
                        f_score[neighbor] = tentative_g_score + heuristic(neighbor, end)
                        heapq.heappush(open_set, (f_score[neighbor], neighbor))
        return None

    def display_maze(self):
        for y in range(self.height):
            top = ''.join('##' if self.grid[y][x]['walls']['N'] else '# ' for x in range(self.width)) + '#'
            mid = ''.join('# ' if self.grid[y][x]['walls']['W'] else '  ' for x in range(self.width)) + '#'
            print(top)
            print(mid)
        print('#' * (self.width * 2 + 1))


# Example usage
maze = Maze(10, 10)
maze.generate_maze()
maze.display_maze()
start, end = (0, 0), (9, 9)
path = maze.solve_maze(start, end)
print("Path:", path)
