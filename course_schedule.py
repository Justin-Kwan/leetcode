class Solution:
#     # optimal dfs cycle detection
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         # track courses already visited along path to detect cyclic links
#         # and cache whether course node is already completable
#         visited = {}
#         # add all valid course keys that could be accessed, even if not in prerequisites
#         courseByPrereqs = {course: [] for course in range(numCourses)}

#         if not prerequisites:
#             return True

#         # build graph of each course node by adjacency list of prerequisites
#         for course, prereqCourse in prerequisites:
#             courseByPrereqs[course].append(prereqCourse)

#         # check every course is completable (having no cycles in prerequisites)
#         for course in range(numCourses):
#             if not self.isCourseCompletable(course, courseByPrereqs, visited):
#                 return False

#         return True

#     def isCourseCompletable(self, course: int, courseByPrereqs: Dict[int, List[int]], visited: Dict[int, bool]) -> bool:
#         # cyclic prerequisites exist if course was already visited along current dfs path
#         if course in visited and not visited[course]:
#             return False

#         # course has no preqreuisites and thus is completable or
#         # course is already computed to be completable in cache from previous dfs path
#         if courseByPrereqs[course] == [] or (course in visited and visited[course]):
#             return True

#         # mark current course as visited but not known as completable
#         visited[course] = False

#         # current course is completable only if all its prerequisites are completable
#         for prereqCourse in courseByPrereqs[course]:
#             if not self.isCourseCompletable(prereqCourse, courseByPrereqs, visited):
#                 return False

#         visited[course] = True
#         return visited[course]

    # optimal bfs topological sort
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseIndegrees = [0 for _ in range(numCourses)]
        courseBySuccessors = {course: [] for course in range(numCourses)}
        successorsToVisit = collections.deque([])

        # count number of prerequisites (inbound edges) per each course and
        # build graph o course by successor course adjacency list
        for course, prereqCourse in prerequisites:
            courseIndegrees[course] += 1
            courseBySuccessors[prereqCourse].append(course)

        # queue should start at course nodes with no prerequisites
        for course in range(len(courseIndegrees)):
            if courseIndegrees[course] <= 0:
                successorsToVisit.append(course)

        while successorsToVisit:
            course = successorsToVisit.popleft()
            # remove edge between current course node and successor neighbors
            for successor in courseBySuccessors[course]:
                courseIndegrees[successor] -= 1
                if courseIndegrees[successor] <= 0:
                    successorsToVisit.append(successor)

            # remove current course node from graph since already visited and queued neighbors
            courseBySuccessors.pop(course, None)

        # any remaining edges between nodes mean that we could not travel in single direction and remove them because cyclic reference exists

        # graph is valid DAG only if we travelled between all edges to nodes and removed edges in single direction
        # if edges still exists that we could not travel to, a cyclic reference occurs
        return not courseBySuccessors
