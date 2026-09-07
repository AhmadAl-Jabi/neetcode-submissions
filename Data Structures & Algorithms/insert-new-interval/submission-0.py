class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output_arr = []
        i = 0

        def insert_interval(interval):
            if interval[0] <= output_arr[-1][1]:
                output_arr[-1][1] = max(interval[1],output_arr[-1][1])
            else:
                output_arr.append(interval)

        # 1. Add everything completely before newInterval
        while i < len(intervals) and intervals[i][0] < newInterval[0]:
            output_arr.append(intervals[i])
            i += 1

        # insert/merge newInterval
        insert_interval(newInterval) if output_arr else output_arr.append(newInterval)

        # 2. Add/merge everything completely after newInterval
        while i < len(intervals):
            insert_interval(intervals[i])
            i += 1

        return output_arr