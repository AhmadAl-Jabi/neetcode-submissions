"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        adj_list = []
        seen_nodes = {}

        if not node:
            return None

        def dfs(node):
            if node in seen_nodes:
                return # return early since we already dealt with the guy
            
            seen_nodes[node] = Node(node.val,[])
            for neighbor in node.neighbors:
                dfs(neighbor)
                deep_neighbor = seen_nodes[neighbor]
                seen_nodes[node].neighbors.append(deep_neighbor)
            
            return

        dfs(node)
        #adj_list = [x[1].neighbors for x in tuple(seen_nodes.items())]
        return seen_nodes[node]
        
        # I am thinking we keep going till we see duplicates in neighbours
        # When we see a duplicate we can just append seen_nodes[dup_node] to the curr's neighbours
        # and return from that call


        #Ayt start to finish basic logic:
        #curr node --> if not seen_nodes[curr_node] then make duplicate with empty arr -->
        #then we for loop the curr node's neighbours and do dfs on it -->
        #in that same loop iteration we do seen_nodes[curr_node].neighbors.append(seen_nodes[neigbour]) -->
        #after this we just return
        #In the end adj_list will just equal to the dictionary values appended together

            
        