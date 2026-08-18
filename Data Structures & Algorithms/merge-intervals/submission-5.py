class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # [[1,6], [2,8], [9,10], [5,6]]
        # sort --> [[1,6], [2,8], [5,6],[9,10]]
        # [1,3], [4,5]
        # overlapping means when the start of the bigger interval is smaller or equal than the end of the smaller interval --> This would require the intervals to actually be in order in the first place

        # if len(intervals) == 1 --> return intervals
        #if len(intervals) == 1:
            #return intervals

        # might need to sort intervals increasing based on index[0] --> O(nlogn)
        intervals.sort(key=lambda a:a[0])
        final_intervals = [intervals[0]]

        for right in range(1,len(intervals)):
            if intervals[right][0] > final_intervals[-1][1]:
                final_intervals.append(intervals[right])
            
            else:
                final_intervals[-1][1] = max(intervals[right][1],final_intervals[-1][1])
        
        return final_intervals
        


        