import heapq
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        #Algorithm
        # First we build an adjacency list using the edges array we’re given → make a hashmap of {source: [(neighbour1,dist1), (neighbour2,dist2)]}
        # we can create a min heap and initialize it with the (0, src) → min heap is essentially way to order the cheapest node to process next. When we pop a node it means we have found the cheapest way to it
        # have a output_map that just maps {dest:cost} for every single node given we start from source. When something gets added here it’s final value and it won’t be changed
        # while heap → we pop from the heap, check it hasn’t been processed first, then set output_map[curr_node] = curr_cost that we get from the heap pop
        # then iterate over the neighbours of curr_node and push to heap (curr_cost + adj_list_cost, neighbour_node)

        # Keep doing this and return the hashmap in the end

        adj_list = {}
        for i in range(n):
            adj_list[i] = []
        
        for source, dest, weight in edges:
            adj_list[source].append((dest, weight))
        
        output_map = {}
        heap = [(0,src)]
        while heap:
            curr_cost, curr_node = heapq.heappop(heap)
            if curr_node in output_map:
                continue
            output_map[curr_node] = curr_cost

            for neighbour in adj_list[curr_node]:
                
                heapq.heappush(heap,(curr_cost + neighbour[1], neighbour[0]))

        # make sure to deal with nodes that can't be reached --> just make output_map[i] = -1 if not already included
        for i in range(n):
            if i not in output_map:
                output_map[i] = -1

        return output_map

