# Genetic Algorithm on Conway's Game Of Life 
Introduction
```
Conway's Game of Life is a cellular automata which mimics the evolution which varies by an initial state.
This game is proven to be Turing Complete and can mimic a turing machine.
Because of that there is an intrest in studying it, and especially different initial states and their evolution.
```
read more at 
[wikiLife](https://conwaylife.com/wiki/Conway%27s_Game_of_Life)

# Example of the Game Of Life
![](https://github.com/EitanF12/Biology12/blob/main/Gospers_glider_gun.gif)

# My project
I have simulated The game of life in board sizes from 10 to 50
On the base of the game I initialized 6 random 4*4 initial states and tracked their growth.
Using a genetic algoriithm I have merged the best Initial states by while the utility is measured by the maximal growth.
The merged initial states were mutated by some chance, eventually improving the utilities drastically and saved the best states.

# Features
* Find and Measures the best random initial states
* Collects statistics about the progression
* Finds the best Initial states using a genetic algorithm which by randomneess finds the best units
* In the end of the process it produces an improvment graph between generations to allow studying and modyfying the algorithm

# Usage

1.To start the genetic algorithm and find configurations
Run the maman12.py in bash:
```bash
python maman12.py
```
2.choose board size and see the cool simulations of the random configurations (:
 now you can see the results of each simulation by the amount of filled cells the the configuration has managed to fill.
 
3.run next simulation to improve the pool of initial configurations
4.press kill to see the improvment between generations.

5.you can run and study each configuration in "metushlahSimulation.py" 
by changing in the main the initial matrix and running
```base
python metushlahSimulation.py
```


# Some cool results



4.To test reconnection, close the client and run it again:
```
./client
```
