class Solution {
public:
    int maxPoints(vector<vector<int>>& points) 
    {
        if(points.size() < 3)
        {
            return points.size();
        }
        uint ans = 2;
        for(uint i = 0; i < points.size(); ++i)
        {
            for(uint j = i+1; j < points.size(); ++j)
            {
                uint loopResult = 2;
                for(uint k = 0; k < points.size(); ++k)
                {
                    if(k == i || k == j)
                    {}
                    else if((points[j][1] - points[i][1])*(points[k][0] - points[j][0]) == 
                    (points[j][0] - points[i][0])*(points[k][1] - points[j][1]))
                    {
                        loopResult++;
                    }
                }
                ans = max(ans, loopResult);
            }
        }
        return ans;
    }
};