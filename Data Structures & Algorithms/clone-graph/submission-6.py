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
        # Problem/Assumptions:
        # deep copy of the graph
        # first node as input (value 1), where node stores node.val, node.neighbours (list of nodes)
        # node values from 1 to n where n is total number of nodes
        # return a node in the end (deep copy of the input node)

        # Observations:
        # from each node we can find all its neighbours in node.neighbours 
        # --> we need to ensure we track what we've seen so far to avoid revisiting nodes
        # we can process nodes in an order using some sort of queue

        # Algorithm:
        # can have a hashmap that references {original_node: deep_copy_node}
        # start the queue with the first node
        # current from popleft() queue
        # iterate over the neighbours of the current node
        # if the neighbour hasn't already been cloned 
            # --> make a deep clone and store it in our hashmap of original:clone
            # append the original neighbour to our queue
        # update the current clone's .neighbours to include the clone neighbour
        
        # return clones_map[node] --> reference to the clone of original

        # Code:
        if node is None:
            return None
        
        clone_map = {node: Node(node.val)}
        queue = deque([node])

        while queue:
            current_node = queue.popleft()
            for neighbor in current_node.neighbors:
                if neighbor not in clone_map:
                    clone_map[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                clone_map[current_node].neighbors.append(clone_map[neighbor])
        
        return clone_map[node]        



















