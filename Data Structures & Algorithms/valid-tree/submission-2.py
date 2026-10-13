class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # what makes a valid tree?
        # Must be connected so every node is reachable from one node
        # can't have loops (acyclic)
        # we'll have n - 1 edges where n is the num of nodes (1 less edge than node)



        # Algorithm:
        # check if len(edges) == n - 1 --> otherwise we return False
        # iterate edges and we can build an adjacency list (2D matrix where adjaceny[i] is the neighbours of the ith node [[], [], []] )
        # starting from one node can we reach every node --> through DFS iteratively with a stack, maintain a set of seen nodes (visited)
        # we want to see if len(visited) == n in the end from just starting a DFS from the first node

        if len(edges) != n - 1:
            return False
        
        adjacency_list = [[] for i in range(n)]
        for node1, node2 in edges:
            adjacency_list[node1].append(node2)
            adjacency_list[node2].append(node1)
        
        nodes_visited = {0}
        stack = [0]
        while stack:
            curr_node = stack.pop()
            for neighbour in adjacency_list[curr_node]:
                if neighbour not in nodes_visited:
                    nodes_visited.add(neighbour)
                    stack.append(neighbour)
        
        return len(nodes_visited) == n
  


