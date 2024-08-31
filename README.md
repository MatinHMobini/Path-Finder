# 🧩 Maze Solver Game

## Overview

This Python project is a maze solver game where the objective is to find a path through a maze filled with obstacles. The program reads a maze represented by a grid of characters and calculates a valid path from the entrance on the left side to the exit on the right side.

## Features

- **Maze Input**: The maze is provided as a list of strings, where `#` represents blocked cells and `p` represents open paths.
- **Pathfinding**: The program finds a valid path from the entrance (left side) to the exit (right side) of the maze.
- **Path Visualization**: The path is marked with `*` characters to show the route through the maze.

## Example Maze and Output

**Input Maze:**
```
################
#ppppp#pps##pp##
pp###pppp###pp##
#p###pp#p##ppp##
#pppp##pp##ppp##
####p###########
###pp###########
####ppppp#######
########pp####pp
########ppppppp#
################
```

**Output Maze:**
```
################
#ppppp#pps##pp##
**###pppp###pp##
#*###pp#p##ppp##
#****##pp##ppp##
####*###########
###p*###########
####*****#######
########**####**
########p******#
################
```

## How to Use

1. **Input the Maze**: Provide the maze layout as a list of strings.
2. **Run the Solver**: The program will process the maze and find a valid path.
3. **View the Path**: The output will display the maze with the path marked using `*` characters.

Thank you for viewing!
