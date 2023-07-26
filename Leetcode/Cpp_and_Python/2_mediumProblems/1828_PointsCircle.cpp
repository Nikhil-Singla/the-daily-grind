class Solution {
public:

    int countInside(vector<vector<int>>& points, vector<int> query)
    {
        int count = 0;
        int radius_sq = query[2]*query[2]; 
        for(auto &c : points)
        {
            int xcor = query[0] - c[0];
            int ycor = query[1] - c[1];
            count += xcor*xcor + ycor*ycor <= radius_sq;  
        }
        return count;
    }

    vector<int> countPoints(vector<vector<int>>& points, vector<vector<int>>& queries) 
    {
        vector<int> ans;
        for(auto &c : queries)
        {
            ans.push_back(countInside(points, c));
        }
        return ans;
    }
};