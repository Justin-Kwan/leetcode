class Solution {
public:
    // optimal four boundaries approach
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        if (matrix.empty()) {
            return {};
        }

        // initial border boundaries for scanning matrix in spiral
        int totalRows = matrix.size(), totalCols = matrix[0].size();
        int topRow = 0, bottomRow = totalRows - 1;
        int leftCol = 0, rightCol = totalCols - 1;

        vector<int> spiralNums;
        while (spiralNums.size() < totalRows * totalCols) {
            // scan top row of spiral, left to right
            for (int col = leftCol; col <= rightCol; ++col) {
                spiralNums.push_back(matrix[topRow][col]);
            }

            // scan right column of spiral, top to bottom (skip top right)
            for (int row = topRow + 1; row <= bottomRow; ++row) {
                spiralNums.push_back(matrix[row][rightCol]);
            }

            // scan bottom row of spiral, right to left (skip bottom right)
            // do not scan if it's the same top row already scanned left to right
            if (topRow != bottomRow) {
                for (int col = rightCol - 1; col >= leftCol; --col) {
                    spiralNums.push_back(matrix[bottomRow][col]);
                }
            }

            // scan left column of spiral, bottom to top (skip bottom left and top left)
            // do not scan if it's the same right column already scanned top to bottom
            if (leftCol != rightCol) {
                for (int row = bottomRow - 1; row > topRow; --row) {
                    spiralNums.push_back(matrix[row][leftCol]);
                }
            }

            // shift in bounds on all four sides
            ++topRow; --bottomRow;
            ++leftCol; --rightCol;
        }

        return spiralNums;
    }
};
