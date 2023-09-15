class Solution {
public:
    // optimal transpose reflect approach
    void rotate(vector<vector<int>>& matrix) {
        // transpose all cells (rows to columns and vice versa) by reflecting diagonally
        for (int row = 0; row < matrix.size(); ++row) {
            for (int col = row; col < matrix[row].size(); ++col) {
                // transpose cell by swapping with cell at flipped row and column in
                // bottomRow triangle quadrant
                swap(matrix[row][col], matrix[col][row]);
            }
        }

        // reflect all cells vertically about y-axis to obtain rotated matrix
        for (int row = 0; row < matrix.size(); ++row) {
            int totalCols = matrix[row].size();
            for (int col = 0; col < totalCols / 2; ++col) {
                swap(matrix[row][col], matrix[row][totalCols - 1 - col]);
            }
        }
    }

    // // optimal cycle rotation approach
    // void rotate(vector<vector<int>>& matrix) {
    //     int leftCol = 0, rightCol = matrix.size() - 1;

    //     // for each square bound on current layer, rotate each cell on all four sides
    //     while (leftCol < rightCol) {
    //         for (int i = 0; i < rightCol - leftCol; ++i) {
    //             // width and height of current square layer is always the same
    //             int topRow = leftCol, bottomRow = rightCol;

    //             int topLeftCell = matrix[topRow][leftCol + i];
    //             matrix[topRow][leftCol + i] = matrix[bottomRow - i][leftCol];
    //             matrix[bottomRow - i][leftCol] = matrix[bottomRow][rightCol - i];
    //             matrix[bottomRow][rightCol - i] = matrix[topRow + i][rightCol];
    //             matrix[topRow + i][rightCol] = topLeftCell;
    //         }

    //         // reduce bounds to start rotating next inner smaller square layer
    //         ++leftCol;
    //         --rightCol;
    //     }
    // }
};
