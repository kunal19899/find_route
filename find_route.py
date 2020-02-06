import os
import sys
from queue import PriorityQueue

# everything is working, I just need to do error checking

def create_map(filename):
    with open(filename) as input:
        map = []
        for line in input:
            if line == "END OF INPUT\n":
                return map
            nodeA, nodeB, distance = line.split()
            map.append([nodeA, nodeB, distance])
            map.append([nodeB, nodeA, distance])

def create_heuristics(filename):
    with open(filename) as input:
        heuristics = {}
        for line in input:
            if line == "END OF INPUT\n":
                return heuristics
            city, weight = line.split()
            heuristics[city] = weight
        

def uniform_cost_search(map, start, goal):
    nodes_expanded = 0
    nodes_generated = 0
    max_nodes_in_memory = 0

    visitedCities = set()
    priorityQueue = PriorityQueue()

    priorityQueue.put((0, [start]))
    while priorityQueue:
        if priorityQueue.empty():
            return ["none", "infinity", nodes_expanded, nodes_generated, max_nodes_in_memory]

        if priorityQueue.qsize() >= max_nodes_in_memory:
            max_nodes_in_memory = priorityQueue.qsize()
            
        node = priorityQueue.get()
        nodes_expanded += 1
        cost = node[0]
        path = node[1]

        city = node[1][len(node[1])-1]
        
        if city == goal:
            return [path, cost, nodes_expanded, nodes_generated, max_nodes_in_memory]

        if city not in visitedCities:
            visitedCities.add(city)
            for connection in map:
                if connection[0] == city:
                    nodes_generated += 1
                    temp = node[1][:]
                    temp.append(connection[1])
                    newCost = cost + int(connection[2])
                    priorityQueue.put((newCost, temp))

def a_start_search(map, start, goal, heuristics):
    nodes_expanded = 0
    nodes_generated = 0
    max_nodes_in_memory = 0

    visitedCities = set()
    priorityQueue = PriorityQueue()

    f = int(heuristics[start]) + 0
    priorityQueue.put((f, [start]))
    
    while priorityQueue:
        if priorityQueue.empty():
            return ["none", "infinity", nodes_expanded, nodes_generated, max_nodes_in_memory]

        if priorityQueue.qsize() >= max_nodes_in_memory:
            max_nodes_in_memory = priorityQueue.qsize()

        node = priorityQueue.get()
        nodes_expanded += 1
        g = int(node[0]) - int(heuristics[node[1][len(node[1])-1]])
        path = node[1]
        city = node[1][len(node[1])-1]

        if city == goal:
            return [path, g, nodes_expanded, nodes_generated, max_nodes_in_memory]

        if city not in visitedCities:
            visitedCities.add(city)
            for connection in map:
                if connection[0] == city:
                    nodes_generated += 1
                    temp = node[1][:]
                    temp.append(connection[1])
                    f = g + int(connection[2]) + int(heuristics[connection[1]])
                    priorityQueue.put((f, temp))

def start_state_retrieval(map):
    start_states = []
    for i in range(len(map)):
        if map[i][0] not in start_states:
            start_states.append(map[i][0])
    return start_states

def goal_state_retrieval(map):
    goal_states = []
    for i in range(len(map)):
        if map[i][1] not in goal_states:
            goal_states.append(map[i][1])
    return goal_states
 
def print_results(results, map):
    print("nodes expanded: " + str(results[2]))
    print("nodes generated: " + str(results[3]))
    print("max_nodes in memory: " + str(results[4]))
    print("distance: " + str(results[1]) + " km")
    print("route:")
    if results[0] != "none":
        for i in range(len(results[0])-1):
            for connection in map:
                if connection[0] == results[0][i] and connection[1] == results[0][i+1]:
                    print(results[0][i] + " to " + results[0][i+1] + ", " + connection[2] + " km")
    else:
        print("none")

def main():
    inputFile = sys.argv[1]
    start = sys.argv[2]
    goal = sys.argv[3]
    map = create_map(inputFile)

    start_states = start_state_retrieval(map)
    goal_states = goal_state_retrieval(map)
    
    if start not in start_states:
        print("Start state not found")
        sys.exit()
    if goal not in goal_states:
        print("Goal state not found")
        sys.exit()
    
    if len(sys.argv) == 4:
        results = uniform_cost_search(map, start, goal)
    elif len(sys.argv) == 5:
        heuristics = create_heuristics(sys.argv[4])
        results = a_start_search(map, start, goal, heuristics)
    
    print_results(results, map)


if __name__ == '__main__': 
    main()
