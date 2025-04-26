# Maze Pathfinding Project

## Overview
This project implements a basic **A\* pathfinding algorithm** to solve a maze represented as a grid.
It also provides a simple visualization of the maze and the path found using **Matplotlib**.

## Features
- Maze representation with configurable walls for each cell (North, South, East, West).
- A\* algorithm for efficient shortest path finding.
- Ability to add barriers (blocked cells) dynamically.
- Visualization of the maze structure and the computed path.

## Requirements
- Python 3.x
- `matplotlib` library

You can install `matplotlib` via pip if you don't have it:
```bash
pip install matplotlib
```

## How It Works
- The maze is defined as a 2D list of dictionaries, where each dictionary specifies the walls of a cell.
- The `solve_maze` function:
  - Uses A\* search to find the shortest path from a start point to an end point, considering walls and barriers.
- The `display_maze` function:
  - Visualizes the maze grid.
  - If a path is found, it is drawn on the maze.

## Files
- `solve_maze(start, end, height, width, grid, barriers)`  
  Finds the shortest path between the `start` and `end` points.

- `display_maze(grid, width, height, path=None)`  
  Draws the maze and optionally the solution path.

## Example Usage
```python
start, end = (0, 0), (2, 4)
display_maze(grid, width=6, height=6)
path = solve_maze(start, end, height=6, width=6, grid=grid, barriers=[(1, 0)])
display_maze(grid, width=6, height=6, path=path)
print(path)
```

## Notes
- The maze must be manually defined, including walls for each cell.
- The algorithm prints out `g_score` and `f_score` dictionaries during execution for debugging purposes.
- Barriers are additional blocks inside the maze not related to walls.
- Path will not be found if start and end are completely blocked.
