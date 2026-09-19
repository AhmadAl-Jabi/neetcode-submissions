# need to somehow keep things in a sorted order or at least the top k elements
# we only care about the k biggest so we can have a min heap of size k and ignore any numbers smaller than our root
# this way our root is always the smallest one or the kth biggest. If the add is smaller than root we ignore. 
# If it's bigger and we hit capacity then we need to add new node, remove the root and heapify
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # we want a min heap containing only the k biggest items (with the root being smallest)
        # start with just 0:k of nums then process the rest
        self.heap = nums[:k]
        heapq.heapify(self.heap)
        self.size = k

        for num in nums[self.size:]:
            if num >= self.heap[0]:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap,num)

        

    def add(self, val: int) -> int:
        if len(self.heap) == self.size:
            if val >= self.heap[0]:
                heapq.heappop(self.heap)
            else:
                return self.heap[0]

        heapq.heappush(self.heap,val)
        return self.heap[0]
        