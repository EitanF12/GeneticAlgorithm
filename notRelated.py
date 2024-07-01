#import numpy
#import matplotlib.pyplot as plt
import random
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk

#draw the graph of the function y(t) = A * sin(2Pi * f * t + phase) where f = 100GZ, A = 1, phase = 0, t = 0.01S
def draw_graph():
    f = 100
    A = 1
    phase = 0
    t = np.arange(0, 1, 0.01)
    y = A * np.sin(2 * np.pi * f * t + phase)
    plt.plot(t, y)
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.title("Sine Wave")
    plt.grid(True)
    plt.tight_layout()  # Add this line to make the graph layout more compact
    plt.show()

#main
def main():
    draw_graph()

if __name__ == "__main__":
    main()
