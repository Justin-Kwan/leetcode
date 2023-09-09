class Solution:
    # dfs in place approach
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        maxIslandArea = 0

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                curIslandArea = self.countIslandCells(grid, row, col)
                maxIslandArea = max(curIslandArea, maxIslandArea)

        return maxIslandArea

    def countIslandCells(self, grid: List[List[int]], row: int, col: int) -> int:
        # no island cells reachable when out of bounds, at water or already visited
        if (row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row]) or
            grid[row][col] != 1):
            return 0

        # mark current island cell as visited (water) before traversing
        # to avoid double counting it from another path, do not unmark
        grid[row][col] = 0

        # cells reachable from current is 1 + cells reachable from neighbors
        return (self.countIslandCells(grid, row - 1, col) +
                self.countIslandCells(grid, row, col + 1) +
                self.countIslandCells(grid, row + 1, col) +
                self.countIslandCells(grid, row, col - 1)) + 1

    # # bfs in place approach
    # def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    #     if not grid:
    #         return 0

    #     maxIslandArea = 0

    #     for row in range(len(grid)):
    #         for col in range(len(grid[row])):
    #             curIslandArea = self.countIslandCells(grid, row, col)
    #             maxIslandArea = max(curIslandArea, maxIslandArea)

    #     return maxIslandArea

    # def countIslandCells(self, grid: List[List[int]], row: int, col: int) -> int:
    #     if grid[row][col] != 1:
    #         return 0

    #     # start bfs from first seen island cell, premark it as visited
    #     totalCells, grid[row][col] = 1, 0
    #     cellsToVisit = collections.deque([(row, col)])

    #     while cellsToVisit:
    #         # each island cell already accounted for once dequeued
    #         curRow, curCol = cellsToVisit.popleft()

    #         for rowMove, colMove in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
    #             nextRow, nextCol = curRow + rowMove, curCol + colMove

    #             # do not queue out of bounds, water, or already visited island cells
    #             if (nextRow < 0 or nextRow >= len(grid) or nextCol < 0 or nextCol >= len(grid[nextRow]) or
    #                 grid[nextRow][nextCol] == 0):
    #                 continue

    #             # mark next cell as visited to avoid double queueing from another neighbor
    #             grid[nextRow][nextCol] = 0
    #             totalCells += 1
    #             cellsToVisit.append((curRow + rowMove, curCol + colMove))

    #     return totalCells

    # # dfs visited set approach
    # def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    #     if not grid:
    #         return 0

    #     maxIslandArea = 0
    #     visited = [[False] * len(grid[0]) for row in grid]

    #     for row in range(len(grid)):
    #         for col in range(len(grid[row])):
    #             curIslandArea = self.countIslandCells(grid, visited, row, col)
    #             maxIslandArea = max(curIslandArea, maxIslandArea)

    #     return maxIslandArea

    # def countIslandCells(self, grid: List[List[int]], visited: List[List[int]], row: int, col: int) -> int:
    #     # no island cells reachable when out of bounds, at water or already visited
    #     if (row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row]) or
    #         grid[row][col] == 0 or visited[row][col] == True):
    #         return 0

    #     # mark current island cell as visited before traversing to avoid
    #     # double counting it from another path, do not unmark
    #     visited[row][col] = True

    #     # cells reachable from current is 1 + cells reachable from neighbors
    #     return (self.countIslandCells(grid, visited, row - 1, col) +
    #             self.countIslandCells(grid, visited, row, col + 1) +
    #             self.countIslandCells(grid, visited, row + 1, col) +
    #             self.countIslandCells(grid, visited, row, col - 1)) + 1
