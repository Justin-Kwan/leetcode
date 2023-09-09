class Solution:
#     # unoptimized dfs
#     def mincostTickets(self, days: List[int], costs: List[int]) -> int:
#         if len(days) == 0:
#             return 0

#         return self.findMinTicketsCost(days, 0, costs)

#     def findMinTicketsCost(self, days: List[int], curDayPos: int, costs: List[int]) -> int:
#         # previous ticket had enough days to complete remaining days of travelling
#         if curDayPos >= len(days):
#             return 0

#         minCostSoFar = float('inf')

#         for ticketCost, ticketDuration in zip(costs, [1, 7, 30]):
#             i = curDayPos
#             # find first dates of each ticket's expiry (cannot be used) to continue exploring from
#             # will only ever need to travel up by 30+7+1 positions in worst case if travelling on consecutive days
#             while i < len(days) and days[i] < days[curDayPos] + ticketDuration:
#                 i += 1

#             # minimum ticket combination cost 
#             minCostSoFar = min(minCostSoFar, ticketCost + self.findMinTicketsCost(days, i, costs))

#         return minCostSoFar

    # optimized memoized dfs
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        if len(days) == 0:
            return 0

        return self.findMinTicketsCost(days, 0, costs, {})

    def findMinTicketsCost(self, days: List[int], curDayPos: int, costs: List[int], cache: Dict[int, int]) -> int:
        # previous ticket had enough days to complete remaining days of travelling
        if curDayPos >= len(days):
            return 0

        if curDayPos in cache:
            return cache[curDayPos]

        minCostSoFar = float('inf')

        for ticketCost, ticketDuration in zip(costs, [1, 7, 30]):
            i = curDayPos
            # find first dates of each ticket's expiry (cannot be used) to continue exploring from
            # will only ever need to travel up by 30+7+1 positions in worst case if travelling on consecutive days
            while i < len(days) and days[i] < days[curDayPos] + ticketDuration:
                i += 1

            # minimum ticket combination cost at current day is minimum of all explored
            # options against current day + minimum cost from remaining path of days
            minCostSoFar = min(minCostSoFar, ticketCost + self.findMinTicketsCost(days, i, costs, cache))

        # cache minimum tickets cost at current day
        cache[curDayPos] = minCostSoFar
        return minCostSoFar
