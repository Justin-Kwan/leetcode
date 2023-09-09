class Solution:
    # optimized bfs approach
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] != 0:
            return -1

        visitedCells = set()
        targetCell = (len(grid) - 1, len(grid[0]) - 1)

        pathLength = 1
        neighborsToVisit = collections.deque([(0, 0)])

        while neighborsToVisit:
            # for every node in current layer, add its children
            for _ in range(0, len(neighborsToVisit)):
                cell = neighborsToVisit.popleft()

                if cell == targetCell:
                    return pathLength

                for neighborCell in self.getNeighborsCells(cell):
                    nRow, nCol = neighborCell[0], neighborCell[1]
                    isNeighborInRange = nRow >= 0 and nRow < len(grid) and nCol >= 0 and nCol < len(grid[0])

                    if isNeighborInRange and grid[nRow][nCol] == 0 and neighborCell not in visitedCells:
                            neighborsToVisit.append(neighborCell)
                            visitedCells.add(neighborCell)

            pathLength += 1

        return -1

    def getNeighborsCells(self, cell: tuple[int, int]):
        row, col = cell[0], cell[1]

        return [
            (row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1),
            (row + 1, col - 1), (row - 1, col + 1), (row - 1, col - 1), (row + 1, col + 1)]


#     # brute force dfs
#     def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
#         if not grid:
#             return -1

#         minPathToEnd = self.findMinPathToEnd(grid, 0, 0)

#         if minPathToEnd == float('inf'):
#             return -1

#         return minPathToEnd

#     def findMinPathToEnd(self, grid: List[List[int]], row: int, col: int) -> int:
#         # out of bounds
#         if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
#             return float('inf')

#         # not in path
#         if grid[row][col] != 0:
#             return float('inf')

#         # reached end
#         if row == len(grid) - 1 and col == len(grid[0]) - 1:
#             return 1

#         minPathToEnd = float('inf')
#         grid[row][col] = 1

#         for neighborRow in range(row - 1, row + 2):
#             for neighborCol in range(col - 1, col + 2):
#                 minPathToEnd = min(minPathToEnd, self.findMinPathToEnd(grid, neighborRow, neighborCol))

#         grid[row][col] = 0
 
#         return minPathToEnd + 1
