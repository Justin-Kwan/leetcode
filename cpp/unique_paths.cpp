class Solution {
public:
    // optimal bottom up dp approach
    // time:  O(MN) for M rows and N columns to visit every cell and compute
    //        number of paths from it to finish in constant time based on cells
    //        to right and below
    // space: O(MN) to for M rows and N columns to build and store total paths
    //        from each cell in grid
    int uniquePaths(int m, int n) {
        if (m == 0 || n == 0) {
            return 0;
        }

        // final cell trivially has one path to itself, build up from this
        vector<vector<int>> totalPathsFromCell(m, vector<int>(n));
        totalPathsFromCell[m - 1][n - 1] = 1;

        // build up count of total paths to finish cell from each cell
        for (int row = m - 1; row >= 0; --row) {
            for (int col = n - 1; col >= 0; --col) {
                // each cell in the bottom row begins with only 1 path to finish from
                // cell to right since no cells below
                if (row + 1 < m) {
                    totalPathsFromCell[row][col] += totalPathsFromCell[row + 1][col];
                }
                // each cell in the rightmost column begins with only 1 path to finish from
                // cell below since no cells to right
                if (col + 1 < n) {
                    totalPathsFromCell[row][col] += totalPathsFromCell[row][col + 1];
                }
            }
        }

        // total paths to reach finish from start has been computed
        return totalPathsFromCell[0][0];
    }

    // // optimal top down dp approach
    // // time:  O(MN) for M rows and N columns since dfs search paths will
    // //        visit all cells, and when cells are visited from subsequent
    // //        paths, the number of paths will be cached and accessed in
    // //        constant time
    // // space: O(MN + (M+N)) => O(MN) for M rows and N columns for at most
    // //        MN cell entries in cache, and max call stack depth of M+N 
    // //        which is total distance of any path from start to end cell
    // //        (not asymptotically sigificant)
    // int uniquePaths(int m, int n) {
    //     if (m == 0 || n == 0) {
    //         return 0;
    //     }
    //     vector<vector<int>> cache(m, vector<int>(n, -1));
    //     return countPathsFrom(cache, m - 1, n - 1);
    // }

    // int countPathsFrom(vector<vector<int>> &cache, int row, int col) {
    //     // reached out of bound cell by going up or left too far
    //     if (row < 0 || col < 0) {
    //         return 0;
    //     }
    //     // finish cell reached from a valid path
    //     if (row == 0 && col == 0) {
    //         return 1;
    //     }
    //     if (cache[row][col] != -1) {
    //         return cache[row][col];
    //     }

    //     // number of ways to reach finish cell from current cell is the sum
    //     // of number of ways to reach finish from left and above cells
    //     int curTotalPaths = countPathsFrom(cache, row, col - 1) +
    //                         countPathsFrom(cache, row - 1, col);

    //     cache[row][col] = curTotalPaths;
    //     return curTotalPaths;
    // }
};
