class Solution {
public:
    int tribonacci(int n) 
    {
        vector<int> ans;
        ans.push_back(0);
        ans.push_back(1);
        ans.push_back(1);
        for(auto i = 3; i <= n; i++)
        {
            ans.push_back(ans[i-1] + ans[i-2] + ans[i-3]);
        }    
        return ans[n];
    }
};