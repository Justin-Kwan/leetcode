class Solution:
    
    # merged intervals: [[1,3], [8,10], [15,18]]
    # intervals: [[1,3],[2,6],[8,10],[15,18]]
    
    # merged intervals: [[1,17],[13,17]]  mi  = 1
    # intervals: [[1,4],[4,5],[4,10],[10,17],[10,11][13,14]]

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key = lambda x:x[0])
        mergedIntervals = [intervals[0]]

        for interval in intervals:
            if mergedIntervals[-1][1] < interval[0]:
                # current interval comes after last merged interval so append it
                # and compare future intervals against it
                mergedIntervals.append(interval)
            else:
                # last merged interval's end crosses current interval's start so
                # take max of both ends
                #
                # last merged interval should keep its start since it's always less
                # or equal to current interval's start
                mergedIntervals[-1][1] = max(interval[1], mergedIntervals[-1][1])

        return mergedIntervals
