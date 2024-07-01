import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
import random

#Eitan 

# Global variables to track evaluations per generation
max_evaluations_per_generation = []
average_evaluations_per_generation = []

# Function to generate a random configuration
def generate_random_configuration(size=4):
    return [[random.randint(0, 1) for _ in range(size)] for _ in range(size)]

# Function to initialize the grid with an initial pattern
def initialize_grid(grid_size, initial_pattern):
    grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    start_x = (grid_size - len(initial_pattern[0])) // 2
    start_y = (grid_size - len(initial_pattern)) // 2
    for i, row in enumerate(initial_pattern):
        for j, cell in enumerate(row):
            grid[start_y + i][start_x + j] = cell
    return grid

# Function to update the grid based on the rules of the game
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

# Function to draw the grid on the canvas
def draw_grid(canvas, grid, cell_size=20):
    canvas.delete("all")
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            color = "black" if cell == 1 else "white"
            canvas.create_rectangle(j * cell_size, i * cell_size, (j + 1) * cell_size, (i + 1) * cell_size, fill=color, outline="gray")

# Function to run the simulation and return the evaluation percentages
def run_simulation(canvas, grid_size, initial_pattern):
    grid = initialize_grid(grid_size, initial_pattern)
    evaluations = []

    for stage in range(50):
        grid = update_grid(grid, grid_size)
        draw_grid(canvas, grid, 20)
        black_cells = sum(cell for row in grid for cell in row)
        total_cells = grid_size ** 2
        evaluation_percentage = (black_cells / total_cells) * 100
        evaluations.append(evaluation_percentage)
        canvas.update()
        canvas.after(5)

    return evaluations

# Function to plot the evaluation graph
def plot_evaluation_graph(evaluations):
    plt.figure(figsize=(10, 5))
    plt.plot(range(len(evaluations)), evaluations, marker='o')
    plt.title("Evaluation Over Time")
    plt.xlabel("Stage")
    plt.ylabel("Black Cells Percentage")
    plt.grid(True)
    plt.show()

# Function to view a configuration on a separate window
def view_configuration(config, grid_size):
    top_window = tk.Toplevel()
    top_window.title("Configuration View")
    canvas = tk.Canvas(top_window, width=grid_size*20, height=grid_size*20)
    canvas.pack()
    draw_grid(canvas, config, 20)

# Function to calculate the chances for each configuration based on their evaluations
def calculate_chances(evaluations):
    total_evaluation = sum(evaluation for _, evaluation, _ in evaluations)
    chances = [evaluation / total_evaluation for _, evaluation, _ in evaluations]
    return chances

# Function to select configuration pairs for the next generation
def select_configuration_pairs(evaluations, chances):
    indexes = np.random.choice(len(evaluations), 6, replace=False, p=chances)
    return [evaluations[indexes[i]][0] for i in range(6)]

# Function to merge two configurations
def merge_configurations(config1, config2):
    half = len(config1) // 2
    new_config1 = config1[:half] + config2[half:]
    new_config2 = config2[:half] + config1[half:]
    return new_config1, new_config2

# Function to mutate a configuration
def mutate_configuration(config, mutation_chance):
    mutated_config = []
    for row in config:
        mutated_row = [(cell if random.random() > mutation_chance else 1-cell) for cell in row]
        mutated_config.append(mutated_row)
    return mutated_config

# Function to run the configurations for each generation
def run_configurations(previous_evaluations=None):
    global results_window, grid_size, max_evaluations_per_generation, average_evaluations_per_generation
    if results_window:
        results_window.destroy()

    results_window = tk.Toplevel()
    results_window.title("Results")

    configurations = []
    mutation_chances = [0.1, 0.2, 0.3]  # Mutation chances for each pair

    if previous_evaluations:
        chances = calculate_chances(previous_evaluations)
        selected_configs = select_configuration_pairs(previous_evaluations, chances)

        for i in range(0, 6, 2):  # Process pairs
            new_config1, new_config2 = merge_configurations(selected_configs[i], selected_configs[i+1])
            mutation_chance = mutation_chances[i//2]
            new_config1 = mutate_configuration(new_config1, mutation_chance)
            new_config2 = mutate_configuration(new_config2, mutation_chance)
            configurations.extend([new_config1, new_config2])
    else:
        configurations = [generate_random_configuration(4) for _ in range(6)]  # Initial configurations

    evaluations = []

    for i, config in enumerate(configurations):
        window = tk.Toplevel()
        window.title(f"Configuration {i+1}")
        canvas = tk.Canvas(window, width=grid_size*20, height=grid_size*20)
        canvas.pack()

        evals = run_simulation(canvas, grid_size, config)
        evaluations.append((config, max(evals), evals))

        window.destroy()

    # Update max and average evaluations for this generation
    best_evaluation_this_gen = max(evaluation for _, evaluation, _ in evaluations)
    average_evaluation_this_gen = np.mean([evaluation for _, evaluation, _ in evaluations])
    max_evaluations_per_generation.append(best_evaluation_this_gen)
    average_evaluations_per_generation.append(average_evaluation_this_gen)

    evaluations.sort(key=lambda x: x[1], reverse=True)

    for i, (config, max_eval, evals) in enumerate(evaluations):
        tk.Button(results_window, text=f"View Configuration {i+1} (Max Eval: {max_eval:.2f}%)",
                  command=lambda c=config, gs=grid_size: view_configuration(c, gs)).pack()
        tk.Button(results_window, text=f"View Graph {i+1}",
                  command=lambda e=evals: plot_evaluation_graph(e)).pack()

    tk.Button(results_window, text="Run Next Generation", command=lambda: run_configurations(evaluations)).pack()
    tk.Button(results_window, text="Kill", command=lambda: [plot_generational_changes(), root.destroy()]).pack()

# Function to plot the generational changes
def plot_generational_changes():
    generations = range(1, len(max_evaluations_per_generation) + 1)
    if max_evaluations_per_generation:
        plt.figure(figsize=(12, 6))

        # Plotting the best evaluations
        plt.plot(generations, max_evaluations_per_generation, marker='o', linestyle='-', color='b', label='Best Evaluation')

        # Plotting the average evaluations
        plt.plot(generations, average_evaluations_per_generation, marker='x', linestyle='--', color='r', label='Average Evaluation')

        plt.title("Evaluation Over Generations")
        plt.xlabel("Generation")
        plt.ylabel("Evaluation (%)")
        plt.xticks(generations)
        plt.legend()
        plt.grid(True)
        plt.show()
    else:
        messagebox.showinfo("Info", "No generational data to plot.")

# Main function
def main():
    global root, grid_size, results_window
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    grid_size = simpledialog.askinteger("Grid Size", "Choose grid size (10 or 50):", minvalue=10, maxvalue=50, parent=root)

    if grid_size is None:
        return

    results_window = None
    run_configurations()

    root.mainloop()

if __name__ == "__main__":
    main()
