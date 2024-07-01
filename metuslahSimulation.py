import tkinter as tk
from tkinter import simpledialog, messagebox
import matplotlib.pyplot as plt
import random
#Eitan 
def generate_random_configuration(size=4):
    return [[random.randint(0, 1) for _ in range(size)] for _ in range(size)]

def initialize_grid(grid_size, initial_pattern):
    grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    start_x = (grid_size - len(initial_pattern)) // 2
    start_y = (grid_size - len(initial_pattern)) // 2
    for i, row in enumerate(initial_pattern):
        for j, cell in enumerate(row):
            grid[start_y + i][start_x + j] = cell
    return grid

def update_grid(grid, grid_size):
    new_grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    for i in range(grid_size):
        for j in range(grid_size):
            live_neighbors = sum(
                grid[i + x][j + y] for x in (-1, 0, 1) for y in (-1, 0, 1)
                if 0 <= i + x < grid_size and 0 <= j + y < grid_size and (x != 0 or y != 0)
            )
            if grid[i][j] == 1 and live_neighbors in (2, 3):
                new_grid[i][j] = 1
            elif grid[i][j] == 0 and live_neighbors == 3:
                new_grid[i][j] = 1
    return new_grid

def draw_grid(canvas, grid, cell_size=20):
    canvas.delete("all")
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            color = "black" if cell == 1 else "white"
            canvas.create_rectangle(j * cell_size, i * cell_size, (j + 1) * cell_size, (i + 1) * cell_size, fill=color, outline="gray")

def run_simulation(canvas, grid, live_cells_count, stage=0, auto=False):
    if stage < 50:
        draw_grid(canvas, grid, 20)
        live_cells_count.append(sum(cell for row in grid for cell in row))
        grid[:] = update_grid(grid, len(grid))
        if auto:
            canvas.after(100, lambda: run_simulation(canvas, grid, live_cells_count, stage + 1, auto))
    else:
        plt.figure(figsize=(10, 5))
        plt.plot(range(len(live_cells_count)), live_cells_count, marker='o')
        plt.title("Live Cells Over Time")
        plt.xlabel("Stage")
        plt.ylabel("Number of Live Cells")
        plt.grid(True)
        plt.show()

def main():
    root = tk.Tk()
    root.title("Game of Life Simulation")

    grid_size = simpledialog.askinteger("Grid Size", "Choose grid size (10 or 50):", minvalue=10, maxvalue=50, parent=root)

    if grid_size is None:
        root.destroy()
        return

    initial_pattern = [[1, 1, 0, 0,1], [1,0, 1, 1, 1], [1, 1, 1, 0,0], [0,0, 0, 0, 1],[0,1,1,0,0]]
    grid = initialize_grid(grid_size, initial_pattern)
    live_cells_count = []

    canvas = tk.Canvas(root, width=grid_size*20, height=grid_size*20)
    canvas.pack()

    tk.Button(root, text="Run All Stages", command=lambda: run_simulation(canvas, grid, live_cells_count, auto=True)).pack(side=tk.LEFT)
    tk.Button(root, text="Next Stage", command=lambda: run_simulation(canvas, grid, live_cells_count)).pack(side=tk.LEFT)
    tk.Button(root, text="Kill", command=root.destroy).pack(side=tk.RIGHT)

    root.mainloop()

if __name__ == "__main__":
    main()
