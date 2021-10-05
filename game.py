import os
import time

SEED = "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n" \
       "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n" \
       "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n" \
       "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n" \
       "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n" \
       "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][X][X][X][X][X][X][X][X][X][X][X][X][X][X]\n" \
       "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n" \
       "[X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X]\n" \
       "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n" \
       "[X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X]\n" \
       "[ ][ ][ ][ ][ ][ ][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][ ][ ][ ][ ]\n" \
       "[X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n" \
       "[X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X]\n" \
       "[X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X]\n" \
       "[ ][ ][ ][ ][ ][ ][ ][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X]\n" \
       "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n" \
       "[ ][ ][ ][ ][ ][ ][ ][X][X][X][X][X][X][X][X][X][X][ ][ ][ ][ ][ ][ ][ ][ ]\n" \
       "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][X][X][X][X][X][X][X][X][X][X][X][X][X][X]\n" \
       "[X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X]\n" \
       "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n" \
       "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][X][X][X][X][X][X][X][X][X][X][X][X][X]\n" \
       "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n" \
       "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n" \
       "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n" \
       "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]"


def start_game():
    grid = construct_initial_grid(SEED)
    print_grid(grid)
    while True:
        clear_screen()
        grid = construct_and_update_grid(grid)
        print_grid(grid)
        time.sleep(0.1)

def construct_initial_grid(seed_string):
    grid = []
    row = 0
    for line in seed_string.split("\n"):
        col = 0
        for elem in get_cell_value(line):
            if elem == "[X]":
                grid.append((int(row), int(col)))
            col += 1
        row += 1
    return grid

def get_cell_value(line):
    elements = []
    str = ""
    for char in line:
        if char != ']':
            str += char
        else:
            str += char
            elements.append(str)
            str = ""
    return elements

def construct_and_update_grid(board):
    grid = []
    neighbors = get_neighbors_with_count(board)
    for neighbor in neighbors:
        neighbor_count = neighbors[neighbor]
        if neighbor_count == 3:
            if neighbor not in grid:
                grid.append(neighbor)
        if neighbor_count == 2:
            if neighbor in board:
                if neighbor not in grid:
                    grid.append(neighbor)
    return grid

def get_neighbors_with_count(grid):
    neighbor_counts = {}
    for cell in grid:
        for neighbor in get_neighbors(cell):
            if neighbor in neighbor_counts:
                neighbor_counts[neighbor] += 1
            else:
                neighbor_counts[neighbor] = 1
    return neighbor_counts

def get_neighbors(cell):
    neighbors = []
    row, col = cell
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if (i, j) != (row, col):
                neighbors.append((i, j))
    return neighbors

def clear_screen():
    try:
        os.system('clear')
    except:
        os.system('cls')

def print_grid(grid):
    if grid:
        grid_string = generate_grid_string(grid)
        print(grid_string)

def generate_grid_string(grid):
    grid_string = ""
    for row in range(0, 25):
        for col in range(0, 25):
            grid_string += "[X]" if (row, col) in grid else "[ ]"
        grid_string += "\n"
    return grid_string

def get_columns_positions(grid):
    positions = []
    for (col, row) in grid:
        positions.append(col)
    return positions

def get_rows_positions(grid):
    positions = []
    for (col, row) in grid:
        positions.append(row)
    return positions

start_game()