class Solution {
public:
    // optimal top down dp approach
    int uniquePaths(int m, int n) {
        if (m == 0 || n == 0) {
            return 0;
        }
        vector<vector<int>> cache(m, vector<int>(n, -1));
        return countPathsFrom(cache, m - 1, n - 1);
    }

    int countPathsFrom(vector<vector<int>> &cache, int row, int col) {
        // reached out of bound cell by going up or left too far
        if (row < 0 || col < 0) {
            return 0;
        }
        // finish cell reached from a valid path
        if (row == 0 && col == 0) {
            return 1;
        }
        if (cache[row][col] != -1) {
            return cache[row][col];
        }

        // number of ways to reach finish cell from current cell is the sum
        // of number of ways to reach finish from left and above cells
        int curTotalPaths = countPathsFrom(cache, row, col - 1) +
                            countPathsFrom(cache, row - 1, col);

        cache[row][col] = curTotalPaths;
        return curTotalPaths;
    }
};
