class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Make sure that the cars are in increasing order of position
        cars = [(position[i],speed[i]) for i in range(len(position))]
        cars.sort(key=lambda a:a[0])

        # do a first pass where we calculate the time it takes each car to reach the end if it moved individually
        time_arr = []
        for i in range(len(cars)):
            time_taken = (target - cars[i][0]) / cars[i][1]
            time_arr.append(time_taken)

        # e.g. [1,4] [3,2] target = 10 --> [3,3]
        limiting_time = -1
        fleet_count = 0

        # then we can iterate from the back of this "time" array and stack the first time we see. This is the "limiting" time we'll compare to. Increment count by 1 
        for i in range(len(position) - 1, -1, -1):

            # now as we iterate if we see a bigger time that becomes the new limiter and we append to stack and increase counter
            if limiting_time < time_arr[i]:
                fleet_count += 1
                limiting_time = time_arr[i]

            # if we see a smaller time it means nothing since it'll just join the current fleet
        
        return fleet_count
