# Project Node Class

# noinspection PyInitNewSignature
class Node:
    def __init__(self, name, value, highway, position, speed, parent, neighbors, g, h, f):
        self.name = name  # name of the node for printing purposes
        self.value = value  # value of the name
        self.highway = highway  # boolean
        self.position = position  # 2 tuple position on map (used to calculate cost and euclidean dist.)
        self.speed = speed  # value for the speed limit to this node
        self.parent = parent  # list of parent nodes
        self.neighbors = neighbors  # list of neighboring nodes
        self.g = g  # actual cost to node
        self.h = h  # heuristic estimated cost to goal node
        self.f = f  # total cost g + h
