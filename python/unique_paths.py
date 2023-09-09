class Solution:
#     # brute force dfs
#     def uniquePaths(self, m: int, n: int) -> int:
#         # subproblem: how many ways to reach finish from any point on grid?

#         # out of bounds, so invalid path
#         if m < 1 or n < 1:
#             return 0

#         # finish reached from valid path 
#         if m == 1 and n == 1:
#             return 1

#         return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)

    # optimized memoized dfs
    def uniquePaths(self, m: int, n: int) -> int:
        return self.countUniquePaths(m, n, {})

    def countUniquePaths(self, row: int, col: int, cache: dict[tuple[int, int], int]) -> int:
        # subproblem: how many ways to reach finish from any point on grid?

        # hit cache to get path count
        if (row, col) in cache:
            return cache[(row, col)]

        # out of bounds, so invalid path
        if row < 1 or col < 1:
            return 0

        # finish reached from valid path 
        if row == 1 and col == 1:
            return 1

        pathCountFromCell = self.countUniquePaths(row - 1, col, cache) + self.countUniquePaths(row, col - 1, cache)

        # cache path count to finish from current cell
        cache[(row, col)] = pathCountFromCell
        return pathCountFromCell
