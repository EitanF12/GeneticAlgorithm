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
On the base of the game I initialized 6 random 4*4 initial states and tracked their growth,

# Features
* Supports file transfer in any format up to 512 MB
* Binary protocol for efficient communication
* Python server handling multiple parallel connections
* C++ clients with unique encryption keys for each connection
* Checksum verification for data integrity
* Winsock communication managed by a singleton object
* Factory design pattern for simplified main function and distinct instruction behavior
* SQL database support for allowing reconnections
* Defensive programming to prevent buffer overflows
Vulnerability research of the protocol conducted at the end of the project

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
