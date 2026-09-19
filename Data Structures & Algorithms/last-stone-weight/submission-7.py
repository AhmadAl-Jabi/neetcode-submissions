import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap) # this does it in place!!!

        # after smashing two stones we need to add the resulting stone back into the heap
        # also note that the two stones that are smashed are just the ones popped from the max heap

        # condition is just while the heap has at least 2 elements 
        while len(heap) >= 2:
            rock_1 = -heapq.heappop(heap)
            rock_2 = -heapq.heappop(heap)

            resulting_rock = rock_1 - rock_2
            if resulting_rock > 0:
                heapq.heappush(heap, -resulting_rock)
        
        return -heap[0] if heap else 0