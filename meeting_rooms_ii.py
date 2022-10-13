class Solution:
    # optimal track room expiries in min heap
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        roomExpiries = []

        # sort all meeting time intervals by start time
        intervals = sorted(intervals, key=lambda interval: interval[0])

        for startTime, endTime in intervals:
            # can reuse earliest expiring room, pop it and add updated room expiry
            if roomExpiries and startTime >= roomExpiries[0]:
                heapq.heapreplace(roomExpiries, endTime)
            # no rooms exist or new meeting overlaps with others in use (earliest),
            # add new room 
            else:
                heapq.heappush(roomExpiries, endTime)

        return len(roomExpiries)

#     # suboptimal list approach
#     def minMeetingRooms(self, intervals: List[List[int]]) -> int:
#         roomExpiries = []

#         # sort all meeting time intervals by start time
#         intervals = sorted(intervals, key=lambda interval: interval[0])

#         for startTime, endTime in intervals:
#             meetingRoomPos = self.findAvailableRoom(startTime, roomExpiries)

#             # new meeting overlaps with all others in use, requiring new room
#             if meetingRoomPos < 0:
#                 roomExpiries.append(endTime)
#             # update available meeting room with new expiry time
#             else:
#                 roomExpiries[meetingRoomPos] = endTime

#         return len(roomExpiries)

#     def findAvailableRoom(self, startTime: int, roomExpiries: List[int]) -> int:
#         # find first available room that expires before new meeting
#         for i in range(len(roomExpiries)):
#             if roomExpiries[i] <= startTime:
#                 return i

#         return -1
