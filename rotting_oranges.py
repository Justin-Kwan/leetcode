import collections

class Solution:
    # bfs approach
    def orangesRotting(self, grid: List[List[int]]) -> int:
        orangesToRot = collections.deque([])
        totalFreshOranges = 0
        totalRotMins = 0

        # find all inital rotten oranges, rotting can occur in parallel from multiple cells
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    totalFreshOranges += 1
                elif grid[row][col] == 2:
                    orangesToRot.append((row, col))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while orangesToRot:
            # only iterate through current layer, queueing next layer of fresh oranges
            # (not visited yet) to rot in next minute
            for _ in range(len(orangesToRot)):
                row, col = orangesToRot.popleft()

                # queue fresh oranges from above, below, left and right
                for direction in directions:
                    if self.isFreshOrangeAt(grid, row + direction[0], col + direction[1]):
                        orangesToRot.append((row + direction[0], col + direction[1]))
                        grid[row + direction[0]][col + direction[1]] = 2
                        totalFreshOranges -= 1

            # another minute passed only if more adjacent oranges became rotten
            if len(orangesToRot) > 0:
                totalRotMins += 1

        # unreachable fresh oranges may still exist
        return -1 if totalFreshOranges > 0 else totalRotMins

    def isFreshOrangeAt(self, grid: List[List[int]], row: int, col: int) -> bool:
        return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[row]) and grid[row][col] == 1
