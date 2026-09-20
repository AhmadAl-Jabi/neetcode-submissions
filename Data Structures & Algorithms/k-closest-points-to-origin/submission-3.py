import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # need the k closest points --> we can sort, but if we only need the k closest (smallest distance)
        # we can just use a min heap BUT max heap more optimal cuz we only keep the k smallest elements and only pop & push
        # when the curr element is closer than the root (the root being the furthest)
        heap, output_arr = [], []

        # for i in range(len(points)):
        for i in range(len(points)):
            # we compare to (0,0) always so simplify the formula
            dist = ((points[i][0])**2 + (points[i][1])**2)**0.5 # --> where x = points[i][0], y = points[i][1]
            # if len(heap) == k:
            if len(heap) == k:
                # if -dist < heap[0][0]:
                if -dist < heap[0][0]:
                    continue
                heapq.heappop(heap)
                
            # then we can heappush a tuple with (-dist,points[i]) and the heap automatically will work
            heapq.heappush(heap,(-dist,points[i]))

        return [element[1] for element in heap]
