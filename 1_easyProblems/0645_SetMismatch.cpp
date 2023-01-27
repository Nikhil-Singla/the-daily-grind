class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) 
    {
        vector<int> ans(2);
        int n = nums.size();
        int sum = (n*(n+1))/2;
        int numSum = 0;
        set<int> map;
        for(auto c : nums)
        {
            if(map.find(c) != map.end())
            {
                ans[0] = c;
            }
            numSum += c;
            map.insert(c);
        }
        ans[1] = sum - numSum + ans[0];
        return ans;
    }
};