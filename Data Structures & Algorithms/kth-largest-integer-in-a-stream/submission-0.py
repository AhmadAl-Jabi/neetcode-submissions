class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = nums

        heapq.heapify(self.min_heap) # Built-in O(logn)

        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap) # Also O(logn) --> We ensure in the end smallest is root and we only have k elements. 
            
            # Root is kth largest
        

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)

        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]
        
