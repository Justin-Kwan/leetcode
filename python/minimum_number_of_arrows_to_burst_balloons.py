class Solution:
    # optimal sorting approach
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        # sort all balloon intervals by start positions to compare overlaps
        sortedPoints = sorted(points, key=lambda point: point[0])
        arrowCount = 0
        overlapEnd = sortedPoints[0][1]

        # greedily find longest sequence of overlapping intervals at a time
        for point in sortedPoints:
            # current (and future) interval does not overlap with previous
            if overlapEnd < point[0]:
                arrowCount += 1
                overlapEnd = point[1]
            # current interval overlaps, update tightest intersection bound
            else:
                overlapEnd = min(point[1], overlapEnd)

        arrowCount += 1
        return arrowCount
