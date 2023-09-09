class Solution:
    
    # merged intervals: [[1,3], [8,10], [15,18]]
    # intervals: [[1,3],[2,6],[8,10],[15,18]]
    
    # merged intervals: [[1,17],[13,17]]  mi  = 1
    # intervals: [[1,4],[4,5],[4,10],[10,17],[10,11][13,14]]

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        
        mergedIntervals = [intervals[0]]
        currMergedInterval = 0

        for i in range(1, len(intervals)):
            if intervals[i][0] <= mergedIntervals[currMergedInterval][1]:

                mergedIntervals[currMergedInterval] = [
                    mergedIntervals[currMergedInterval][0],
                    max(intervals[i][1], mergedIntervals[currMergedInterval][1])
                ]
            else:
                mergedIntervals.append(intervals[i])
                currMergedInterval += 1
        
        return mergedIntervals
