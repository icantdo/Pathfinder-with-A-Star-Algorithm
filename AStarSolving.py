import heapq
import matplotlib.pyplot as plt

def solve_maze(start, end, height, width, grid, barriers):
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}
    print(f_score)
    print(g_score)

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
        for direction, (dx, dy) in {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}.items():
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height and not grid[y][x]['walls'][direction] and (nx, ny) not in barriers:
                neighbor = (nx, ny)
                tentative_g_score = g_score[current] + 1
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, end)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
    return None

def display_maze(grid, width, height, path=None):
    fig, ax = plt.subplots(figsize=(width, height))

    for y in range(height):
        for x in range(width):
            if not grid[y][x]['walls']['N']:
                ax.plot([x, x], [y, y + 1], 'k-')
            if not grid[y][x]['walls']['S']:
                ax.plot([x, x], [y, y - 1], 'k-')
            if not grid[y][x]['walls']['W']:
                ax.plot([x, x - 1], [y, y], 'k-')
            if not grid[y][x]['walls']['E']:
                ax.plot([x, x + 1], [y, y], 'k-')

    if path:
        px, py = zip(*path)
        ax.plot(px, py, 'r-', linewidth=2)

    plt.show()


grid = [ # y = 0
    [
        {'walls': {'N': False, 'S': True, 'E': False, 'W': True}}, # x = 0
        {'walls': {'N': False, 'S': True, 'E': False, 'W': False}}, # x = 1
        {'walls': {'N': False, 'S': True, 'E': False, 'W': False}}, # x = 2
        {'walls': {'N': False, 'S': True, 'E': False, 'W': False}}, # x = 3
        {'walls': {'N': False, 'S': True, 'E': False, 'W': False}}, # x = 4
        {'walls': {'N': False, 'S': True, 'E': True, 'W': False}}, # x = 5
    ],
    [
        {'walls': {'N': False, 'S': False, 'E': True, 'W': True}}, # x = 0
        {'walls': {'N': False, 'S': False, 'E': True, 'W': True}}, # x = 1
        {'walls': {'N': False, 'S': False, 'E': True, 'W': True}}, # x = 2
        {'walls': {'N': False, 'S': False, 'E': True, 'W': True}}, # x = 3
        {'walls': {'N': False, 'S': False, 'E': True, 'W': True}}, # x = 4
        {'walls': {'N': False, 'S': False, 'E': True, 'W': True}}, # x = 5
    ],
    [
        {'walls': {'N': False, 'S': False, 'E': True, 'W': True}},  # x = 0
        {'walls': {'N': False, 'S': False, 'E': True, 'W': True}},  # x = 1
        {'walls': {'N': False, 'S': False, 'E': True, 'W': True}},  # x = 2
        {'walls': {'N': False, 'S': False, 'E': True, 'W': True}},  # x = 3
        {'walls': {'N': False, 'S': False, 'E': True, 'W': True}},  # x = 4
        {'walls': {'N': False, 'S': False, 'E': True, 'W': True}},  # x = 5
    ],
    [
        {'walls': {'N': False, 'S': False, 'E': True, 'W': True}},  # x = 0
        {'walls': {'N': False, 'S': False, 'E': True, 'W': True}},  # x = 1
        {'walls': {'N': False, 'S': False, 'E': True, 'W': True}},  # x = 2
        {'walls': {'N': False, 'S': False, 'E': True, 'W': True}},  # x = 3
        {'walls': {'N': False, 'S': False, 'E': True, 'W': True}},  # x = 4
        {'walls': {'N': False, 'S': False, 'E': True, 'W': True}},  # x = 5
    ],
    [
        {'walls': {'N': False, 'S': False, 'E': True, 'W': True}},  # x = 0
        {'walls': {'N': False, 'S': False, 'E': True, 'W': True}},  # x = 1
        {'walls': {'N': False, 'S': False, 'E': True, 'W': True}},  # x = 2
        {'walls': {'N': False, 'S': False, 'E': True, 'W': True}},  # x = 3
        {'walls': {'N': False, 'S': False, 'E': True, 'W': True}},  # x = 4
        {'walls': {'N': False, 'S': False, 'E': True, 'W': True}},  # x = 5
    ],
    [
        {'walls': {'N': True, 'S': False, 'E': False, 'W': True}},  # x = 0
        {'walls': {'N': True, 'S': False, 'E': False, 'W': False}},  # x = 1
        {'walls': {'N': True, 'S': False, 'E': False, 'W': False}},  # x = 2
        {'walls': {'N': True, 'S': False, 'E': False, 'W': False}},  # x = 3
        {'walls': {'N': True, 'S': False, 'E': False, 'W': False}},  # x = 4
        {'walls': {'N': True, 'S': False, 'E': True, 'W': False}},  # x = 5
    ]
]


start, end = (0, 0), (2,4)
display_maze(grid, width=6, height=6)
path = solve_maze(start, end, height=6, width=6, grid=grid , barriers= [(1, 0)])
display_maze(grid, width=6, height=6, path=path)
print(path)