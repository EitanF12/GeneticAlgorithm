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
* Allowes me to test 

# Usage

1.Ensure the following files are deleted on the client:
me.info
defensive.db

2.Run the server in bash:
```bash
python server.py
```
3.Run the client:
```bash
./client
```

4.To test reconnection, close the client and run it again:
```
./client
```
