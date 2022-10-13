class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        vector<int> a;
        a.push_back(nums[0]);
        for(int i = 1; i < nums.size(); i++)
        {
            a.push_back(a[i-1]+nums[i]);
        }
        return a;
    }
};
