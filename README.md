# Final Project Source Code B351

Welcome to the shortest path delivery route project source code!

This is where all the real fun happens.

The contents of the Node.py file include:
- node class

The contents of the Astar.py file include:
- import statements
- constant variables
- euclidean distance function
- heuristic function
- bellman ford function
- astar search function
- main function

# Node.py
The node class defines each node to contain a name, value, highway boolean, its position,
speed to that node, parent node, list of neighbor nodes, g cost to the node, heuristic estimate
to the goal node, and f-value.

# Astar.py
For this file we imported the Node.py file to use the Node class, as well as the math module.

We only had 1 constant variable to initialize at the beginning of this source code and that
was a maximum speed variable that was used in the calculation of our heuristic.

The euclidean distance function was used in the formula to calculate the distance/weight from
a current node to a child node, and again, in the calculation of our heuristic.

Our heuristic function was defined by the time it takes to travel the euclidean distance from
the current node to the goal while traveling at the maximum speed. This function was used in the 
astar search function to help calculate the f-value of the child node.

The Bellman Ford search function was implemented to compare to the astar function, as well as support astar's correctnes.

The astar search function was used to calculate the optimal path from the start node to goal node and show its cost.

Our main function is in place to define our map/graph. This is done by initializing nodes, updating node neighbors,
creating a graph (list of nodes) for the Bellman Ford function, and calling the astar_search and bellman_ford function.

To see the results, we run the main function and print its execution time for insight.
