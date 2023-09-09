class Solution {
public:
    // optimal dfs in place approach
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int maxIslandArea = 0;

        for (int row = 0; row < grid.size(); ++row) {
            for (int col = 0; col < grid[row].size(); ++col) {
                int curIslandArea = this->countIslandCells(grid, row, col);
                maxIslandArea = max(curIslandArea, maxIslandArea);
            }
        }

        return maxIslandArea;
    }

private:
    int countIslandCells(vector<vector<int>>& grid, int row, int col) {
        if (row < 0 || row >= grid.size() || col < 0 || col >= grid[row].size()) {
            return 0;
        }
        if (grid[row][col] != 1) {
            return 0;
        }

        // mark current island cell as visited
        grid[row][col] = 0;

        return this->countIslandCells(grid, row - 1, col) +
               this->countIslandCells(grid, row, col + 1) +
               this->countIslandCells(grid, row + 1, col) +
               this->countIslandCells(grid, row, col - 1) + 1;
    }
};
