import math

import MAP


# def astarHeur(cur_state):
#     # implement Heuristic here
#     return
#
#
# def astarStreet():
#     return
#
#
# def astarHighway():
#     return
#
#
# def astarAll():
#     return


#########################################

# Project A Search / Test Work

def euclidean_distance(x, y):
    result = 0
    for i in range(len(x)):
        result += math.pow(x[i] - y[i], 2)
    return math.sqrt(result)


AVERAGE_SPEED = 40


# how much time it takes (in minutes) to travel the distance (in miles)
# between 2 nodes given the speed limit

# function is directly trained for test data
# def get_speed_between(node, destination_node):
#     if node.name == 'Node A' and destination_node.name == 'Node B':
#         return 20
#     if node.name == 'Node A' and destination_node.name == 'Node C':
#         return 60
#     if node.name == 'Node B' and destination_node.name == 'Node E':
#         return 20
#     if node.name == 'Node C' and destination_node.name == 'Node D':
#         return 50
#     if node.name == 'Node D' and destination_node.name == 'Node E':
#         return 15
#     else:
#         return AVERAGE_SPEED


def heuristic(node, goal):
    # euclidean distance
    distance = euclidean_distance(node.position, goal.position)
    # relative to the average driving speed for our map
    h = distance / (AVERAGE_SPEED / 60)
    return h


def goal_function(node, goal):
    if node == goal:
        return node


def get_path(came_from, start, end):
    reverse_path = [end]
    while end != start:
        end = came_from[end]
        reverse_path.append(end)
    return list(reversed(reverse_path))


def a_search(start, goal):
    # initialize lists
    open_list = []
    closed = []
    # put start node on the open list we need to visit
    open_list.append(start)
    # while there are nodes to explore
    while len(open_list) > 0:
        # get first node off the list (fringe)
        current_node = open_list[0]
        current_index = 0
        # compare to every other node on the fringe and
        # get the node with the smallest f-value
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index
        # pop the node from computed index and
        # put the current node on the closed/visited list
        open_list.pop(current_index)
        closed.append(current_node)

        # if current_node.highway:
        #     return print("Highway Node: ", current_node.name)

        if current_node == goal:
            print("The cost is how many minutes it takes to travel the optimal path to the goal node.")
            print("Cost:", current_node.f)
            path = []
            current = current_node
            while current is not None:
                path.append(current.name)
                print("Node:", current.name, "| f(", current.name, ") =", current.f)
                current = current.parent
            return path[::-1]

        # loop through children
        for child in current_node.neighbors:

            for closed_child in closed:
                if child == closed_child:
                    continue
            g_score = current_node.g + (euclidean_distance(current_node.position, child.position) / (child.speed / 60))
            # if g_score < child.g:
            child.h = euclidean_distance(child.position, goal.position)
            child.g = g_score
            child.f = child.g + child.h
            child.parent = current_node

            # if child not in open_list:
            #    open_list.append(child)

            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            open_list.append(child)


def main():
    # initialize nodes
    # start node
    Node_A = MAP.Node('A', False, (0, 0), 0, None, None, 0, 0, 0)
    Node_B = MAP.Node('B', False, (0, 10), 60, None, None, float('inf'), 0, None)
    Node_C = MAP.Node('C', False, (20, 0), 60, None, None, float('inf'), 0, None)
    Node_D = MAP.Node('D', False, (0, 30), 120, None, None, float('inf'), 0, None)
    Node_E = MAP.Node('E', False, (30, 10), 60, None, None, float('inf'), 0, None)
    Node_F = MAP.Node('F', True, (20, 40), 320, None, None, float('inf'), 0, None)
    Node_G = MAP.Node('G', False, (30, 30), 60, None, None, float('inf'), 0, None)
    Node_H = MAP.Node('H', False, (50, 0), 60, None, None, float('inf'), 0, None)
    Node_I = MAP.Node('I', False, (40, 40), 60, None, None, float('inf'), 0, None)
    Node_J = MAP.Node('J', False, (50, 40), 60, None, None, float('inf'), 0, None)
    Node_K = MAP.Node('K', False, (50, 20), 60, None, None, float('inf'), 0, None)
    Node_Goal = MAP.Node('Goal', False, (50, 30), 60, None, None, float('inf'), 0, None)

    # update heuristics
    # euclidean distance along path to goal with regard to speed limits
    # Node_B.h = euclidean_distance(Node_B.position, Node_Goal.position) / (20 / 60)
    # Node_C.h = euclidean_distance(Node_C.position, Node_Goal.position) / (10 / 60)
    # Node_D.h = euclidean_distance(Node_D.position, Node_Goal.position) / (50 / 60)
    # Node_E.h = euclidean_distance(Node_E.position, Node_Goal.position) / (40 / 60)
    # Node_F.h = euclidean_distance(Node_F.position, Node_Goal.position) / (60 / 60)
    # Node_G.h = euclidean_distance(Node_G.position, Node_Goal.position) / (40 / 60)
    # Node_H.h = euclidean_distance(Node_H.position, Node_Goal.position) / (30 / 60)
    # Node_I.h = euclidean_distance(Node_I.position, Node_Goal.position) / (50 / 60)
    # Node_J.h = euclidean_distance(Node_J.position, Node_Goal.position) / (40 / 60)
    # Node_K.h = euclidean_distance(Node_K.position, Node_Goal.position) / (30 / 60)

    # update neighbors for each node
    Node_A.neighbors = [Node_B, Node_C]
    Node_B.neighbors = [Node_D, Node_E]
    Node_C.neighbors = [Node_F, Node_H]
    Node_D.neighbors = [Node_G]
    Node_E.neighbors = [Node_G]
    Node_F.neighbors = [Node_I]
    Node_G.neighbors = [Node_Goal]
    Node_H.neighbors = [Node_K]
    Node_I.neighbors = [Node_J]
    Node_J.neighbors = [Node_Goal]
    Node_K.neighbors = [Node_Goal]
    Node_Goal.neighbors = None

    # find shortest path from start to goal node
    path = a_search(Node_A, Node_Goal)
    print(path)


if __name__ == '__main__':
    main()

