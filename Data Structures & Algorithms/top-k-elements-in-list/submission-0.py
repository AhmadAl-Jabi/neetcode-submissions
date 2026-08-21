class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Aytt we just got two more cmon now

        freq_map = {}

        for num in nums:
            freq_map[num] = 1 + freq_map.get(num,0)

        #values_arr = list(freq_map.values())
        #key_arr = list(freq_map.keys())

        sorted_keys = [key for key,val in sorted(freq_map.items(),key=lambda p:p[1], reverse=True)][:k]
        return(sorted_keys)