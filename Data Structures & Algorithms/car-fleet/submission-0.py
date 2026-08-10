class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        '''
        Simplest thing to think about:
        -Look at the cars closest to the finish line --> How long does it take them to reach it (seconds)
        -If a car before them gets there faster it does NOT matter since it'll just join the fleet
        -If a car before them gets there SLOWER it DOES matter --> += 1 new fleet

        That's literally it lol
        '''
        

        # Cars can't pass the ones in front of them --> it'll just catch up and move at same speed (join the fleet) --> basically compressing cars to one fleet that has the same speed as the slowest of the bunch (same position & speed)

        # Fleets are non-empty --> single car can be a fleet

        # The max amount of fleets you can have is n and the min is 1 
        
        # We can think of "turns" as in each turn the cars will move "speed" distance and have a new position
        # but cars that joined a fleet will have the same position and speed as the slowest car in the fleet
        '''
        Approach:

        X-Pair each position with its respective speed
        X-Sort the pairs in order of position with decreasing order (i.e. the cars close to finishing first)
        X-Iterate over each pair and build an array of "times" (i.e. (target - position) / speed) <-- if decimal issues then we can avoid division and use cross multiplication
        -Now every car is limited by the "time" of the fleet in front of them 
        -Have a counter and return the final counter (this represents the number of fleets)
        '''

        pairs = []
        times = []
        num_of_fleets = 0

        for i in range(len(position)):
            pairs.append([position[i], speed[i]])
        
        pairs.sort(key= lambda a: a[0], reverse=True) # Sorting --> O(nlogn)

        for pair in pairs:
            cur_pos = pair[0] # position
            cur_speed = pair[1] # speed
            times.append((target - cur_pos) / cur_speed) # keep decimals since exact time matters

        # Compare the times of the cars
        
        max_time = 0
        for time in times:
            if time > max_time:
                max_time = time
                num_of_fleets += 1
                

        return num_of_fleets


