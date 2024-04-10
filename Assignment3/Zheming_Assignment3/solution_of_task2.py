import pandas as pd
import heapq
import datetime
import argparse
import pytz
import sys

def dijkstra(adjacency_list, source, target, tstart):
    # Initialize the distances and previous dictionary
    distances = {node: sys.maxsize for node in adjacency_list}
    previous = {node: None for node in adjacency_list}
    distances[source] = tstart
    # Create a priority queue, the first element is the source with distance tstart
    priority_queue = [(tstart, source)]

    while priority_queue:
        # First, we pop the node with the smallest distance
        current_distance, current_node = heapq.heappop(priority_queue)

        # If the current node is the target, we break the loop
        if current_node == target:
            break

        # Visit all the neighbors of the current node
        for neighbor in adjacency_list[current_node]:
            # If the neihgbor do not have any path to the target, and the neighbor is not the target, we skip it
            if (neighbor[1] not in adjacency_list) and (neighbor[1] != target):
                continue
            # Here, the neighbor has a path to outside, we get the timestamp and the node
            neighbor_timestamp, neighbor_node = neighbor

            # If the timestamp is not smaller than the current distance(current timestamp), we go one step to see if we can update a new distance
            if neighbor_timestamp >= current_distance:
                new_distance = neighbor_timestamp

                # If the new distance is smaller than the distance to the neighbor, we update the distance and previous
                if new_distance < distances[neighbor_node]:
                    distances[neighbor_node] = new_distance
                    previous[neighbor_node] = current_node
                    heapq.heappush(priority_queue, (new_distance, neighbor_node))

    # If we find the path, we reconstruct the path
    path = []

    # If the distance to the target is valid:
    if distances[target] != sys.maxsize:
        # Trace back the path with the link of previous
        node = target
        while node is not None:
            path.append(node)
            node = previous[node]
        # Reverse the path
        path.reverse()

    return path, distances[target]


def main():
    parser = argparse.ArgumentParser(description='Dijkstra Algorithm')

    # Add command line arguments
    parser.add_argument('--filename', type=str, default='graph.tsv', help='Graph data filename')
    parser.add_argument('--source', type=str, default='source_subreddit', help='Source subreddit name')
    parser.add_argument('--target', type=str, default='target_subreddit', help='Target subreddit name')
    parser.add_argument('--tstart', type=str, default='2024-04-09 10:00:00', help='Start timestamp')

    # Parse the arguments
    args = parser.parse_args()

    # Get the arguments
    filename = args.filename
    source = args.source
    target = args.target
    tstart_str = args.tstart
    tstart = datetime.datetime.strptime(tstart_str, '%Y-%m-%d %H:%M:%S')

    # print("filename:", filename)
    # print("source:", source)
    # print("target:", target)
    # print("tstart:", tstart)
    tstart = int(tstart.timestamp())
    
    # print("tstart:", tstart)
    # read dict.tsv and make a dictionary

    # Read dict.tsv and make a dictionary
    dictionary = {}
    with open('dict.tsv', 'r') as file:
        for line in file:
            line = line.strip().split('\t')
            key = line[0]
            value = line[1]
            dictionary[value] = key
    # print(dictionary)
    source = dictionary[source]
    target = dictionary[target]
    
    adjacency_list = {}

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip().split('\t')
            source_id = line[0]
            triples = line[1:]
            
            if source_id not in adjacency_list:
                adjacency_list[source_id] = []
            
            for triple in triples:
                timestamp, target_id, emotion = triple.split(',')
                timestamp = int(timestamp)
                if emotion == '1':
                    adjacency_list[source_id].append((timestamp, target_id))
        



    # Run Dijkstra algorithm
    result = dijkstra(adjacency_list, source, target, tstart)

    # Create a dictionary to store the mapping between the node and the subreddit name
    # By reading the dict.tsv file
    dictionary = {}

    with open('dict.tsv', 'r') as file:
        for line in file:
            line = line.strip().split('\t')
            key = line[0]
            value = line[1]
            dictionary[key] = value

    
    

    
    path, distance = result
    if len(path) == 0:
        print("No path found")
    else:  
        # Change the distance to a datetime object
        distance = datetime.datetime.fromtimestamp(distance)
        print("Arrival time: ", distance)
        print("Path: ")
        for i in range(len(path)):
            print(dictionary[path[i]], end='')
            if i != len(path) - 1:
                print(' -> ', end='')


if __name__ == '__main__':
    main()