class Solution:
#     # suboptimal sorting approach
#     def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
#         # merge and sort new interval into existing ones
#         intervals.append(newInterval)
#         intervals = sorted(intervals, key = lambda interval: interval[0])

#         mergedIntervals = [intervals[0]]

#         for i in range(1, len(intervals)):
#             numMerged = len(mergedIntervals)

#             # current interval is beyond previously written, add it
#             if intervals[i][0] > mergedIntervals[numMerged - 1][1]:
#                 mergedIntervals.append(intervals[i])
#             # current interval starting value "dips" into previously written
#             # since intervals are sorted by starting value), extend if possible
#             else:
#                 mergedIntervals[numMerged - 1][1] = max(intervals[i][1], mergedIntervals[numMerged - 1][1])

#         return mergedIntervals

    # optimal greedy approach
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        mergedIntervals = []

        for i in range(len(intervals)):
            # new interval falls before current one, add it and remaining intervals
            if newInterval[1] < intervals[i][0]:
                mergedIntervals.append(newInterval)
                mergedIntervals.extend(intervals[i:])
                return mergedIntervals
            # new interval is beyond current one, add current one and continue
            if newInterval[0] > intervals[i][1]:
                mergedIntervals.append(intervals[i])
            # new interval overlaps with current interval, update new interval
            # as local max of overlapping start and end bounds
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])

        # new interval (or local max merged interval) is beyond all intervals
        mergedIntervals.append(newInterval)
        return mergedIntervals
