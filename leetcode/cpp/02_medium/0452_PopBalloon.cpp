bool cmp(const vector<int>& v1,const vector<int>& v2) 
{ 
    return v1[1] < v2[1]; 
} 

class Solution 
{
    public:

        int findMinArrowShots(vector<vector<int>>& points) 
        {
            uint n = points.size();
            if(n < 2)
            {
                return n;
            }
            sort(points.begin(), points.end(), cmp);
            int arrows = points[0][1];
            uint count = 1;
            for(uint i = 1; i < n; i++)
            {
                if(points[i][0] > arrows)
                {
                    count++;
                    arrows = points[i][1];
                }
            }
            return count;
        }
};

//Redundant portion of code. Only meant for checks
void printVec(vector<vector<int>>& points)
    {
        for(vector<int> c: points)
        {
            for(int d : c)
            {
                cout<<d<<" ";
            }
            cout<<endl;
        }
    }