import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        # pretty optimal but more space than needed
        heap = [-num for num in nums]
        heapq.heapify(heap)
        for i in range(k):
            curr_elem = -heapq.heappop(heap)
        return crr_elem
        '''
        heap = []
        # have a min heap where if there's an element BIGGER than root (which is the smallest; i.e. kth largest) we pop and push
        for i in range(len(nums)):
            if len(heap) == k:
                if nums[i] < heap[0]:
                    continue
                heapq.heappop(heap)
            heapq.heappush(heap,nums[i])
        
        return heap[0]


