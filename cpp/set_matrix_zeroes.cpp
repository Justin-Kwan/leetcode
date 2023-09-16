class Solution {
public:
    // optimal modify matrix approach
    void setZeroes(vector<vector<int>>& matrix) {
        if (matrix.empty()) {
            return;
        }

        bool isTopRowZero = false;
        bool isLeftColZero = false;

        // seperately check first row (top) and first column (left) for zeroes since
        // they do not have their own first cell in row and column to mark
        for (int col = 0; col < matrix[0].size(); ++col) {
            if (matrix[0][col] == 0) {
                isTopRowZero = true;
            }
        }
        for (int row = 0; row < matrix.size(); ++row) {
            if (matrix[row][0] == 0) {
                isLeftColZero = true;
            }
        }

        // check interior cells for any zeroes, using the first cell of row or of
        // column to indicate whether entire row or column should have zero
        for (int row = 1; row < matrix.size(); ++row) {
            for (int col = 1; col < matrix[row].size(); ++col) {
                if (matrix[row][col] == 0) {
                    matrix[row][0] = 0;
                    matrix[0][col] = 0;
                }
            }
        }

        // set all interior cells to zero as necessary according to first row and
        // column cell indicators
        //
        // must complete before updating the indicator row and columns themselves
        for (int row = 1; row < matrix.size(); ++row) {
            for (int col = 1; col < matrix[row].size(); ++col) {
                // set cell to 0 if its entire row or entire column should be filled
                if (matrix[row][0] == 0 || matrix[0][col] == 0) {
                    matrix[row][col] = 0;
                }
            }
        }

        // set cells in first (top) row and first (left) column to zero according to
        // their seperate boolean indicators
        if (isTopRowZero) {
            for (int col = 0; col < matrix[0].size(); ++col) {
                matrix[0][col] = 0;
            }
        }
        if (isLeftColZero) {
            for (int row = 0; row < matrix.size(); ++row) {
                matrix[row][0] = 0;
            }
        } 
    }

    // // suboptimal caching approach
    // void setZeroes(vector<vector<int>>& matrix) {
    //     if (matrix.empty()) {
    //         return;
    //     }

    //     // cache each row and column that should be filled with 0's
    //     vector<bool> rowsWithZero(matrix.size(), false);
    //     vector<bool> colsWithZero(matrix[0].size(), false);

    //     // mark row and column that should be filled with 0's when 0 cell found
    //     for (int row = 0; row < matrix.size(); ++row) {
    //         for (int col = 0; col < matrix[row].size(); ++col) {
    //             if (matrix[row][col] == 0) {
    //                 rowsWithZero[row] = true;
    //                 colsWithZero[col] = true;
    //             }
    //         }
    //     }

    //     // replace cells in rows and columns with 0's
    //     for (int row = 0; row < matrix.size(); ++row) {
    //         for (int col = 0; col < matrix[row].size(); ++col) {
    //             if (rowsWithZero[row] || colsWithZero[col]) {
    //                 matrix[row][col] = 0;
    //             }
    //         }
    //     }
    // }

    // // broken zero padding approach
    // void setZeroes(vector<vector<int>>& matrix) {
    //     // add 0 padding to every cell value
    //     for (int row = 0; row < matrix.size(); ++row) {
    //         for (int col = 0; col < matrix[row].size(); ++col) {
    //             matrix[row][col] *= 10;

    //             // mark zero cells originally found in matrix
    //             int cellNum = matrix[row][col] / 10;
    //             if (cellNum == 0) {
    //                 ++matrix[row][col];
    //             }
    //         }
    //     }

    //     // input row:  [1, 2, 0, 5, 5, 0, 9]
    //     // output row: [0, 0, 1, 0, 0, 1, 0]
    //     // set zeroes in all rows that contain an original zero
    //     for (int row = 0; row < matrix.size(); ++row) {
    //         bool isZeroRow = false;

    //         for (int col = 0; col < matrix[row].size(); ++col) {
    //             int cellNum = matrix[row][col] / 10;

    //             // set all previous cells to left as zero on first zero cell seen in row
    //             if (cellNum == 0 && !isZeroRow) {
    //                 for (int prevCol = 0; prevCol < col; ++prevCol) {
    //                     matrix[row][prevCol] = 0;
    //                 }
    //                 // skip setting all left cells to zero on next seen zero cell
    //                 isZeroRow = true;
    //             }

    //             // only set cell to 0 if the row should have all 0's and cell is not an original 0 cell
    //             if (isZeroRow && cellNum != 0) {
    //                 matrix[row][col] = 0;
    //             }
    //         }
    //     }

    //     // set zeroes in all columns that contain an original zero
    //     for (int col = 0; col < matrix[0].size(); ++col) {
    //         bool isZeroColumn = false;

    //         for (int row = 0; row < matrix.size(); ++row) {
    //             int cellNum = matrix[row][col] / 10;
    //             bool isOriginalZero = matrix[row][col] % 10 == 1;

    //             if (cellNum == 0 && isOriginalZero) {
    //                 // set all prev cells above to zero
    //                 for (int prevRow = 0; prevRow < row; ++prevRow) {
    //                     matrix[prevRow][col] = 0;
    //                 }
    //                 isZeroColumn = true;
    //             }

    //             matrix[row][col] = isZeroColumn ? 0 : matrix[row][col] /= 10;
    //         }
    //     }
    // }
};
