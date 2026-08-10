class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # A better approach is bucket sort based on the max number

        frequency_dict = {}

        for num in nums:

            if num not in frequency_dict:
                frequency_dict[num] = 0
            
            frequency_dict[num] += 1
        
        sorted_pairs = sorted(
            frequency_dict.items(),
            key = lambda pair: pair[1],
            reverse=True
        )
        
        output_arr = [key for key, value in sorted_pairs[:k]]
        return output_arr

        