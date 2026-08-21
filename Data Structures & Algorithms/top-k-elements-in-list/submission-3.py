class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Aytt we just got two more cmon now

        freq_map = {}

        for num in nums:
            freq_map[num] = 1 + freq_map.get(num,0)

        # The index (bucket) of the array itself represents frequency, and the entries are the numbers themselves
        bucket = [[] for i in range((len(nums) + 1))]

        for key in list(freq_map.keys()):
           bucket[freq_map[key]].append(key)
         
        flat = []
        for row in bucket:
            flat.extend(row)
        
        return flat[-k:]
        


        
