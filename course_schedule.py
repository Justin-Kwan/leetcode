class Solution:
    # optimal dfs cycle detection
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # track courses already visited along path to detect cyclic links
        # and cache whether course node is already completable
        visited = {}
        # add all valid course keys that could be accessed, even if not in prerequisites
        courseByPrereqs = {course: [] for course in range(numCourses)}

        if not prerequisites:
            return True

        # build graph of each course node by adjacency list of prerequisites
        for course, prereqCourse in prerequisites:
            courseByPrereqs[course].append(prereqCourse)

        # check every course is completable (having no cycles in prerequisites)
        for course in range(numCourses):
            if not self.isCourseCompletable(course, courseByPrereqs, visited):
                return False

        return True

    def isCourseCompletable(self, course: int, courseByPrereqs: Dict[int, List[int]], visited: Dict[int, bool]) -> bool:
        # cyclic prerequisites exist if course was already visited along current dfs path
        if course in visited and not visited[course]:
            return False

        # course has no preqreuisites and thus is completable or
        # course is already computed to be completable in cache from previous dfs path
        if courseByPrereqs[course] == [] or (course in visited and visited[course]):
            return True

        # mark current course as visited but not known as completable
        visited[course] = False

        # current course is completable only if all its prerequisites are completable
        for prereqCourse in courseByPrereqs[course]:
            if not self.isCourseCompletable(prereqCourse, courseByPrereqs, visited):
                return False

        visited[course] = True
        return visited[course]
