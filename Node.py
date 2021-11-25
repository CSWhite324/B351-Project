
# Project Node Class

class Node:
    def __init__(self, name, position, parent, neighbors, g, h, f):
        self.name = name  # name of the node for printing purposes
        self.position = position  # 2 tuple position on map (used to calculate cost and euclidean dist.)
        self.parent = parent  # list of parent nodes
        self.neighbors = neighbors  # list of neighboring nodes
        self.g = g  # actual cost to node
        self.h = h  # heuristic estimated cost to goal node
        self.f = f  # total cost g + h
