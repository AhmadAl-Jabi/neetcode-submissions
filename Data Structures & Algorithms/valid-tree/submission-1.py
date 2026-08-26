class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if not edges:
            return True

        node_mapping = {}
        for i in range(n):
            node_mapping[i] = []
        
        for i in range(len(edges)):
            node_mapping[edges[i][0]].append(edges[i][1])
            node_mapping[edges[i][1]].append(edges[i][0])
        
        nodes_seen = set()

        def dfs(node, parent):
            if node in nodes_seen:
                return False
            
            nodes_seen.add(node)

            for neighbor in node_mapping[node]:
                if neighbor != parent:

                    if not dfs(neighbor,node):
                        return False
            
            return True
        
        result = dfs(edges[0][0],None)

        if result and len(nodes_seen) == n:
            return True
        
        return False

        