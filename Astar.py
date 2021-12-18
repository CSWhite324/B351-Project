import math
import Node

#########################################

# Project A Search / Test Work

MAX_SPEED = 70


def euclidean_distance(x, y):
    result = 0
    for i in range(len(x)):
        result += math.pow(x[i] - y[i], 2)
    return math.sqrt(result)


# how much time it takes (in minutes) to travel the distance (in miles)
# between the node and goal node traveling at the maximum speed
def heuristic(node, goal):
    # euclidean distance
    distance = euclidean_distance(node.position, goal.position)
    # relative to the max driving speed for our map
    h = distance / (MAX_SPEED / 60)
    return h

# this code has been developed around the implementation found on the "Bellman–Ford algorithm"
# article on Wikipedia.
# URL: https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm#Applications_in_routing
# quick note: this algorithm does not check for negative weight cycles,
# unlike common implementations, because of our graph
def bellman_ford(graph, source):
    # initialize lists so distance is infinite and predecessor is None
    distance = [float('inf')] * len(graph)
    pred = [None] * len(graph)

    # distance to source is 0
    distance[source.value - 1] = 0
    # print(distance)
    # print(pred)

    # relaxing edges V (# of nodes) - 1 times
    for i in range(len(graph) - 1):
        for node in graph:
            for child in node.neighbors:
                # set the weight (calculated distance to child node)
                weight = (euclidean_distance(node.position, child.position) / (child.speed / 60))
                # if a shorter path to a node is found, update its distance on the list
                if distance[node.value - 1] + weight < distance[child.value - 1]:
                    distance[child.value - 1] = distance[node.value - 1] + weight
                    pred[child.value - 1] = node
    # this is a specific print statement to show the distance between the start node
    # in this case Node_11, which is why distance[10] is called because it is placed
    # in the node.value - 1 position, and the goal node, which in this setup will be the last
    # node on the list. this must be adjusted to see results of different variations.
    return print("Distance to source (should be 0):", distance[10], "| Distance to goal:", distance[len(graph) - 1])


def astar_search(start, goal):
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
            print("The cost is how many minutes it takes to travel the optimal path from the start to the goal node.")
            print("Cost:", current_node.f, "minutes")

            # for printing path
            path = []
            current = current_node
            while current is not None:
                path.append(current.name)
                print("Node:", current.name, "| f(", current.name, ") =", current.f)
                current = current.parent
            return path[::-1]

        # loop through children
        for child in current_node.neighbors:

            # check for visited children
            for closed_child in closed:
                if child == closed_child:
                    continue
            # update the child
            g_score = current_node.g + (euclidean_distance(current_node.position, child.position) / (child.speed / 60))
            child.h = heuristic(child, goal)  # euclidean_distance(child.position, goal.position) / (MAX_SPEED/60)
            child.g = g_score
            child.f = child.g + child.h
            child.parent = current_node

            # check for finding a shorter path to a node
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            open_list.append(child)


def main():
    # initialize nodes

    Node_1 = Node.Node('1', 1, False, (0, 2), 50, None, None, float('inf'), 0, None)
    Node_2 = Node.Node('2', 2, True, (.4, 2), 60, None, None, float('inf'), 0, None)
    Node_3 = Node.Node('3', 3, True, (.8, 2), 70, None, None, float('inf'), 0, None)
    Node_4 = Node.Node('4', 4, False, (.4, 1.8), 30, None, None, float('inf'), 0, None)
    Node_5 = Node.Node('5', 5, False, (.8, 1.8), 30, None, None, float('inf'), 0, None)
    Node_6 = Node.Node('6', 6, False, (.1, 1.5), 40, None, None, float('inf'), 0, None)
    Node_7 = Node.Node('7', 7, False, (.4, 1.5), 30, None, None, float('inf'), 0, None)
    Node_8 = Node.Node('8', 8, False, (.8, 1.5), 10, None, None, float('inf'), 0, None)
    Node_9 = Node.Node('9', 9, False, (1.33, 1.5), 20, None, None, float('inf'), 0, None)
    Node_10 = Node.Node('10', 10, True, (1.5, 1.5), 70, None, None, float('inf'), 0, None)
    # Start Node
    Node_11 = Node.Node('11', 11, False, (.1, 1), 30, None, None, 0, 0, 0)

    Node_12 = Node.Node('12', 12, False, (.66, 1), 10, None, None, float('inf'), 0, None)
    Node_13 = Node.Node('13', 13, False, (.1, .8), 30, None, None, float('inf'), 0, None)
    Node_14 = Node.Node('14', 14, False, (.5, .8), 30, None, None, float('inf'), 0, None)
    Node_15 = Node.Node('15', 15, False, (.8, .8), 10, None, None, float('inf'), 0, None)
    Node_16 = Node.Node('16', 16, False, (1, .8), 10, None, None, float('inf'), 0, None)
    Node_17 = Node.Node('17', 17, False, (1.4, .8), 10, None, None, float('inf'), 0, None)
    Node_18 = Node.Node('18', 18, True, (1.8, .8), 70, None, None, float('inf'), 0, None)
    Node_19 = Node.Node('19', 19, False, (.5, .6), 30, None, None, float('inf'), 0, None)
    Node_20 = Node.Node('20', 20, False, (1.4, .6), 30, None, None, float('inf'), 0, None)
    Node_21 = Node.Node('21', 21, False, (1.7, .6), 30, None, None, float('inf'), 0, None)
    Node_22 = Node.Node('22', 22, False, (.1, .3), 30, None, None, float('inf'), 0, None)
    Node_23 = Node.Node('23', 23, False, (.5, .3), 30, None, None, float('inf'), 0, None)
    Node_24 = Node.Node('24', 24, False, (.8, .3), 30, None, None, float('inf'), 0, None)
    Node_25 = Node.Node('25', 25, False, (1, .3), 30, None, None, float('inf'), 0, None)
    Node_26 = Node.Node('26', 26, False, (1.2, .3), 30, None, None, float('inf'), 0, None)
    Node_27 = Node.Node('27', 27, False, (1.4, .4), 30, None, None, float('inf'), 0, None)
    Node_28 = Node.Node('28', 28, False, (1.7, .4), 30, None, None, float('inf'), 0, None)
    # Origin (0,0)
    Node_29 = Node.Node('29', 29, False, (0, 0), 20, None, None, float('inf'), 0, None)

    Node_30 = Node.Node('30', 30, False, (.1, 0), 30, None, None, float('inf'), 0, None)
    Node_31 = Node.Node('31', 31, False, (.5, 0), 30, None, None, float('inf'), 0, None)
    Node_32 = Node.Node('32', 32, False, (.8, .15), 30, None, None, float('inf'), 0, None)
    Node_33 = Node.Node('33', 33, False, (1, .15), 30, None, None, float('inf'), 0, None)
    Node_34 = Node.Node('34', 34, False, (1.2, .15), 30, None, None, float('inf'), 0, None)
    Node_35 = Node.Node('35', 35, False, (1.4, .15), 30, None, None, float('inf'), 0, None)
    Node_36 = Node.Node('36', 36, False, (1, 0), 30, None, None, float('inf'), 0, None)
    Node_37 = Node.Node('37', 37, False, (0, 1.5), 10, None, None, float('inf'), 0, None)
    Node_38 = Node.Node('38', 38, True, (2, .3), 55, None, None, float('inf'), 0, None)
    Node_39 = Node.Node('39', 39, False, (1.8, .3), 30, None, None, float('inf'), 0, None)
    Node_40 = Node.Node('40', 40, False, (1.8, 0), 30, None, None, float('inf'), 0, None)
    Node_41 = Node.Node('41', 41, False, (1.4, .3), 30, None, None, float('inf'), 0, None)
    # Goal Node
    Node_Goal = Node.Node('Goal', 42, False, (1.9, 0), 30, None, None, float('inf'), 0, None)

    # update neighbors for each node
    Node_1.neighbors = [Node_2]
    Node_2.neighbors = [Node_3]
    Node_3.neighbors = [Node_10]
    Node_4.neighbors = [Node_2]
    Node_5.neighbors = [Node_3]
    Node_6.neighbors = [Node_1, Node_37]
    Node_7.neighbors = [Node_4, Node_8, Node_12]
    Node_8.neighbors = [Node_5, Node_9, Node_15]
    Node_9.neighbors = [Node_10, Node_16]
    Node_10.neighbors = [Node_18]
    # Start Node
    Node_11.neighbors = [Node_6, Node_12]

    Node_12.neighbors = [Node_8, Node_15]
    Node_13.neighbors = [Node_11]
    Node_14.neighbors = [Node_13, Node_15, Node_19]
    Node_15.neighbors = [Node_16]
    Node_16.neighbors = [Node_17]
    Node_17.neighbors = [Node_18, Node_20]
    Node_18.neighbors = [Node_38]
    Node_19.neighbors = [Node_23]
    Node_20.neighbors = [Node_21, Node_27]
    Node_21.neighbors = [Node_28]
    Node_22.neighbors = [Node_13]
    Node_23.neighbors = [Node_22]
    Node_24.neighbors = [Node_23, Node_32]
    Node_25.neighbors = [Node_24, Node_33]
    Node_26.neighbors = [Node_25]
    Node_27.neighbors = [Node_41]
    Node_28.neighbors = [Node_39]
    Node_29.neighbors = [Node_30]
    Node_30.neighbors = [Node_31]
    Node_31.neighbors = [Node_36]
    Node_32.neighbors = [Node_33]
    Node_33.neighbors = [Node_34]
    Node_34.neighbors = [Node_26, Node_35]
    Node_35.neighbors = [Node_41]
    Node_36.neighbors = [Node_33, Node_40]
    Node_37.neighbors = [Node_29]
    Node_38.neighbors = [Node_39]
    Node_39.neighbors = [Node_40, Node_41]
    Node_40.neighbors = [Node_Goal]
    Node_41.neighbors = [Node_26]
    # Goal Node
    Node_Goal.neighbors = [Node_40]

    # list of nodes for Bellman Ford computation
    graph = [Node_1, Node_2, Node_3, Node_4, Node_5, Node_6, Node_7, Node_8, Node_9, Node_10, Node_11,
             Node_12, Node_13, Node_14, Node_15, Node_16, Node_17, Node_18, Node_19, Node_20, Node_21,
             Node_22, Node_23, Node_24, Node_25, Node_26, Node_27, Node_28, Node_29, Node_30, Node_31,
             Node_32, Node_33, Node_34, Node_35, Node_36, Node_37, Node_38, Node_39, Node_40, Node_41,
             Node_Goal]

    # find shortest path from start to goal node
    astar = astar_search(Node_11, Node_Goal)
    print(astar)

    bell = bellman_ford(graph, Node_11)
    print(bell)


# the times can be calculated separately for each algorithm by commenting
# one of them out. it is currently set for total duration of both algorithms.
if __name__ == '__main__':
    import time

    start_time = time.time()
    main()
    print("Time:", time.time() - start_time)
