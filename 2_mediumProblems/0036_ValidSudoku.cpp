class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        int count = 0;
        for(int i = 0; i < board.size(); i++)
        {
            count += 1;
            cout<< count << endl;
            unordered_map<int, int> hash;
            for(int j = 0; j < board[0].size(); j++)
            {
                cout<< count;
                if(board[i][j] <= 9)
                {
                    hash[board[i][j]] += 1;
                }
                if(hash[board[i][j]] > 1)
                {
                    return false;
                }
            }
            unordered_map<int, int> hash2;
            for(int j = 0; j < board[0].size(); j++)
            {
                cout<< count;
                if(board[j][i] <= 9)
                {
                    hash2[board[j][i]] += 1;
                }
                if(hash2[board[j][i]] > 1)
                {
                    return false;
                }
            }
/*            unordered_map<int, int> hash3;
            for(int j = 0; j < board[0].size(); j++)
            {
                cout<< count;
                if(board[j][i] <= 9)
                {
                    if()
                    hash2[board[j][i]] += 1;
                }
                if(hash2[board[j][i]] > 1)
                {
                    return false;
                } */
            }
        }
        return true;
    }
};