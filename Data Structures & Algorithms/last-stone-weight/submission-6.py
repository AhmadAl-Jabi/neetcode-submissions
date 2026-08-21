class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # REMEMBER THAT HEAPS ARE NOT SORTED. THEY JUST GUARANTEE THAT THE TOP NODE IS MIN
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:

            # Keep in mind these are negative rn. They are the two "biggest" nodes
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            if x == y:
                continue
            
            elif x < y: # x is more negative, so it's abs is bigger
                x -= y
                heapq.heappush(stones, x)

            else:
                y -= x
                heapq.heappush(stones, y)
            
        return -(stones[0]) if stones else 0