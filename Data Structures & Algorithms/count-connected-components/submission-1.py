class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0

        if not edges:
            return n

        node_mapping = {}
        for i in range(n):
            node_mapping[i] = []
        
        for i in range(len(edges)):
            node_mapping[edges[i][0]].append(edges[i][1])
            node_mapping[edges[i][1]].append(edges[i][0])
        
        nodes_seen = set()

        def dfs(node, parent):
            if node in nodes_seen:
                return
            
            nodes_seen.add(node)

            for neighbor in node_mapping[node]:
                if neighbor != parent:

                    dfs(neighbor,node)
            
            
            return True

        for key in node_mapping:
            curr_count = len(nodes_seen)
            dfs(key,None)
            if curr_count != len(nodes_seen):
                count += 1

            if len(nodes_seen) == n:
                break
        
        return count