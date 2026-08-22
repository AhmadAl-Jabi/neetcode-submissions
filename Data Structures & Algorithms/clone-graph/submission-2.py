"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #Deep clone graph question:
        '''-Basically need a way to track visited nodes first and foremost (don't need a set can just use dict)
-Then what we do is have a dictionary mapping old nodes to the new clones we create
-Then we traverse the entire graph, map old to new clone, and ignore traversals that would give us a dupe we've seen or out of bounds. Bfs works fine
-After the first traversal all we need to do is go through each key in the dictionary, take deep_curr = dict[key] and then take shallow_neighbours = dict[key].neighbours and have a deep_neighbours = [deep_neighbour for dict[shallow_key] in shallow_neighbours] (basically take the deep copy of each shallow neighbour and append them to deep_neighbours).

In the end I think we just return the first key value pair
'''
        if not node:
            return None

        node_mapping = {}
        queue = deque([node])
        node_mapping[node] = Node(node.val)

        # need a first traversal just to map the nodes in the dict
        # basically start the queue with the first node 

        while queue:
            curr_node = queue.popleft()
            for neighbor in curr_node.neighbors:
                #check that neighbor not in dict already --> continue if they are
                if neighbor in node_mapping:
                    continue

                queue.append(neighbor)
                node_mapping[neighbor] = Node(neighbor.val)
        
        for key in node_mapping:
            deep_neighbors = []
            deep_curr = node_mapping[key]
            shallow_neighbors = key.neighbors

            for neighbor in shallow_neighbors:
                deep_neighbors.append(node_mapping[neighbor])
            
            deep_curr.neighbors = deep_neighbors
        
        return node_mapping[node]

