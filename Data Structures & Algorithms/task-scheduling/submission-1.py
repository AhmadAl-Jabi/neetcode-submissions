import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        freq_map = [0]*26
        counter = 0
        queue = deque()

        # [A,B,A,C] n = 2

        #    2,A
        #  1,B  1,C 

        # we can build a max heap (-1 * freq) of the tasks with the pairing being [freq,char]
        # to do this though we need to build a freq map first --> can do hashmap but size 26 arr works
        for task in tasks:
            idx = ord(task) - ord("A")
            freq_map[idx] += 1
        
        for i in range(len(freq_map)):
            if freq_map[i] == 0:
                continue
            
            # don't need to store the letter itself but can store idx if we want
            heapq.heappush(heap,[-freq_map[i],counter])
        
        # while queue OR heap not empty 
        while queue or heap:
            if heap:
                element = heapq.heappop(heap)
                element[0] += 1
                
                element[1] = counter # update the time of our element
                queue.append(element) if element[0] != 0 else None
            
            if queue and counter - queue[0][1] == n:
                heapq.heappush(heap,queue.popleft())
            # we can have a queue as well FIFO
            # where when we process the root and pop it from the heap we just pop it to the end of the queue with time = counter
            # each iteration we need to check the first element in the queue to see if it's been there long enough 
            # if (counter - time == n) --> queue.popleft() and add back to heap (make sure to decrement freq)

            #c =  A      B   C
            # [[2,0][1,1][1,2]]
            counter += 1
        return counter