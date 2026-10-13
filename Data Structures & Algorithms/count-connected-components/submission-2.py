class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # n is the number of nodes (labelled from 0 to n-1)
        # 1 <= n <= 2000, 1 <= edges.length <= 5000
        # we want the number of connected components (how many individual graphs we have)

        # Observations:
        # we need a way of knowing the adjacent nodes for each node --> adjaceny list or hashmap
        # how many individual graphs do we have (i.e. 1 graph means from a node we can visit every other node since all connected)
        # DFS to see the nodes within a given path --> when we discover new paths (that previous DFS didn't find) that would mean we're in a separate graph

        # Algorithm:
        # first pass through edges --> start with making adjaceny list of node: index means neighbour list of ith node [[],[],[]]
        # we want to start a DFS (can do iteratively with a stack) and go down as far as we can from a node and track the nodes we see in a set
        # need a counter of how many distinct graphs we'd have 
        # can use the fact that nodes that aren't yet in set would require a counter += 1 since it's a whole new component/graph

        adjacency = [[] for i in range(n)]
        for node1, node2 in edges:
            adjacency[node1].append(node2)
            adjacency[node2].append(node1)
        
        num_of_graphs = 0
        visited = set()
        for node in range(n):
            if node in visited:
                continue
            visited.add(node)
            num_of_graphs += 1

            # want to DFS traverse its neighbours
            stack = [node]
            while stack:
                current_node = stack.pop()
                # visit the neighbours
                for neighbour in adjacency[current_node]:
                    # check if in visited
                    if neighbour not in visited:
                        stack.append(neighbour)
                        visited.add(neighbour)

        return num_of_graphs








