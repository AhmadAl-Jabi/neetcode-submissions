class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        # Assumptions:
        # Days CAN be more than number of weights, just means we ship nothing on extra days (has no effect on capacity)
        # Dealing with integer weights and integer days
        # Weights and days are both non-empty/non-zero

        # Constraints
        # Weights MUST be loaded in order given by weights --> We are not allowed to reorder
        #[2,3,1,4] days = 3 --> output = 4

        # Logic
        # Binary search the capacities from lowest possible (the value of max in the array) and max possible (the sum of every number)
        # Basically at each capacity we test to see if we can do it in lte days
        # If not, go up in binary search
        # If so, go lower
        # Return the lowest num we found

        low_bound = max(weights)
        high_bound = sum(weights)

        while low_bound < high_bound:
            cur_capacity = (low_bound + high_bound) // 2
            cur_weight = 0
            counted_days = 1

            for weight in weights:
                if cur_weight + weight > cur_capacity:
                    cur_weight = weight
                    counted_days += 1
                else:
                    cur_weight += weight
            
            if counted_days > days:
                low_bound = cur_capacity + 1
            else:
                high_bound = cur_capacity 

        return high_bound

                

        