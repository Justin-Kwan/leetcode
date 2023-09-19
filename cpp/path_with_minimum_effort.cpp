struct Cell {
    int row;
    int col;
    int pathEffort;

    Cell(int row, int col, int pathEffort): row{row}, col{col}, pathEffort{pathEffort} {
    }

    bool operator > (const struct Cell &other) const {
        return this->pathEffort > other.pathEffort;
    }
};

class Solution {
public:
    // prioritized bfs heap approach
    // time complexity:  O(MN * log(max(M, N))) for M rows and N columns upper bound
    //                   since BFS will visit each cell in grid once, visiting each cell
    //                   requires popping the minimum effort neighbor from the min heap
    //                   and inserting 3 neighbors back into the min heap. Since the heap
    //                   size will grow to max layer size of max(M, N) at most during BFS
    //                   search, popping and inserting neighbors back at each cell takes
    //                   log(max(M, N)) time at most
    // space complexity: O(max(M, N)) for M rows and N columns since min heap will grow
    //                   to contain at most max(M, N) cells for the largest layer in the
    //                   grid and visited cells are simply marked on original grid
    int minimumEffortPath(vector<vector<int>>& heights) {
        if (heights.empty()) {
            return 0;
        }

        int totalRows = heights.size(), totalCols = heights[0].size();
        vector<pair<int, int>> cellMoves = { {-1, 0}, {0, 1}, {1, 0}, {0, -1} };

        // prioritize neighbor cells to visit based on who minimizes max path
        // effort so far (even if all have different deltas, if they're below
        // max path threshold, any neighbor can be chosen)
        priority_queue<Cell, vector<Cell>, greater<Cell>> cellsToVisit;
        cellsToVisit.push(Cell(0, 0, 0));

        while (!cellsToVisit.empty()) {
            Cell curCell = cellsToVisit.top();
            cellsToVisit.pop();

            // reached bottom right cell
            if (curCell.row == totalRows - 1 && curCell.col == totalCols - 1) {
                return curCell.pathEffort;
            }
            // already visited
            if (heights[curCell.row][curCell.col] < 0) {
                continue;
            }

            // mark current cell as visited
            int cellHeight = heights[curCell.row][curCell.col];
            heights[curCell.row][curCell.col] = -1;

            for (auto &[rowMove, colMove] : cellMoves) {
                int nextRow = curCell.row + rowMove;
                int nextCol = curCell.col + colMove;

                // out of range
                if (nextRow < 0 || nextRow >= totalRows || nextCol < 0 || nextCol >= totalCols) {
                    continue;
                }

                // store max delta from step to step along entire path in cell
                int nextStepEffort = abs(cellHeight - heights[nextRow][nextCol]);
                int maxPathEffort = max(curCell.pathEffort, nextStepEffort);
                cellsToVisit.push(Cell(nextRow, nextCol, maxPathEffort));
            }
        }

        return -1;
    }

    // // brute force dfs approach
    // int minimumEffortPath(vector<vector<int>>& heights) {
    //     if (heights.empty()) {
    //         return 0;
    //     }
    //     return minimumEffortPathFrom(heights, 0, 0);
    // }

    // int minimumEffortPathFrom(vector<vector<int>>& heights, int row, int col) {
    //     // current min path at the final bottom left cell is 0 since no more steps needed
    //     if (row == heights.size() - 1 && col == heights[row].size() - 1) {
    //         return 0;
    //     }

    //     // mark as visited
    //     int cellHeight = heights[row][col];
    //     heights[row][col] = -1;

    //     int curMinEffortPath = INT_MAX;

    //     // min effort path from current cell is the min effort path from all 4 around it
    //     // including delta between it to the next
    //     vector<pair<int, int>> moves =  { {-1, 0}, {0, 1}, {1, 0}, {0, -1} };
    //     for (auto &[rowMove, colMove] : moves) {
    //         int nextRow = row + rowMove;
    //         int nextCol = col + colMove;

    //         // out of range
    //         if (nextRow < 0 || nextRow >= heights.size() || nextCol < 0 || nextCol >= heights[nextRow].size()) {
    //             continue;
    //         }
    //         // already visited
    //         if (heights[nextRow][nextCol] < 0) {
    //             continue;
    //         }

    //         int nextStepEffort = abs(cellHeight - heights[nextRow][nextCol]);
    //         int nextPathEffort = max(nextStepEffort, minimumEffortPathFrom(heights, nextRow, nextCol));
    //         curMinEffortPath = min(nextPathEffort, curMinEffortPath);
    //     }

    //     // mark unvisited to be visited by another path
    //     heights[row][col] = cellHeight;
    //     return curMinEffortPath;
    // }
};
