class Solution:
    # optomized track room expiries in min heap
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # underlying list to store expiries as nodes in heap
        roomExpiries = []
        intervals.sort(key = lambda interval: interval[0])
        
        for interval in intervals:
            # exists a room expiry and earliest expiring room (root) is before meeting start
            if roomExpiries and roomExpiries[0] <= interval[0]:
                heapq.heapreplace(roomExpiries, interval[1])    # pop earliest expiry and add new room expiry as end of meeting
            else:
                heapq.heappush(roomExpiries, interval[1])       # checkout new room and add expiry
        return len(roomExpiries)
    
#     # unoptimized track room expiries in list
#     def minMeetingRooms(self, intervals: List[List[int]]) -> int:
#         roomExpiries = []

#         intervals.sort(key = lambda interval: interval[0])

#         for interval in intervals:
#             earliestRoomExpiryPos = self.findEarliesRoomExpiryPos(roomExpiries)

#             # if room exists and expires before meeting, meeting can use
#             if earliestRoomExpiryPos != -1 and roomExpiries[earliestRoomExpiryPos] <= interval[0]:
#                 roomExpiries[earliestRoomExpiryPos] = interval[1]   # update expiry to end of meeting
#             else:
#                 roomExpiries.append(interval[1])   # checkout meeting room, and set expiry

#         return len(roomExpiries)

#     def findEarliesRoomExpiryPos(self, roomExpiries: List[int]) -> int:
#         minRoomExpiry = float('inf')
#         minRoomExpiryPos = -1

#         for i in range(0, len(roomExpiries)):
#             if roomExpiries[i] < minRoomExpiry:
#                 minRoomExpiry = roomExpiries[i]
#                 minRoomExpiryPos = i

#         return minRoomExpiryPos
