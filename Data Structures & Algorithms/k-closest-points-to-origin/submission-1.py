class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        min_heap = []
        result = []

        def dist(point: List[int]):
            return ((point[0])**2 + (point[1])**2) # Since we will always be relative to the origin
        
        # How about we build a new heap where we just push onto it the distances as we go --> distances is O(n)
        # Once we've built the heap we just pop k times. This way push pop and what not is O(log)

        for point in points:
            d = dist(point)
            min_heap.append((d,point)) # Just append a tuple and heapq will sort by the dist anyway
        
        heapq.heapify(min_heap)

        for i in range(k):
            result.append((heapq.heappop(min_heap))[1])
        
        return result
        




        
        