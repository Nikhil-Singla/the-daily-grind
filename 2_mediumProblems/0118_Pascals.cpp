class Solution {
public:
    vector<vector<int>> generate(int numRows) 
    {
        vector<vector<int>> v;
        v.push_back({1});
        if(numRows < 2) {return v;}
        for(int i = 1; i < numRows; i++)
        {
            vector<int> row(i+1);
            row[0] = 1;
            row[i] = 1;
            for(int j = 1; j < i; j++)
            {
                row[j] = v[i-1][j-1] + v[i-1][j];
            }
            v.push_back(row);
        }
        return v;
    }
};