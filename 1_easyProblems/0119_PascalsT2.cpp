class Solution {
public:
    vector<int> getRow(int n) 
    {
        vector<vector<int>> v;
        v.push_back({1});
        for(uint i = 1; i <= n; i++)
        {
            vector<int> row(i+1);
            row[0] = 1;
            row[i] = 1;
            for(uint j = 1; j < i; j++)
            {
                row[j] = v[i-1][j-1] + v[i-1][j];
            }
            v.push_back(row);
        }
        return v.back();
    }
};