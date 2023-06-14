class Solution:
    # optimal backwards bfs
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacificToVisit, atlanticToVisit = collections.deque(), collections.deque()

        # queue all vertical pacitic and atlantic edges to bfs from
        for row in range(len(heights)):
            pacificToVisit.append((row, 0))
            atlanticToVisit.append((row, len(heights[row]) - 1))

        # queue all horizontal pacitic and atlantic edges to bfs from
        for col in range(len(heights[0])):
            pacificToVisit.append((0, col))
            atlanticToVisit.append((len(heights) - 1, col))

        pacificPath = self.searchOceanPath(heights, pacificToVisit)
        atlanticPath = self.searchOceanPath(heights, atlanticToVisit)
        return pacificPath.intersection(atlanticPath)

    def searchOceanPath(self, heights: List[List[int]], cellsToVisit: Deque[Tuple[int, int]]) -> Set[Tuple[int, int]]:
        path = set()
        while cellsToVisit:
            row, col = cellsToVisit.popleft()

            # reject cells that have already been visited since a cell could be queued
            # twice by two cells in the same search layer
            if (row, col) in path:
                continue
            path.add((row, col))

            # continue bfs on all surrounding cells that can reach ocean
            for rowMove, colMove in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nextRow, nextCol = row + rowMove, col + colMove
                # out of grid bounds
                if nextRow < 0 or nextRow >= len(heights) or nextCol < 0 or nextCol >= len(heights[0]):
                    continue
                # water cannot flow from next cell to current
                if heights[row][col] > heights[nextRow][nextCol]:
                    continue
                # next cell already visited as reachable or queued to visit
                if (nextRow, nextCol) in path:
                    continue
                # cell could already be queued, queue it again and deal with later
                cellsToVisit.append((nextRow, nextCol))

        return path

    # # optimal backwards dfs with cache
    # def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    #     pacificPath, atlanticPath = set(), set()

    #     # search water flow paths from vertical pacific and atlantic edges
    #     for row in range(len(heights)):
    #         self.searchOceanPath(row, 0, heights, pacificPath)
    #         self.searchOceanPath(row, len(heights[row]) - 1, heights, atlanticPath)

    #     # search water flow paths from horizontal pacific and atlantic edges
    #     for col in range(len(heights[0])):
    #         self.searchOceanPath(0, col, heights, pacificPath)
    #         self.searchOceanPath(len(heights) - 1, col, heights, atlanticPath)

    #     # take all cells reachable from both oceans
    #     return pacificPath.intersection(atlanticPath)

    # def searchOceanPath(self, row: int, col: int, heights: List[List[int]], path: Set[Tuple[int, int]]):
    #     # current cell can reach ocean, add to seen path
    #     path.add((row, col))

    #     # dfs to all surrounding cells also reachable from ocean
    #     for rowMove, colMove in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
    #         nextRow, nextCol = row + rowMove, col + colMove

    #         # out of grid bounds
    #         if nextRow < 0 or nextRow >= len(heights) or nextCol < 0 or nextCol >= len(heights[row]):
    #             continue
    #         # water cannot flow from next cell to current
    #         if heights[nextRow][nextCol] < heights[row][col]:
    #             continue
    #         # cell already visited and added to seen path
    #         if (nextRow, nextCol) in path:
    #             continue

    #         self.searchOceanPath(nextRow, nextCol, heights, path)

    # # dfs with cache
    # def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    #     atlanticCache, pacificCache = set(), set()
    #     cellsReachingOcean = []

    #     # search at each cell to see if it can reach each both oceans
    #     for row in range(len(heights)):
    #         for col in range(len(heights[row])):
    #             if (self.isOceanReached("atlantic", row, col, heights, atlanticCache) and
    #                 self.isOceanReached("pacific", row, col, heights, pacificCache)):
    #                 cellsReachingOcean.append([row, col])

    #     return cellsReachingOcean

    # def isOceanReached(self, ocean: str, row: int, col: int, heights: List[List[int]], cache: Set[Tuple[int, int]]) -> bool:
    #     # reached edge of island which always flows to ocean
    #     isPacificReached = ocean == "pacific" and (row == 0 or col == 0)
    #     isAtlanticReached = ocean == "atlantic" and (row == len(heights) - 1 or col == len(heights[0]) - 1)

    #     if isPacificReached or isAtlanticReached or (row, col) in cache:
    #         return True

    #     # temporarily prevent recursing back to current cell
    #     cellHeight = heights[row][col]
    #     heights[row][col] = float('inf')

    #     # dfs for path to ocean from current cell
    #     isReached = False
    #     for rowMove, colMove in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
    #         nextRow, nextCol = row + rowMove, col + colMove
    #         isValidNeighbor = (nextRow >= 0 and nextRow < len(heights) and
    #                            nextCol >= 0 and nextCol < len(heights[row]) and
    #                            heights[nextRow][nextCol] <= cellHeight)

    #         if isValidNeighbor and self.isOceanReached(ocean, nextRow, nextCol, heights, cache):
    #             isReached = True
    #             cache.add((row, col))
    #             break

    #     heights[row][col] = cellHeight
    #     return isReached
