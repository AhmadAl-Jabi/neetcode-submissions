from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # [course, prereq]
        # total of numCourses -> [0, numCourses - 1]
        # ex. numCourses = 2, prerequisites = [[0,1],[1,0]] --> impossible because loop
        # We can have a loop of prereqs and courses that don't get finishes 
        # 0 -> 1 -> 2 -> 0

        # Observations:
        # We'd want to start with the courses that have no prereqs --> queue of courses (potentially BFS with a queue)
        # We can maybe map {prereqs: [courses]} in a hashmap (this lets us access courses after completing the prereq)
        # Repeteadly take courses with prereqs all completed

        #Algorithm
        # Map each prerequisite to the courses that depend on it (build up a hashmap of {prereq: [courses]})
        # track how many prereqs each course still has --> call this dependency_arr this will let us know when we can take a class
        # we can then have a queue starting with the classes that have no prereqs
        # From there we can visit the courses that depend on these prereqs (through BFS with queue)
        # Decrement the neighbouring course's dependency_arr entry and if it's at 0 we can add it to queue and so on
        # track how many total classes we dealt with by the end of the queue and if it's less than numCourses we return False

        # Code
        prereq_to_courses = {}
        dependency_arr = [0] * numCourses
        for course, prereq in prerequisites:
            if prereq not in prereq_to_courses:
                prereq_to_courses[prereq] = []
            prereq_to_courses[prereq].append(course)
            dependency_arr[course] += 1
        
        queue = deque()
        for course in range(numCourses):
            if dependency_arr[course] == 0:
                queue.append(course)
        
        classes_processed = 0
        while queue:
            prereq = queue.popleft()
            classes_processed += 1

            # decrement the dependency_arr[course] since we processed a prereq for it
            for course in prereq_to_courses.get(prereq, []):
                dependency_arr[course] -= 1
                if dependency_arr[course] == 0:
                    queue.append(course)
                    
        return classes_processed == numCourses











        
            

        
