class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # can use similar approach as last question where we do dfs
        # but instead what we can add is when we hit a base case we can append the set to an arr of possible paths and then return any one of them that has len numCourses
        output_arr = []
        seen_on_path = set()
        finished = set() # this set serves as nodes we've already verified as good AND are in output_arr (don't add again)
        preq_map = {}

        # basically build the dependency hashmap
        for key in range(numCourses):
            preq_map[key] = []
        
        for i in range(len(prerequisites)):
            course = prerequisites[i][0]
            prereq = prerequisites[i][1]

            preq_map[course].append(prereq)


        # Then we do dfs fully on each key. If its full path of what it depends on is good then we add it to output_arr and add it to finished and set its value to []. Recursively this would keep going until we hit base case of something that does NOT rely on any courses, and it would be the first added to output_arr.

        def dfs(course):

            # if already in finished (dealt with) just return True cuz its valid
            if course in finished:
                return True
            
            # if course already in seen_on_path --> return False
            if course in seen_on_path:
                return False

            # add course to seen_on_path
            seen_on_path.add(course)

            for preq in preq_map[course]:
                if not dfs(preq):
                    return False
            
            # remove course from seen_on_path --> backtracking, allows other paths
            seen_on_path.discard(course)
            # preq_map[course] = [] --> This saves wasted time since we proved that course is valid
            preq_map[course] = []

            # if it got this far then it's guaranteed NOT in finished
            output_arr.append(course)
            finished.add(course)

            return True # course was valid

        # If curr was deemed good that means it would be appended AFTER all its prereqs are already in output_arr, and if anything depends on curr, that thing will simply be appended AFTER current naturally

        # we call dfs on every key through a for loop
        for key in preq_map:
            if not dfs(key):
                return []

        return output_arr
        