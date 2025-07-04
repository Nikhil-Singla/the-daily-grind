class Solution {
public:
    int minCostConnectPoints(vector<vector<int>>& points) 
    {
        vector<int> distance(points.size(), INT_MAX);
        int ans = 0;
        for(uint i = 0; i < points.size() - 1; i++)
        {
            for(uint j = i+1; j < points.size(); j++)
            {
                distance[j] = min(distance[j], abs(points[i][0] - points[j][0])
                                             + abs(points[i][1] - points[j][1]));
                if(distance[j] < distance[i+1])
                {
                    swap(points[j], points[i+1]);
                    swap(distance[j], distance[i+1]);
                }
            }

            
            ans += distance[i+1];
        }
        return ans;
    }
};
