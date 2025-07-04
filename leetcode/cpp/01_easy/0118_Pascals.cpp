class Solution {
public:
    vector<vector<int>> generate(int numRows) 
    {
        vector<vector<int>> triangle;
        vector<int> row = {1};
        triangle.push_back(row);
        if(numRows == 1)
        {return triangle;}
        for(int i = 1; i < numRows; i++)
        {
            vector<int> temp = {1, 1};
            for(int j = 1; j < i; j++)
            {
                temp.insert(temp.begin()+1, triangle[i-1][j-1] + triangle[i-1][j]);
            }
            triangle.push_back(temp);
        }
        return triangle;
    }
};

class Solution {
public:
    vector<vector<int>> generate(int numRows) 
    {
        vector<vector<int>> v;
        v.push_back({1});
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