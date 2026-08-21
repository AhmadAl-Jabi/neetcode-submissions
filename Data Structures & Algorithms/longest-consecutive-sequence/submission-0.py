class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # Main thing is basically finding the beginning of a sequence. I suppose I could do this by turning arr into hash table (O(n))
        # Then we can go thru the array and check if num - 1 not in hash set. If this the case, we identified a start of a sequence (add to new arr)
        # Once we have our starts we basically just try to see if we can do num + 1, if so then set cur to that num and incremenet streak
        # If we can't we update the max count (end of seq) we reset counter & set the new cur to the next start of a sequence

        # Even better is rather than making a "starts" arr we can just look for the next start after finishing the first seq

        hash_set = set(nums)
        max_count = 0

        for num in nums:

            # If it's not the start of a seq we don't care
            if num - 1 in hash_set:
                continue
            
            # Start of a seq
            count = 1
            cur_num = num
            while cur_num + 1 in hash_set:
                count += 1
                cur_num += 1
            
            if count > max_count:
                max_count = count

        return max_count
            
        