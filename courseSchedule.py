# Time Complexity : O(V+E), where V is the number of courses and E is the number of prerequisites
# Space Complexity : O(V+E), where V is the number of courses and E is the number of prerequisites
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Approach:
# We will use a BFS approach to solve this problem.
# 1. Create a list to store the indegrees of each course, indicating how many prerequisites each course has.
# 2. Create a hashMap to store the prerequisites and the courses that depend on them.
# 3. For each course in the prerequisites, update the indegrees and the hashMap.
# We will iteratively check the courses that have no prerequisites (indegree of 0), and add them to the queue,
# For each processed course, their corresponding courses in the hashMap will have their indegrees decremented by 1.
# If any of those courses have an indegree of 0, we will add them to the queue.
# 4. If we can process all the courses, we return True.

from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        # Initialize indegrees list with 0 for each course
        indegrees = [0] * numCourses
        # Create a hashMap to store the prerequisites and the courses that depend on them
        hashMap = defaultdict(list)

        # Fill the hashMap and indegrees list based on the prerequisites
        # For each course and its prerequisite, update the hashMap and indegrees
        for course, pre in prerequisites:
            hashMap[pre].append(course)
            indegrees[course] += 1

        # Initialize a queue to store the courses with no prerequisites (indegree of 0)
        q = deque()
        # Add all courses with indegree of 0 to the queue
        for i in range(len(indegrees)):
            if indegrees[i] == 0:
                q.append(i)
        
        # Initialize a counter to keep track of the number of courses processed (courses taken)
        courseCount = 0
        # Process the courses in the queue
        while q:
            # Take a snapshot of the size of the queue
            # This will help us process all the courses that could be taken in this iteration
            size = len(q)
            # Process all the courses in the current level (semester)
            for i in range(size):
                # Pop each course from the queue, indicating we have taken the course
                currCourse = q.popleft()
                # Increment the courseCount because we have taken this course
                courseCount += 1
                # Check if we have taken all the courses. If yes, return True
                if courseCount == numCourses:
                    return True
                # For each course that depends on the current course, decrement its indegree
                courseList = hashMap[currCourse]
                if courseList:
                    for c in courseList:
                        indegrees[c] -= 1
                        # If the indegree of the course becomes 0, add it to the queue, indicating that this course can now be taken in the next semester
                        if indegrees[c] == 0:
                            q.append(c)

        # If we have processed all the courses, we would've returned True in the loop
        # If we reach here, it means we couldn't take all the courses due to circular dependencies
        # So we return False
        return False

# Time Complexity : O(V+E), where V is the number of courses and E is the number of prerequisites
# Space Complexity : O(V+E), where V is the number of courses and E is the number of prerequisites
# Approach: DFS
# We will use a DFS approach to solve this problem.
# 1. Create a hashMap to store the prerequisites and the courses that depend on them.
# 2. Create a list to store the completion status of each course.
# 3. Create a set to store the courses that are currently being visited.
# 4. For each course, check if it is already completed or if it is currently being visited.
# If it is in the current visit path, it means we have a cycle, so return False.
# 5. If the course is not completed, mark it as being visited and check its prerequisites.
# 6. If any of the prerequisites have a cycle, return False.   
class Solution:
    def canFinish(self, numCourses: int, prerequisites):
        def isCycle(c):
            if complete[c]:
                return False
            if c in visit:
                return True

            visit.add(c)
            courses = courseMap[c]
            for course in courses:
                if isCycle(course):
                    return True
            visit.remove(c)
            complete[c] = True

        courseMap = defaultdict(list)
        for i in range(len(prerequisites)):
            course, depend = prerequisites[i][0], prerequisites[i][1]
            courseMap[depend].append(course)

        visit = set()
        complete = [False] * numCourses
        for i in range(numCourses):
            if isCycle(i):
                return False
        return True