class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_map = {}
        # make the hashmap from 0 to numCourses - 1 and have each of them with empty arr
        for i in range(numCourses):
            course_map[i] = []
        # then iterate over prereqs and append to each value array
        for i in range(len(prerequisites)):
            course_map[prerequisites[i][0]].append(prerequisites[i][1])

        seen = set()

        def dfs(course):

            if course_map[course] == []:
                return True
            
            if course in seen:
                return False #--> It's a dupe along this path

            seen.add(course)
            for preq in course_map[course]:
                if not dfs(preq):
                    return False
                
            # get rid of the course (backtrack) if it was successful so we can explore other options -> We also set its prereqs to empty arr so that if anything depends on it it'll shortcircuit to True (instead of going thru the entire dfs once again for no reason)
            seen.discard(course)
            course_map[course] = []
            return True
        
        for key in course_map:
            if not dfs(key):
                return False
        
        return True
        