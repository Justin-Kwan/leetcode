class Solution:
    # max heap approach
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if not points or k <= 0:
            return []

        kClosestPoints = []

        # keep running track of top k closest points
        for point in points:
            pointOriginDist = sqrt(pow(point[0], 2) + pow(point[1], 2))

            # always insert each point with distance in "max" heap, it's either within
            # k so k+1th bubbles up and is ejected or it's outside k and is ejected
            heapq.heappush(kClosestPoints, (-pointOriginDist, point))
            if len(kClosestPoints) > k:
                heapq.heappop(kClosestPoints)

        # return k closest points in ascending order
        # kClosestOrdered = collections.deque()
        # while kClosestPoints:
        #     _, point = heapq.heappop(kClosestPoints)
        #     kClosestOrdered.appendleft([point[0], point[1]])

        # return k closest points unordered
        return map(lambda distPoint: distPoint[1], kClosestPoints)
