import heapq, math
from typing import Optional
from queue import PriorityQueue

from helpers import Map, load_map, show_map

def heuristic(a, b):
    return math.sqrt(((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2))

def reconstruct_path(came_from, current, goal):
    node = goal
    path = [node]
    if node not in came_from:
        print(f"Node: {node} not found in map.")
        return
    
    while current != node:
        node = came_from[node]
        path.append(node)
    path.reverse()
    return path

def heuristic_measure(start, goal):
    return math.sqrt(((start[0] - goal[0]) ** 2) + ((start[1] - goal[1]) ** 2))

def shortest_path(M: Map, start: int, goal: int):
    path_queue = PriorityQueue()
    path_queue.put(start, 0)

    previous = {start: None}
    score = {start: 0}

    while not path_queue.empty():
        current = path_queue.get()
        if current == goal:
            reconstruct_path(previous, start, goal)

        for node in M.roads[current]:
            update_score = score[current] + heuristic_measure(
                M.intersections[current],
                M.intersections[node]
            )

            if node not in score or update_score < score[node]:
                score[node] = update_score
                totalScore = update_score + heuristic_measure(
                    M.intersections[current], M.intersections[node])
                path_queue.put(node, totalScore)
                previous[node] = current

    return reconstruct_path(previous, start, goal)