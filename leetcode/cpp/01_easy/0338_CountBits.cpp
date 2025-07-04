class Solution {
public:
    vector<int> countBits(int n) 
    {
        vector<int> ans;
        for(int i = 0; i <= n; i++)
        {
            int num = i;
            int res = 0;
            while(num != 0)
            {
                res += num%2;
                num /= 2;
            }
            ans.push_back(res);
        }
        return ans;
    }
};