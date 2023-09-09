class Solution:
# test cases:
#     input:        [[0,30],[5,10],[15,20]]
# after sorting:    [[5,10],[15,20],[0,30]]
# checking overlaps:[[5,10],[15,20],[0,30]]
# => false

# input: [[0,5]]
# => true

    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:

        # sort by each element's 1th element
        intervals.sort(key = lambda x:x[1])

        # check that there are no overlaps between a given interval's starting and previous interval's ending time
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False

        return True

