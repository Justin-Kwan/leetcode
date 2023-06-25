class Solution:
    # optimal quick select approach
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if not points or k <= 0:
            return []

        # partition closer and further points around kth ordered point
        self.selectKthPoint(points, k, 0, len(points) - 1)
        return points[:k]

    def selectKthPoint(self, points: List[List[int]], k: int, start: int, end: int):
        # finally reached kth ordered point
        if start == end:
            return

        pivotPos = self.partition(points, start, end)
        # pivoit point is kth closest, found early
        if pivotPos == k - 1:
            return
        # kth closest in larger partition, left partition part of k closest
        elif pivotPos < k - 1:
            self.selectKthPoint(points, k, pivotPos + 1, end)
        # kth closest in smaller partition, right partition discarded
        else:
            self.selectKthPoint(points, k, start, pivotPos - 1)

    def partition(self, points: List[List[int]], start: int, end: int) -> int:
        # temporarily move pivot out of way to end
        pivotPos = random.randrange(start, end)
        points[pivotPos], points[end] = points[end], points[pivotPos]

        # partition all points around pivot by distance
        nextCloserPos = start
        for i in range(start, end):
            # throw all closer points to pivot left partition
            if self.distToOrigin(points[i]) <= self.distToOrigin(points[end]):
                points[nextCloserPos], points[i] = points[i], points[nextCloserPos]
                nextCloserPos += 1

        # put pivot back right after left partition since last element skipped
        points[nextCloserPos], points[end] = points[end], points[nextCloserPos]
        return nextCloserPos

    def distToOrigin(self, point: List[int]) -> float:
        return sqrt(pow(point[0], 2) + pow(point[1], 2))

    # # optimal max heap approach
    # def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    #     if not points or k <= 0:
    #         return []

    #     kClosestPoints = []

    #     # keep running track of top k closest points
    #     for point in points:
    #         pointOriginDist = sqrt(pow(point[0], 2) + pow(point[1], 2))

    #         # always insert each point with distance in "max" heap, it's either within
    #         # k so k+1th bubbles up and is ejected or it's outside k and is ejected
    #         heapq.heappush(kClosestPoints, (-pointOriginDist, point))
    #         if len(kClosestPoints) > k:
    #             heapq.heappop(kClosestPoints)

    #     # return k closest points in ascending order
    #     # kClosestOrdered = collections.deque()
    #     # while kClosestPoints:
    #     #     _, point = heapq.heappop(kClosestPoints)
    #     #     kClosestOrdered.appendleft([point[0], point[1]])

    #     # return k closest points unordered
    #     return map(lambda distPoint: distPoint[1], kClosestPoints)
