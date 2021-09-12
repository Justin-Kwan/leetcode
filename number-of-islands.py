class Solution:

    # dfs approach, auxilliary structure to track visited island tiles
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rowCount = len(grid)
        colCount = len(grid[0])

        islandCount = 0
        visitedIslandCells = set()

        for rowPos in range(0, rowCount):
            for colPos in range(0, colCount):
                if grid[rowPos][colPos] == "1" and (rowPos, colPos) not in visitedIslandCells:
                    self.searchCellsInIsland(rowPos, colPos, grid, visitedIslandCells)
                    islandCount += 1

        return islandCount

    def searchCellsInIsland(self, rowPos: int, colPos: int, grid: List[List[str]], visitedIslandCells: set[str]):
        isCellOutOfBounds = rowPos < 0 or rowPos >= len(grid) or colPos < 0 or colPos >= len(grid[0])

        if isCellOutOfBounds or grid[rowPos][colPos] == "0" or (rowPos, colPos) in visitedIslandCells:
            return

        visitedIslandCells.add((rowPos, colPos))

        self.searchCellsInIsland(rowPos + 1, colPos, grid, visitedIslandCells)
        self.searchCellsInIsland(rowPos - 1, colPos, grid, visitedIslandCells)
        self.searchCellsInIsland(rowPos, colPos + 1, grid, visitedIslandCells)
        self.searchCellsInIsland(rowPos, colPos - 1, grid, visitedIslandCells)
        
#     # dfs approach, writing over visited island tiles as water
#     def numIslands(self, grid: List[List[str]]) -> int:
#         if not grid:
#             return 0

#         islandCount = 0
#         gridRowCount = len(grid)
#         gridColCount = len(grid[0])

#         for cellRow in range(0, gridRowCount):
#             for cellCol in range(0, gridColCount):
#                 if grid[cellRow][cellCol] == "1":
#                     self.searchCellsInIsland(cellRow, cellCol, grid)
#                     islandCount += 1
                    
#         return islandCount

#     def searchCellsInIsland(self, cellRow: int, cellCol: int, grid: List[List[str]]):
#         isCellOutOfBounds = cellRow < 0 or cellRow >= len(grid) or cellCol < 0 or cellCol >= len(grid[0])

#         if isCellOutOfBounds or grid[cellRow][cellCol] == "0":
#             return

#         grid[cellRow][cellCol] = "0"

#         self.searchCellsInIsland(cellRow + 1, cellCol, grid)
#         self.searchCellsInIsland(cellRow - 1, cellCol, grid)
#         self.searchCellsInIsland(cellRow, cellCol + 1, grid)
#         self.searchCellsInIsland(cellRow, cellCol - 1, grid)

