class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Basically judt want to take the first k elements
        # Then we heapify and take out smallest guy
        # Then just add another element to the heap
        # basically keep doing this until the og is gone
        # then take the first element (the smalledt of the k, aka the kth biggest)
        # We can have a heap arr and the og arr
        # Always take first element from og and add to heap, until we exhaust initial arr
        # since the heap always remains a fixed size, once we hit the end itll have k elements still
        # thats how we take the k smallest one (heappop one last time)

        heap_arr = nums[:k]
        heapq.heapify(heap_arr)
        nums = nums[k:]

        while nums:
            # First pop from heap the smallest value
            # Then pop the top of nums and push to heap

            # This way heap stays the exact same size and always filters the smallest num
            heapq.heappush(heap_arr, nums.pop())
            heapq.heappop(heap_arr)
            #heapq.heappush(heap_arr, nums.pop()) 
        
        return heap_arr[0]