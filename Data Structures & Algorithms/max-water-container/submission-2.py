class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # length of the container is gonna just be the two indices subtracted (not ordered and I don't think we can order)

        # height is just the lesser of the two heights we choose --> so all that matters is we move the one with the smaller height. 
        # We effectively gain nothing by moving the one with the bigger height and keeping the smaller. In fact it makes it worse

        # We can brute force but I think there's def a better way

        max_water = 0

        i = 0
        j = len(heights) - 1

        while i < j:

            length = j - i
            height = min(heights[i], heights[j])
            area = length * height

            if area > max_water:
                max_water = area

            if heights[i] < heights[j]:
                i += 1
            
            else:
                j -= 1
        
        return max_water
        