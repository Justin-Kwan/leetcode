class Solution
{
public:
    // optimal bottom up dp approach
    int minHeightShelves(vector<vector<int>> &books, int shelfWidth)
    {
        vector<int> costs(books.size() + 1, INT_MAX);
        costs[books.size()] = 0;

        for (int i = books.size() - 1; i >= 0; --i)
        {
            int curWidth = 0, curHeight = 0;

            // minimum height when arrange ith to nth books depends on minimum
            // height when arranging all configurations with ith book as first
            //
            // for every configuration where current book is the first of the row,
            // update the current shelf's height and sum with the next row's total
            // height (precomputed at book k away)
            for (int j = i; j < books.size(); ++j)
            {
                int bookWidth = books[j][0], bookHeight = books[j][1];
                if (curWidth + bookWidth > shelfWidth)
                {
                    break;
                }

                curWidth += bookWidth;
                curHeight = max(curHeight, bookHeight);
                costs[i] = min(costs[i], curHeight + costs[j + 1]);
            }
        }

        return costs[0];
    }

    // // optimal top down dp approach
    // int minHeightShelves(vector<vector<int>> &books, int shelfWidth) {
    //     vector<vector<int>> cache(books.size(), vector<int>(shelfWidth + 1, -1));
    //     return findMinHeight(cache, books, 0, 0, 0, shelfWidth);
    // }

    // int findMinHeight(vector<vector<int>> &cache, vector<vector<int>> &books, int i, int curWidth, int curShelfHeight, int shelfWidth) {
    //     // base case is reached the last book's height
    //     if (i >= books.size()) {
    //         return curShelfHeight;
    //     }

    //     if (cache[i][curWidth] != -1) {
    //         return cache[i][curWidth];
    //     }

    //     int bookWidth = books[i][0], bookHeight = books[i][1];

    //     // find min total height when appending and newlining the book
    //     int heightFromCur = INT_MAX, heightFromNext;

    //     if (curWidth + bookWidth <= shelfWidth) {
    //         heightFromCur = findMinHeight(cache, books, i + 1, curWidth + bookWidth, max(curShelfHeight, bookHeight), shelfWidth);
    //     }

    //     heightFromNext = findMinHeight(cache, books, i + 1, bookWidth, bookHeight, shelfWidth);

    //     return cache[i][curWidth] = min(heightFromCur, curShelfHeight + heightFromNext);
    // }
};
