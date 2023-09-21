class Solution {
public:
    // optimal iterative approach
    int countBattleships(vector<vector<char>> &board) {
        if (board.empty()) {
            return 0;
        }

        int totalBattleships = 0;
        for (int row = 0; row < board.size(); ++row) {
            for (int col = 0; col < board[row].size(); ++col) {
                // only increment total ships if current cell is the first seen of a ship
                if (board[row][col] == 'X' && isFirstShipCell(board, row, col)) {
                    ++totalBattleships;
                }
            }
        }

        return totalBattleships;
    }

    bool isFirstShipCell(vector<vector<char>> &board, int row, int col) {
        bool isWaterAbove = row - 1 < 0 || board[row - 1][col] == '.';
        bool isWaterBelow = row + 1 >= board.size() || board[row + 1][col] == '.';
        bool isWaterToLeft = col - 1 < 0 || board[row][col - 1] == '.';
        bool isWaterToRight = col + 1 >= board[row].size() || board[row][col + 1] == '.';

        // two properties for the first cell of a ship while scanning left to right for
        // vertical or horizontal ship
        return (isWaterAbove && isWaterToLeft && isWaterBelow) ||
               (isWaterAbove && isWaterToLeft && isWaterToRight);
    }

    // // iterative approach
    // int countBattleships(vector<vector<char>> &board) {
    //     if (board.empty()) {
    //         return 0;
    //     }

    //     int totalBattleships = 0;
    //     vector<vector<char>> shipCells(board.size(), vector<char>(board[0].size(), '.'));

    //     for (int row = 0; row < board.size(); ++row) {
    //         for (int col = 0; col < board[row].size(); ++col) {
    //             if (board[row][col] != 'X') {
    //                 continue;
    //             }

    //             // only increment total ships if current cell is the first seen of a ship
    //             // (where no four adjacent cells have a ship cell seen)
    //             if (isFirstShipCell(shipCells, row, col)) {
    //                 ++totalBattleships;
    //             }
    //             // mark current cell with ship so adjacent cells do not increment total ships
    //             shipCells[row][col] = 'X';
    //         }
    //     }

    //     return totalBattleships;
    // }

    // bool isFirstShipCell(vector<vector<char>> &shipCells, int row, int col) {
    //     // cell starts a new ship if surrounding cells in four directions
    //     // are water cells
    //     for (auto &[rowMove, colMove] : cellMoves) {
    //         int nextRow = row + rowMove, nextCol = col + colMove;
    //         bool isInRange = row >= 0 && nextRow < shipCells.size() && nextCol >= 0 && nextCol < shipCells[row].size();

    //         // another cell of current ship has already been seen at an adjacent cell 
    //         if (isInRange && shipCells[nextRow][nextCol] == 'X') {
    //             return false;
    //         }
    //     }
    //     return true;
    // }

    // // dfs approach
    // int countBattleships(vector<vector<char>>& board) {
    //     int totalBattleships = 0;
        
    //     vector<pair<int, int>> cellMoves = { {-1, 0}, {0, 1}, {1, 0}, {0, -1} };
    //     for (int row = 0; row < board.size(); ++row) {
    //         for (int col = 0; col < board[row].size(); ++col) {
    //             if (board[row][col] == 'X') {
    //                 searchBattleship(board, cellMoves, row, col);
    //                 ++totalBattleships;
    //             }
    //         }
    //     }

    //     return totalBattleships;
    // }

    // void searchBattleship(vector<vector<char>> &board, vector<pair<int, int>> &cellMoves, int row, int col) {
    //     // out of range
    //     if (row < 0 || row >= board.size() || col < 0 || col >= board[row].size()) {
    //         return;
    //     }
    //     // no battleship at cell or already visited this battleship cell
    //     if (board[row][col] != 'X') {
    //         return;
    //     }

    //     // mark current ship cell as visited
    //     board[row][col] = '.';

    //     // search for continuation of current ship in all four directons since assuming
    //     // no two ships can be adjacent
    //     for (auto &[rowMove, colMove] : cellMoves) {
    //         searchBattleship(board, cellMoves, row + rowMove, col + colMove);
    //     }
    // }
};
