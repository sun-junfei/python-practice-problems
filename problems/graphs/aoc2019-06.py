"""
Starter code for Advent of Code 2019 Day #6

You must implement functions part1 and part2
"""

import sys
import os
import re


def part1(orbits):
    """
    Solves Part 1 (see problem statement for more details)

    Parameter:
    - orbits: a dictionary mapping an object name (e.g., "B")
              to the name of the object it orbits (e.g., "COM")

    Returns an integer
    """


    def helper(node, graph):
        orb_count = 0
        if node not in graph.keys():
            return orb_count

        orb_count += (helper(graph[node], graph) + 1)
        return orb_count
    
    orb_num = 0
    for star in orbits.keys():
        orb_num += helper(star, orbits)
    
    return orb_num


def part2(orbits):
    """
    Solves Part 2 (see problem statement for more details)

    Parameter:
    - orbits: a dictionary mapping an object name (e.g., "B")
              to the name of the object it orbits (e.g., "COM")

    Returns an integer
    """
    orb_graph = {}
    for key in orbits.keys():
        if orbits[key] not in orb_graph.keys():
            orb_graph[orbits[key]] = []
        orb_graph[orbits[key]].append(key)
        
        if key not in orb_graph.keys():
            orb_graph[key] = []
        orb_graph[key].append(orbits[key])
    
    
    def BFS(start, graph):
        route = {}
        queue = []
        explored = set()
        queue.append(start)
        explored.add(start)
        while queue:
            v = queue.pop()
            for child in graph[v]:
                if child == 'SAN':
                    return v, route
                if child not in explored:
                    queue.append(child)
                    explored.add(child)
                    route[child] = v
        return None
    
    key, route = BFS('YOU', orb_graph)
    road_length = 0
    while route[key] != 'YOU':
        key = route[key]
        road_length +=1 
    return road_length
    




############################################
###                                      ###
###      Do not modify the code below    ###
###                EXCEPT                ###
###    to comment/uncomment the calls    ###
###        to the functions above        ###
###                                      ###
############################################


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"USAGE: python3 {os.path.basename(sys.argv[0])} <INPUT FILE>")
        sys.exit(1)

    input_file = sys.argv[1]

    if not os.path.exists(input_file):
        print(f"ERROR: No such file: {input_file}")
        sys.exit(1)

    with open(input_file) as f:
        lines = f.read().strip().split("\n")
        objs = [line.split(")") for line in lines]
        orbits = {}
        for p1, p2 in objs:
            orbits[p2] = p1

    #print(f"Part 1:", part1(orbits))
    
    # Uncomment the following line when you're ready to work on Part 2
    print(f"Part 2:", part2(orbits))
